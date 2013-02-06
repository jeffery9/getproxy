from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from proxybot.items import ProxybotItem
from scrapy.spider import BaseSpider

class GetproxySpider(CrawlSpider):
    name = 'getproxy.jp'
    allowed_domains = ['www.getproxy.jp']
    start_urls = ['http://www.getproxy.jp/en/china']

    rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths='//*[@class="pagination"]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)        
        rows = hxs.select('//*[@id="mytable"]/tr[position()>1]')
        items =[]
                        
        for row in rows:
                         
            item = ProxybotItem()                    
            item['IP'] = row.select('td[1]/text()').extract()[0]
            item['Type'] = row.select('td[7]/text()').extract()[0]
            item['CheckedDate'] = row.select('td[8]/text()').extract()[0]
                       
            items.append(item)           
        
        return items
