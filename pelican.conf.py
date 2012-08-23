# -*- coding: utf-8 -*-
AUTHOR = u'CNBorn'
SITENAME = u"CNBorn"
TAGLINE = u"Dharma's truth"
SITEURL = 'http://cnborn.net/blog/'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

GITHUB_URL = 'http://github.com/CNBorn/'
DISQUS_SITENAME = "cnborn"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_DATE_FORMAT = "%Y.%m.%d"
DEFAULT_PAGINATION = 2
DEFAULT_ORPHANS = 0
GOOGLE_ANALYTICS = "UA-329713-5"

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = (('OpenParty', 'http://www.beijing-open-party.org'),
        )

SOCIAL = (('Twitter', 'http://twitter.com/CNBorn'),
          ('Douban', 'http://www.douban.com/people/CNBorn/'),
          ('github', 'http://github.com/CNBorn'),
         )

# global metadata to all the contents
DEFAULT_METADATA = (('CNBorn', 'cnborn'),)

# static paths will be copied under the same name
STATIC_PATHS = ["images",]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

TIMEZONE = "Asia/Shanghai"
