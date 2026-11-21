"""Compare built Hugo site against the online Pelican mirror, page by page."""
import difflib, glob, os, re, sys
from bs4 import BeautifulSoup

ONLINE = os.path.expanduser('~/Backups/cnborn-blog-online-20261121')
SITE = sys.argv[1]
verbose = '-v' in sys.argv


def norm_url(u):
    if not u:
        return u
    u = re.sub(r'^https?://(www\.)?cnborn\.net', '', u)
    if u.startswith('/images/'):
        u = '/blog' + u  # was broken online, fixed in hugo
    return u


def load(root, rel):
    p = os.path.join(root, rel)
    if not os.path.exists(p):
        return None
    return BeautifulSoup(open(p, encoding='utf-8').read(), 'html.parser')


def text(el):
    return re.sub(r'\s+', '', el.get_text()) if el else ''


def summary(rel, sel):
    a, b = load(ONLINE, rel), load(SITE, rel)
    if b is None:
        return ['MISSING in site']
    issues = []
    for what in ('title',):
        ta, tb = a.title.get_text().strip(), b.title.get_text().strip()
        if ta != tb:
            issues.append(f'<title> {ta!r} != {tb!r}')
    ea, eb = a.select(sel), b.select(sel)
    if len(ea) != len(eb):
        issues.append(f'{sel}: {len(ea)} vs {len(eb)} elements')
    for x, y in zip(ea, eb):
        tx, ty = text(x), text(y)
        if tx != ty:
            r = difflib.SequenceMatcher(None, tx, ty).ratio()
            issues.append(f'text differs ratio={r:.4f}')
            if verbose:
                for op in difflib.SequenceMatcher(None, tx, ty).get_opcodes():
                    if op[0] != 'equal':
                        issues.append(f'   {op[0]}: {tx[op[1]-10:op[2]+10]!r} -> {ty[op[3]-10:op[4]+10]!r}')
        ia = [norm_url(i.get('src')) for i in x.select('img')]
        ib = [norm_url(i.get('src')) for i in y.select('img')]
        if ia != ib:
            issues.append(f'imgs differ: {set(ia) ^ set(ib)}')
        la = [norm_url(i.get('href')) for i in x.select('a[href]')]
        lb = [norm_url(i.get('href')) for i in y.select('a[href]')]
        if la != lb:
            issues.append(f'links differ: {sorted(set(la) ^ set(lb))[:6]}')
        # structural tags
        sa = [t.name for t in x.find_all(True)]
        sb = [t.name for t in y.find_all(True)]
        if sa != sb:
            issues.append(f'tag structure differs ({len(sa)} vs {len(sb)})')
    # article meta
    ma, mb = a.select_one('#article_meta'), b.select_one('#article_meta')
    if ma and text(ma) != text(mb):
        issues.append(f'meta {text(ma)!r} != {text(mb)!r}')
    pa, pb = a.select_one('.abbr.published'), b.select_one('.abbr.published')
    if pa and pb and (pa.get('title') != pb.get('title') or text(pa) != text(pb)):
        issues.append(f'published {pa.get("title")} != {pb.get("title")}')
    return issues


pages = sorted(os.path.relpath(p, ONLINE) for p in glob.glob(f'{ONLINE}/blog/20*/*/*/index.html'))
pages = [p for p in pages if 'duo-lun-duo-yi-nian' not in p]
others = ['blog/pages/about/index.html', 'blog/pages/projects/index.html', 'blog/pages/404/index.html',
          'blog/index.html', 'blog/archives.html', 'blog/categories.html', 'blog/tags.html',
          'blog/lang/en/index.html', 'blog/lang/zh/index.html'] + \
    sorted(os.path.relpath(p, ONLINE) for p in glob.glob(f'{ONLINE}/blog/category/*/index.html')) + \
    sorted(os.path.relpath(p, ONLINE) for p in glob.glob(f'{ONLINE}/blog/tag/*/index.html'))

bad = 0
for rel in pages:
    iss = summary(rel, '.article-content')
    if iss:
        bad += 1
        print(rel)
        for i in iss:
            print('   ', i)
for rel in others:
    iss = summary(rel, '#posts')
    if iss:
        bad += 1
        print(rel)
        for i in iss:
            print('   ', i)
print(f'{len(pages)} articles + {len(others)} other pages checked, {bad} with differences')
