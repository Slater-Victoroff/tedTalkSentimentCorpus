# Scrapy settings for tedScraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'tedScraper'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['tedScraper.spiders']
NEWSPIDER_MODULE = 'tedScraper.spiders'
DEFAULT_ITEM_CLASS = 'tedScraper.items.TedscraperItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

