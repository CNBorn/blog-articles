"""Convert Pelican sources into Hugo content, using the online mirror as metadata truth.

usage: convert.py online.json <pelican_src_dir> <hugo_content_dir>
"""
import json, os, re, sys, glob

online = json.load(open(sys.argv[1]))
SRC, DST = sys.argv[2], sys.argv[3]
CAT_FIX = {'Projects': 'projects', 'tech': 'Tech'}
UNLISTED = {'2014/09/reading-in-myanmar-part-two'}
SKIP = {'2016/08/duo-lun-duo-yi-nian'}  # handled by redirect


def parse(path):
    raw = open(path, encoding='utf-8').read()
    meta = {}
    if path.endswith('.md'):
        head, _, body = raw.partition('\n\n')
        for line in head.splitlines():
            k, _, v = line.partition(':')
            meta[k.strip().lower()] = v.strip()
    else:
        lines = raw.splitlines()
        i = 0
        while not lines[i].strip():
            i += 1
        meta['title'] = lines[i].strip()
        i += 2
        while i < len(lines) and (lines[i].startswith(':') or not lines[i].strip()):
            m = re.match(r':(\w+):\s*(.*)', lines[i])
            if m:
                meta[m.group(1).lower()] = m.group(2).strip()
            i += 1
        body = '\n'.join(lines[i:]) + '\n'
    return meta, body


sources = []
for p in glob.glob(f'{SRC}/**/*', recursive=True):
    if p.endswith(('.md', '.rst')) and '/pages/' not in p and os.path.basename(p) != 'README.md':
        meta, body = parse(p)
        sources.append((p, meta, body))


def norm_title(t):
    t = t.replace('&quot;', '"').replace('&amp;', '&')
    return re.sub(r'\s+', '', t)


def find_source(key, info):
    ym = key[:7].replace('/', '-')
    slug = key[8:]
    cands = [s for s in sources if s[1].get('date', '').startswith(ym)]
    for s in cands:
        if s[1].get('slug') == slug:
            return s
    for s in cands:
        if norm_title(s[1].get('title', '')) == norm_title(info['title']):
            return s
    raise SystemExit(f'no source for {key}')


# map source filename -> online url (for {filename} links)
url_of = {}
matched = {}
for key, info in online.items():
    if key in SKIP:
        continue
    s = find_source(key, info)
    matched[key] = s
    url_of[os.path.relpath(s[0], SRC)] = f'/blog/{key}/'


def fix_body(body):
    body = re.sub(r'\{(?:filename|static)\}/?images/', '/blog/images/', body)

    def link(m):
        target = m.group(1).lstrip('/')
        if target not in url_of:
            raise SystemExit(f'unresolved {{filename}} link {target}')
        return url_of[target]
    body = re.sub(r'\{filename\}(/?[^)\s"]+\.(?:md|rst))', link, body)
    body = re.sub(r'https?://(?:www\.)?cnborn\.net/(blog|docs)/', r'/\1/', body)
    body = re.sub(r'https?://(?:www\.)?cnborn\.net(?![\w.-])/?', '/', body)
    body = re.sub(r'(\]\(|src=["\']|image:: )/images/', r'\1/blog/images/', body)
    return body


def yq(s):
    return json.dumps(s, ensure_ascii=False)


os.makedirs(f'{DST}/posts', exist_ok=True)
used = set()
for key, (path, meta, body) in sorted(matched.items()):
    info = online[key]
    ext = os.path.splitext(path)[1]
    name = key.replace('/', '-') + ext
    assert name not in used
    used.add(name)
    lang = [l for l in info['langs'] if l != 'cn'] or ['zh']
    fm = ['---', f'title: {yq(info["title"])}', f'date: {info["date"]}',
          f'slug: {yq(key[8:])}', f'url: {yq("/blog/" + key + "/")}',
          f'original_language: {lang[0]}']
    cats = [CAT_FIX.get(c, c) for c in info['categories']]
    fm.append('categories: [' + ', '.join(yq(c) for c in cats) + ']')
    if info['tags']:
        fm.append('tags: [' + ', '.join(yq(t) for t in info['tags']) + ']')
    if key in UNLISTED:
        fm += ['build:', '  list: never']
    fm.append(f'source_file: {yq(os.path.relpath(path, SRC))}')
    fm.append('---')
    with open(f'{DST}/posts/{name}', 'w', encoding='utf-8') as f:
        b = fix_body(body).lstrip('\n')
        if ext == '.md':
            # Python-Markdown treats a --- line right under a paragraph as <hr>; goldmark as setext h2
            b = re.sub(r'(?m)^([^\n]*\S[^\n]*)\n( {0,3}(?:-{3,}|\*{3,}))[ \t]*$', r'\1\n\n\2', b)
        f.write('\n'.join(fm) + '\n\n' + b)

# pages
os.makedirs(f'{DST}/pages', exist_ok=True)
for p in glob.glob(f'{SRC}/pages/*.md'):
    meta, body = parse(p)
    slug = meta['slug']
    fm = ['---', f'title: {yq(meta["title"])}', f'slug: {yq(slug)}',
          f'url: {yq("/blog/" if slug == "Home" else "/blog/pages/" + slug + "/")}']
    if meta.get('status') == 'hidden':
        fm += ['build:', '  list: never']
    fm.append('---')
    with open(f'{DST}/pages/{slug.lower()}.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(fm) + '\n\n' + fix_body(body).lstrip('\n'))

unused = [os.path.relpath(s[0], SRC) for s in sources if os.path.relpath(s[0], SRC) not in url_of]
print('wrote', len(matched), 'posts; sources not online:', len(unused))
for u in sorted(unused):
    print('  ', u)
