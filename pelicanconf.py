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

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'blog')
PAGINATED_DIRECT_TEMPLATES = (('blog',))
DISQUS_SITENAME = 'epydial'
