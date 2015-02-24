from __future__ import unicode_literals


# Pelican settings ------------------------------------------------------------

# Basic
SITENAME = 'Prewired'
SITEURL = 'http://prewired.pw'

AUTHOR = 'John T. Ombagi'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
THEME = 'theme/alchemy'
TIMEZONE = 'Africa/Nairobi'

# Plugins
PLUGINS = ['sitemap']

# Set to True when testing locally
RELATIVE_URLS = False


# Feeds
FEED_ATOM = 'feed/atom.xml'
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# URLs
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'
PAGE_LANG_URL = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'
PAGE_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}.html'
PAGE_URL = '{date:%Y}/{date:%m}/pages/{slug}.html'

# Delete the output directory, before generating new files
DELETE_OUTPUT_DIRECTORY = True

# The static paths you want to have accessible on the output path "static"
STATIC_PATHS = [
'images',
'extra/CNAME',
'extra/favicon.ico',
'extra/favicon-16x16.png',
'extra/favicon-32x32.png',
'extra/favicon-96x96.png',
'extra/favicon-160x160.png',
'extra/favicon-196x196.png',
'extra/robots.txt',
]
# Extra metadata dictionaries keyed by relative path
EXTRA_PATH_METADATA = {
'extra/CNAME': {'path': 'CNAME'},
'extra/favicon.ico': {'path': 'favicon.ico'},
'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
'extra/favicon-96x96.png': {'path': 'favicon-96x96.png'},
'extra/favicon-160x160.png': {'path': 'favicon-160x160.png'},
'extra/favicon-196x196.png': {'path': 'favicon-196x196.png'},
'extra/robots.txt': {'path': 'robots.txt'},
}
# Theme settings --------------------------------------------------------------
PAGES_ON_MENU = True
PROFILE_IMAGE = '/images/profile.png'
SHOW_ARTICLE_AUTHOR = True
SITE_SUBTEXT = 'Random Thoughts Aligned..'
META_DESCRIPTION = '''John Ombagi (aka Troon) personal blog and thoughts dump-site.
                        InfoSec, Linux, Oracle, Databases and rants. '''
EXTRA_FAVICON = True
LICENSE_URL = 'http://creativecommons.org/licenses/by/4.0/'
LICENSE_NAME = 'Creative Commons (4.0)'

# MENU_ITEMS = (
#    ('One', '#'),
#    ('Two', '#'),
# )


# Social widget
GITHUB_ADDRESS = 'https://github.com/JohnTroony'
TWITTER_ADDRESS = 'https://twitter.com/JohnTroony'
GPLUS_ADDRESS = 'https://plus.google.com/+JohnOmbagi'

DISQUS_SITENAME = 'Prewired'
