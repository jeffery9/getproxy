# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import urllib2
from scrapy import log

class ProxybotPipeline(object):
    def __init__(self):
       self.file = open('proxy_list', 'wb')
             
    def __del__(self):
        self.file.close()
        pass
    
    def process_item(self, item, spider):   
        string = item['IP']
        type =item['Type']               
                           
        try:
            proxy_string = 'http://%s' % (string)
            print 'validating proxy ... ', proxy_string
            proxy_support = urllib2.ProxyHandler({"http":proxy_string})
            opener = urllib2.build_opener(proxy_support)
            urllib2.install_opener(opener)                        
            urllib2.urlopen('http://edition.cnn.com/')
            
            log.msg('proxy worked ...')    
            print proxy_string        
            self.file.writelines(proxy_string)
            self.file.writelines('\n')   
                            
        except urllib2.HTTPError, e:
            log.msg('The server couldn\'t fulfill the request.')
            print 'Error code: ', e.code
                        
        except urllib2.URLError, e:
            log.msg('We failed to reach a server.')
            print  'Reason: ', e.reason
                                     
        return item
        
    def close_spider(self, spider):
        pass
        