# -*- coding: utf-8 -*-
AUTHOR = u'Tyler Xing'
SITENAME = u"Tyler Xing"
TAGLINE = u"Dharma's truth"
SITEURL = 'http://cnborn.net/blog/'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
TAG_URL = 'tag/{name}/'
TAG_SAVE_AS = 'tag/{name}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{name}/'
CATEGORY_SAVE_AS = 'category/{name}/index.html'
AUTHOR_SAVE_AS = ''
ARTICLE_LANG_SAVE_AS = ARTICLE_SAVE_AS
DRAFT_SAVE_AS = ''

GITHUB_URL = 'http://github.com/CNBorn/'
DISQUS_SITENAME = "cnborn"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_DATE_FORMAT = "%Y.%m.%d"
DEFAULT_PAGINATION = 1
DEFAULT_ORPHANS = 0
GOOGLE_ANALYTICS = "UA-329713-5"

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

PLUGIN_PATHS = ['/Users/benxing/Projects/',]
PLUGINS = ['pelican-langcategory']

LANGUAGE_URL = 'lang/{lang}/'
LANGUAGE_SAVE_AS = 'lang/{lang}/index.html'

MENUITEMS = (
    ('Reading', '/blog/category/Reading/'),
    ('Travel', '/blog/category/Traveling/'),
    ('EN', '/blog/lang/en/'),
    ('CN', '/blog/lang/cn/'),
)

LINKS = (('OpenParty', 'http://www.beijing-open-party.org'),
        )

SOCIAL = (('Twitter', 'http://twitter.com/CNBorn'),
          ('Douban', 'http://www.douban.com/people/CNBorn/'),
          ('github', 'http://github.com/CNBorn'),
         )

LINKS = ()
SOCIAL = ()


# global metadata to all the contents
DEFAULT_METADATA = (('CNBorn', 'cnborn'),)

# static paths will be copied under the same name
STATIC_PATHS = ["images",]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

TIMEZONE = "Asia/Shanghai"

IGNORE_FILES = ['.DS_Store', 'legacy/*.rst', '*.rst', 'README.md']
