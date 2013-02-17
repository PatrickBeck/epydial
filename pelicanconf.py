#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Frank Gau'
SITENAME = u'epydial'
SITEURL = 'http://epydial.pyneo.org'
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 10
THEME = "epydialtheme"

MD_EXTENSIONS = (['codehilite','extra','nl2br'])
# http://pythonhosted.org/Markdown/extensions/index.html

DIRECT_TEMPLATES = ('index', 'blog')
USE_FOLDER_AS_CATEGORY = (True)
PAGINATED_DIRECT_TEMPLATES = (('blog',))
DISQUS_SITENAME = 'epydial'
