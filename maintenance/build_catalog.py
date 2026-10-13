"""Render the MCP catalog from reviewed tool records; --check verifies tracked output."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def slug(value):
    return re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-')


def anchor(tool):
    return 'tool-' + slug('-'.join(filter(None, [tool.get('surface'), tool['name']])))


def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', '<br>')


def markdown_text(value):
    parts = re.split(r'(`+[^`]*`+|<?https?://[^\s<>`]+>?|<?[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}>?)', str(value))
    for i, part in enumerate(parts):
        if i % 2 == 0:
            parts[i] = part.replace('_', '\\_').replace('*', '\\*')
        elif not part.startswith(('`', '<')):
            parts[i] = '<' + part + '>'
    return ''.join(parts)


def code(value):
    return '`' + cell(json.dumps(value, ensure_ascii=False)) + '`'


def type_label(schema):
    if '$ref' in schema:
        return schema['$ref'].rsplit('/', 1)[-1]
    for union in ('anyOf', 'oneOf', 'allOf'):
        if union in schema:
            return ' / '.join(type_label(s) for s in schema[union])
    kind = schema.get('type', 'any')
    if isinstance(kind, list):
        return ' / '.join(kind)
    if kind == 'array':
        return 'array of ' + type_label(schema.get('items', {}))
    return kind


def restrictions(schema):
    labels = []
    for key in ('enum', 'const', 'minimum', 'maximum', 'exclusiveMinimum',
                'exclusiveMaximum', 'multipleOf', 'minLength', 'maxLength',
                'pattern', 'format', 'minItems', 'maxItems', 'uniqueItems'):
        if key in schema:
            labels.append(key + ': ' + json.dumps(schema[key], ensure_ascii=False))
    return cell('; '.join(labels)) or '—'


def schema_refs(schema, root):
    if isinstance(schema, dict):
        if '$ref' in schema:
            ref = schema['$ref']
            assert ref.startswith('#/'), f'External schema reference must be reviewed: {ref}'
            target = root
            for part in ref[2:].split('/'):
                target = target[part.replace('~1', '/').replace('~0', '~')]
        for value in schema.values():
            schema_refs(value, root)
    elif isinstance(schema, list):
        for value in schema:
            schema_refs(value, root)


def validate_record(record):
    assert re.fullmatch(r'[0-9a-f]{40}', record['commit']), record['repo']
    seen = set()
    for tool in record['tools']:
        key = (tool.get('surface', ''), tool['name'])
        assert key not in seen, (record['repo'], key)
        seen.add(key)
        assert isinstance(tool['description'], str)
        if tool.get('verified'):
            schema = tool['inputSchema']
            assert isinstance(schema, dict) and schema.get('type') == 'object', key
            assert set(schema.get('required', [])).issubset(schema.get('properties', {})), key
            schema_refs(schema, schema)
            assert tool['sources'], key
    ids = [anchor(t) for t in record['tools']]
    assert len(ids) == len(set(ids)), record['repo']


def tool_link(record, tool, prefix='docs/mcp/'):
    return f"[`{tool['name']}`]({prefix}{record['slug']}.md#{anchor(tool)})"


def render_page(record, entry, reviewed):
    tools = record['tools']
    gt = sum(t['domain'] == 'google-trends' for t in tools)
    surfaces = {t.get('surface', 'default') for t in tools}
    lines = [f"# {record['repo']}", '',
             '[Catalog](../../README.md) · [Tool name index](../tools.md) · '
             f"[Repository]({record['source_url']}) · [JSON definitions](../../data/mcp/{record['slug']}.json)", '',
             f"Reviewed {reviewed} at commit [`{record['commit'][:12]}`](https://github.com/{record['repo']}/tree/{record['commit']}).",
             '', entry['summary'], '',
             f"**{len(tools)} tool definitions; {gt} marked Google Trends.**"]
    if len(surfaces) > 1:
        lines += ['', 'Tool sets from different server surfaces are listed separately.']
    if not entry['included']:
        lines += ['', '**Outside the main catalog:** ' + entry['exclusion_reason']]
    notes = entry.get('notes', [])
    if notes:
        lines += [''] + ['- ' + note for note in notes]
    multi_surface = len(surfaces) > 1
    lines += ['', '## Tools', '', '| Tool | Scope' + (' | Surface |' if multi_surface else ' |'),
              '|---|---|---|' if multi_surface else '|---|---|']
    for t in tools:
        suffix = f" {cell(t.get('surface', 'default'))} |" if multi_surface else ''
        lines.append(f"| [`{t['name']}`](#{anchor(t)}) | {t['domain']} |" + suffix)
    if not tools:
        lines += ['', 'The full registered tool list could not be obtained. No tool names or schemas have been inferred from a REST API.']
    for t in tools:
        suffix = f" ({t['surface']})" if t.get('surface') else ''
        lines += ['', f'<a id="{anchor(t)}"></a>', '', f"### `{t['name']}`{suffix}", '']
        if t.get('implementation_status'):
            lines += [f"Implementation status: **{t['implementation_status']}**. {t['behavior']}", '']
        if t.get('behavior_verified') is False:
            lines += ['The hosted registration is verified; its implementation is not publicly available.', '']
        if t['description']:
            description = t['description'].rstrip()
            if len(description) > 500 or '\n' in description:
                lines += [markdown_text(t['behavior']), '', '<details>', '<summary>Full registered description</summary>', '',
                          '```text', description, '```', '', '</details>', '']
            else:
                lines += [markdown_text(description), '']
        else:
            lines += [markdown_text(t['behavior']), '', '*The registration supplies no description.*', '']
        if not t.get('verified') or not isinstance(t.get('inputSchema'), dict):
            lines += ['**Schema unavailable:** this definition is not counted as verified.', '']
        else:
            schema = t['inputSchema']
            props = schema.get('properties', {})
            required = set(schema.get('required', []))
            if props:
                lines += ['| Parameter | Type | Required | Schema default | Description | Constraints |',
                          '|---|---|---|---|---|---|']
                for name, spec in props.items():
                    lines.append(f"| `{name}` | {cell(type_label(spec))} | {'Yes' if name in required else 'No'} | "
                                 f"{code(spec['default']) if 'default' in spec else '—'} | "
                                 f"{cell(markdown_text(spec.get('description', ''))) or '—'} | {restrictions(spec)} |")
                lines += ['']
            else:
                lines += ['No caller parameters.', '']
            lines += ['<details>', '<summary>Complete input schema</summary>', '', '```json',
                      json.dumps(schema, ensure_ascii=False, indent=2), '```', '', '</details>', '']
        notes = [note for note in t.get('validation_notes', [])
                 if not note.startswith(('All inputs use plain scalar annotations;',
                                         'All registrations are unconditional.',
                                         'Default trendspy implementation has no additional explicit',
                                         'Timeframe/geo/category values are descriptive guidance,'))]
        if notes:
            lines += ['Implementation notes:', ''] + ['- ' + markdown_text(note) for note in notes] + ['']
        sources = t.get('sources', [])
        if sources:
            labels = []
            for i, source in enumerate(sources):
                label = source['path']
                if source.get('start_line'):
                    label += ':' + str(source['start_line'])
                labels.append(f"[{markdown_text(label)}]({source['url']})")
            lines += ['Sources: ' + ' · '.join(labels)]
    lines += ['', '## Schema provenance', '', record['extraction_method']]
    if record.get('limitations'):
        lines += [''] + ['- ' + note for note in record['limitations']]
    return '\n'.join(lines).rstrip() + '\n'


def render_index(records, reviewed):
    rows = [(r, t) for r in records for t in r['tools']]
    rows.sort(key=lambda rt: (rt[1]['name'].lower(), rt[0]['repo'].lower(), rt[1].get('surface', '')))
    unique = len({t['name'] for r, t in rows})
    lines = ['# MCP tool name index', '', '[Catalog](../README.md) · [CLIs and SDKs](clients.md)', '',
             f"{len(rows)} tool definitions, {unique} distinct names, {len(records)} inspected MCP providers. Reviewed {reviewed}.", '',
             'Search this page for an exact tool name. Non-Trends tools are included to make each provider’s full tool set searchable.', '',
             '| Tool name | MCP provider | Scope | Surface | Schema |', '|---|---|---|---|---|']
    for r, t in rows:
        lines.append(f"| {tool_link(r, t, 'mcp/')} | [{r['repo']}](mcp/{r['slug']}.md) | {t['domain']} | "
                     f"{cell(t.get('surface', 'default'))} | {'Verified definition' if t.get('verified') else 'Unavailable'} |")
    empty = [r for r in records if not r['tools']]
    if empty:
        lines += ['', '## Tool lists unavailable', '']
        for r in empty:
            lines.append(f"- [{r['repo']}](mcp/{r['slug']}.md): {r.get('reason', 'No complete tool schema was available.')}")
    return '\n'.join(lines) + '\n'


def render_main(manifest, records):
    lookup = {r['slug']: r for r in records}
    included = [e for e in manifest['entries'] if e['included']]
    included_records = [lookup[e['slug']] for e in included]
    definitions = sum(len(r['tools']) for r in included_records)
    trends = sum(t['domain'] == 'google-trends' and t.get('verified', False)
                 for r in included_records for t in r['tools'])
    lines = ['# Awesome Google Trends MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)', '',
             '> Discover what Google Trends MCP tools can do: compare search interest, find related demand, track live searches, and query published rankings.', '',
             '[Google Trends](https://trends.google.com/) · [MCP](https://modelcontextprotocol.io/) · '
             '[Every tool name](docs/tools.md) · [CLIs and SDKs](docs/clients.md)', '',
             f"**{len(included)} MCP providers · {trends} Google Trends tool definitions · {definitions} total definitions across documented surfaces.** "
             f"Reviewed {manifest['reviewed']}. Grouping follows registered tools and their implementations.", '',
             '## Contents', '']
    for group in manifest['groups']:
        count = sum(e['group'] == group['id'] for e in included)
        if count:
            lines.append(f"- [{group['title']} ({count})](#{slug(group['title'])})")
    lines += ['- [Tool name index](docs/tools.md)', '- [CLIs and SDKs](docs/clients.md)']
    for group in manifest['groups']:
        members = [e for e in included if e['group'] == group['id']]
        if not members:
            continue
        lines += ['', '## ' + group['title'], '', group['summary'], '',
                  '| MCP | What its tools do | Tools to explore |', '|---|---|---|']
        for entry in sorted(members, key=lambda e: lookup[e['slug']]['repo'].lower()):
            r = lookup[entry['slug']]
            tools = []
            for featured in entry['featured']:
                candidates = [t for t in r['tools'] if t['name'] == featured['name']
                              and (not featured.get('surface') or t.get('surface') == featured['surface'])]
                assert len(candidates) == 1, (entry['slug'], featured)
                t = candidates[0]
                assert t.get('verified') and t['domain'] in ('google-trends', 'server-management'), (entry['slug'], t['name'])
                tools.append(tool_link(r, t))
            count_label = entry.get('count_label', f"{len(r['tools'])} {'tool' if len(r['tools']) == 1 else 'tools'}")
            lines.append(f"| [**{r['repo']}**](docs/mcp/{r['slug']}.md) ({count_label}) | "
                         f"{cell(entry['summary'])} | {' · '.join(tools)} |")
    excluded = [e for e in manifest['entries'] if not e['included']]
    if excluded:
        lines += ['', '## Outside the verified catalog', '', '| MCP | Missing evidence |', '|---|---|']
        for entry in excluded:
            r = lookup[entry['slug']]
            lines.append(f"| [{r['repo']}](docs/mcp/{r['slug']}.md) | {cell(entry['exclusion_reason'])} |")
    return '\n'.join(lines) + '\n'


def validate_links(outputs):
    paths = set(outputs) | set(ROOT.glob('*.md')) | set((ROOT / 'docs').rglob('*.md'))
    anchors = {}
    for path in paths:
        text = outputs.get(path, path.read_text() if path.exists() else '')
        plain = re.sub(r'```.*?```', '', text, flags=re.S)
        ids = set(re.findall(r'<a id="([^"]+)"', plain))
        for heading in re.findall(r'^#{1,6} (.+)$', plain, re.M):
            ids.add(slug(heading))
        anchors[path.resolve()] = ids
    for path, text in outputs.items():
        plain = re.sub(r'```.*?```', '', text, flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)', plain):
            if target.startswith(('https://', 'http://')):
                continue
            filename, _, fragment = target.partition('#')
            dest = (path.parent / filename).resolve() if filename else path.resolve()
            assert dest in outputs or dest.exists(), (path.name, target)
            if fragment:
                assert fragment in anchors.get(dest, set()), (path.name, target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'data/catalog.json').read_text())
    records = []
    outputs = {}
    expected_slugs = {e['slug'] for e in manifest['entries']}
    assert len(expected_slugs) == len(manifest['entries'])
    assert {p.stem for p in (ROOT / 'data/mcp').glob('*.json')} == expected_slugs
    for entry in manifest['entries']:
        record = json.loads((ROOT / f"data/mcp/{entry['slug']}.json").read_text())
        assert record['slug'] == entry['slug']
        validate_record(record)
        if entry['included']:
            assert any(t['domain'] == 'google-trends' and t.get('verified') for t in record['tools'])
            assert all(t.get('verified') for t in record['tools']), entry['slug']
        records.append(record)
        outputs[ROOT / f"docs/mcp/{entry['slug']}.md"] = render_page(record, entry, manifest['reviewed'])
    outputs[ROOT / 'docs/tools.md'] = render_index(records, manifest['reviewed'])
    outputs[ROOT / 'README.md'] = render_main(manifest, records)
    validate_links(outputs)
    stale = []
    for path, text in outputs.items():
        if args.check:
            if not path.exists() or path.read_text() != text:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
    if stale:
        raise SystemExit('Generated files are stale: ' + ', '.join(stale))
    print(f"{'Checked' if args.check else 'Built'} {len(records)} MCP pages, tool index, and catalog; schemas, counts, uniqueness and links passed.")


if __name__ == '__main__':
    main()
