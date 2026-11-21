import sys, os, re, difflib
from bs4 import BeautifulSoup
O=os.path.expanduser('~/Backups/cnborn-blog-online-20261121')
rel=sys.argv[2]
def g(p):
    c=BeautifulSoup(open(p).read(),'html.parser').select_one('.article-content')
    h=re.sub(r'https?://cnborn\.net','',str(c))
    return [l.strip() for l in re.sub(r'>\s*<','>\n<',h).splitlines() if l.strip()]
for l in difflib.unified_diff(g(f'{O}/{rel}'),g(f'{sys.argv[1]}/{rel}'),lineterm='',n=1): print(l[:160])
