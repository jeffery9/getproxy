# Scrapy settings for proxybot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'proxybot'

SPIDER_MODULES = ['proxybot.spiders']
NEWSPIDER_MODULE = 'proxybot.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1'

ITEM_PIPELINES = ['proxybot.pipelines.ProxybotPipeline', ]
