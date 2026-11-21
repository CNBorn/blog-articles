"""Extract ground-truth metadata from the online Pelican mirror."""
import json, re, sys, glob, os
from bs4 import BeautifulSoup

ROOT = os.path.expanduser('~/Backups/cnborn-blog-online-20261121/blog')

def soup(p):
    with open(p, encoding='utf-8') as f:
        return BeautifulSoup(f.read(), 'html.parser')

langs = {}
for lang in ('en', 'zh', 'cn'):
    for p in glob.glob(f'{ROOT}/lang/{lang}/index*.html'):
        for a in soup(p).select('#posts a[href]'):
            m = re.search(r'/blog/(\d{4}/\d{2}/[^/]+)/', a['href'])
            if m:
                langs.setdefault(m.group(1), set()).add(lang)

archives = []
for dt, dd in zip(soup(f'{ROOT}/archives.html').select('#posts dt'), soup(f'{ROOT}/archives.html').select('#posts dd')):
    m = re.search(r'/blog/(\d{4}/\d{2}/[^/]+)/', dd.a['href'])
    archives.append(m.group(1))

out = {}
for p in sorted(glob.glob(f'{ROOT}/20*/*/*/index.html')):
    key = os.path.relpath(os.path.dirname(p), ROOT)
    s = soup(p)
    art = s.select_one('#posts article')
    title = art.select_one('h1.title a').get_text()
    pub = art.select_one('.abbr.published')['title']
    meta = art.select_one('#article_meta')
    cats, tags = [], []
    for a in meta.select('a'):
        if '/category/' in a['href']:
            cats.append(a.get_text())
        elif '/tag/' in a['href']:
            tags.append(a.get_text())
    content = art.select_one('.article-content')
    imgs = [i.get('src') for i in content.select('img')]
    out[key] = dict(title=title, date=pub, categories=cats, tags=tags,
                    langs=sorted(langs.get(key, [])), listed=key in archives,
                    text=re.sub(r'\s+', '', content.get_text()), imgs=imgs,
                    links=[a.get('href') for a in content.select('a[href]')])

json.dump(out, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
print(len(out), 'articles;', sum(v['listed'] for v in out.values()), 'listed')
print('no lang:', [k for k, v in out.items() if not v['langs']])
print('multi lang:', {k: v['langs'] for k, v in out.items() if len(v['langs']) > 1})
print('categories:', sorted({c for v in out.values() for c in v['categories']}))
print('no category:', [k for k, v in out.items() if not v['categories']])
