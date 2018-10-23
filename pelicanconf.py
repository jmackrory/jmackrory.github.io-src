#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'J. Mackrory'
SITENAME = "Jonathan's Data Science Portfolio"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
SOCIAL = (('github', 'https://github.com/jmackrory'),)

DEFAULT_PAGINATION = 10

#THEME="pelican-themes/pelican-blue"
THEME="pelican-themes/pure-single"
COVER_IMG_URL="blog/img_4005.jpg"

STATIC_PATHS=['blog']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Added lines to allow pelican-ipynb plugin to work
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

MENU_ITEMS=['About Me']
