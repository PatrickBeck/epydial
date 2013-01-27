#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Frank Gau'
SITENAME = u'epydial'
SITEURL = 'http://epydial.pyneo.org'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
THEME = "epydialtheme"

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'blog')
PAGINATED_DIRECT_TEMPLATES = (('blog',))
DISQUS_SITENAME = 'epydial'
