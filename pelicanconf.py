#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Institute fo Numerical Simulation'
SITENAME = u'PADME-AM'
SITEURL = ''
SITE_SUMMARY = 'PADME-AM - Partition of Unity Methods for Additive Manufacturing'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'
LOCALE = "C"
DEFAULT_DATE_FORMAT = '%a %d %B %Y'


THEME = 'themes/polar'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Institute for Numerical Simulation', 'https://ins.uni-bonn.de/'),
         ('Institute for Software Technology', 'http://www.dlr.de/sc/en/'),
         ('Institute of Materials Science', 'http://www.dlr.de/wf/en/'),
         ('Access Technology', 'https://access-technology.de/'),
         ('Fraunhofer SCAI', 'https://www.scai.fraunhofer.de/en.html'),
         ('Imprint', 'https://ins.uni-bonn.de/content/impressum'),
         ('Privacy', 'https://ins.uni-bonn.de/content/privacy'))

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

SITEMAP = {
    'exclude': ['author/'],
    'format': 'xml',
    'changefreqs': {
        'articles': 'weekly',
        'pages': 'monthly',
        'indexes': 'yearly'
    }
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Static paths
STATIC_PATHS = ['images', 'pages/images', 'extra/CNAME']
ARTICLE_EXCLUDES = []

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['pelican-page-hierarchy.page_hierarchy', 'sitemap', 'pelican-open_graph']

# Github pages domain name
# EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}