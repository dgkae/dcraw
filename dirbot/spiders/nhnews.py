'''
jiaxing zaixian 
cnjxol.com
news
'''
from dirbot.items import TextItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import log
from scrapy import Spider
import scrapy
import json
import sys
import hashlib   
from dborm.settings import push_url
from dborm.settings import isexist_url
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

log.msg("This is a warning", level=log.WARNING)

reload(sys)
sys.setdefaultencoding("utf-8")

def Catch0(list):
    if len(list) > 0:
        return list[0]
    else:
        return "null"

def mm5(l):

    m2 = hashlib.md5()   
    m2.update(l)   
    return m2.hexdigest()   

class MininovaSpider(Spider):

    name = 'nhnews'
    allowed_domains = ['jx.zjol.com.cn']

    start_urls = ["http://jx.zjol.com.cn/"]



    def parse(self, response):

        #get all links
        # baseurl = response.xpath('//base/@href').extract()[0]
        #baseurl = "http://www.cnjxol.com/"
        baseurl = get_base_url(response)

        log.msg(response.url, level=log.WARNING)
        # log.msg(response.body, level=log.WARNING)

        mm5t = mm5(response.url)
        push_url(mm5t)

        linklist = response.xpath('//a/@href').extract()



        # a = ('/html/body/table[13]/tr/td[1]/table[1]/tr/td/table[3]/tr/td/table/tr/td/table[1]/tr[6]/td/span')
        a = '//body'

        data = response.xpath(a)
        infos = data.xpath('string(.)').extract()

        content = Catch0(infos)

        if content  == "null" or len(content) < 200:
            log.msg("NO non no conent\n", level=log.WARNING)
            pass
        else:
            item = TextItem()
            lent = len(content)
            content = content[int(lent*0.25) : int(lent*0.75)]


            item['text'] = content
            log.msg(content, level=log.WARNING)

            
            yield item
        

        for uuu in linklist:
            fullurl = urljoin_rfc(baseurl, uuu)
            print(fullurl)
            tm5 = mm5(fullurl)
            if isexist_url(tm5):
                pass
            else:
                log.msg(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"+fullurl, level=log.WARNING)
                push_url(mm5t)

                if 'cn/system' in fullurl:
                    yield scrapy.Request(fullurl)

        