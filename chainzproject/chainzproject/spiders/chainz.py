# -*- coding: utf-8 -*-
import scrapy
from chainzproject.items import ChainzprojectItem,ChainzprojectItemWebInfoItem

class ChainzSpider(scrapy.Spider):
    name = 'chainz'
    allowed_domains = ['chinaz.com']
    start_urls = ['http://top.chinaz.com/hangyemap.html']

    def parse(self, response):
        print(response.status)
        tags=response.xpath('//div[@class="Taright"]/a')
        for tag in tags:
            tag_item=ChainzprojectItem()
            tag_item['tagname'] = tag.xpath('./text()').extract_first('')
            firsturl = tag.xpath('./@href').extract_first('')
            tag_item['firsturl']=firsturl
            yield tag_item
            yield scrapy.Request(firsturl,callback=self.parse_tags_page)

    def parse_tags_page(self,response):
        print(response.status)
        webInfos=response.xpath('//ul[@class="listCentent"]//li')
        for webInfo in webInfos:
            web_item=ChainzprojectItemWebInfoItem()
            web_item['coverImage'] = webInfo.xpath('./div[1]/a/img/@src').extract_first('')
            web_item['title'] = webInfo.xpath('./div[2]/h3/a/text()').extract_first('')
            web_item['domenis'] = webInfo.xpath('./div[2]/h3/span/text()').extract_first('')
            web_item['week_rank'] = webInfo.xpath('./div[2]/div[1]/p[1]/a/text()').extract_first('')
            web_item['ulink'] = webInfo.xpath('./div[2]/div[1]/p[4]/a/text()').extract_first('')
            web_item['info'] = webInfo.xpath('./div[2]/div[1]/p[5]/text()').extract_first('')
            web_item['score'] = webInfo.xpath('./div[3]/div/span/text()').extract_first('')
            web_item['rank'] = webInfo.xpath('./div[3]/div/strong/text()').extract_first('')
            #web_item['locakImagePath'] = webInfo.xpath('')
            print(web_item)
        next_urls=response.xpath('//div[@class="ListPageWrap"]//a').extract()[1:]
        #print(next_urls)
        for next_url in next_urls:
            next_url=response.urljoin(next_url)
            yield scrapy.Request(next_url,callback=self.parse_tags_page)
            print('======================获取下一页')



