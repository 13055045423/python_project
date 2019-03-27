# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangprojectItem,DangdangprojectactileItem,DangdangprojectcontentItem

class DangdangprojectSpider(scrapy.Spider):
    name = 'dangdangproject'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://book.dangdang.com/']

    def parse(self, response):
        print(response.status)
        cotagry_urls = response.xpath('//div[@class="con flq_body"]/div[8]//div[@class="col eject_left"]/dl[1]/dd/a')
        #print(cotagry_urls)
        for cotagry in cotagry_urls:
            tag_item=DangdangprojectItem()
            firsturl=cotagry.xpath('./@href').extract_first('')
            #print(firsturl)
            tag_item['firsturl']=firsturl
            tagname=cotagry.xpath('./text()').extract_first('')
            tag_item['tagname']=tagname
            yield tag_item
            yield scrapy.Request(firsturl,callback=self.parse_tags_page)

    def parse_tags_page(self,response):
        print(response.status)
        #response.xpath('')
        book_item=DangdangprojectactileItem()
        book_urls=response.xpath('//ul[@id="component_59"]//li/a')

        for book in book_urls:
            book_urls=book.xpath('./@href').extract_first('')
            book_item['book_urls']=book_urls
            yield scrapy.Request(book_urls,callback=self.parse_actile_page)

        next_urls=response.xpath('//li[@class="next"]/a')
        #print(next_urls)
        for next in next_urls:
            if len(next_urls)>0:
                next_urls='http://category.dangdang.com'+next.xpath('./@href').extract_first('')
                print(next_urls)
                book_item['next_urls']=next_urls
                yield scrapy.Request(next_urls,callback=self.parse_tags_page)
            else:
                book_item['next_urls']=None
        yield book_item

            #if len(next_urls)>0:

    def parse_actile_page(self,response):
        book_dict=DangdangprojectcontentItem()
        book_dict['title']=response.xpath('//div[@class="name_info"]/h1/@title').extract_first('')
        book_dict['coverImage'] = response.xpath('//div[@id="largePicDiv"]/a[1]/img/@src').extract_first('')
        book_dict['content'] = response.xpath('//span[@class="head_title_name"]/@title').extract_first('').replace('\xa0','').replace(' ','')
        book_dict['author'] = response.xpath('//span[@id="author"]/a[1]/text()').extract_first('暂无')
        book_dict['biming'] = response.xpath('//span[@id="author"]/a[2]/text()').extract_first('暂无')
        book_dict['chuping'] = response.xpath('//span[@id="author"]/a[2]/text()').extract_first('暂无')
        book_dict['publish_company'] = response.xpath('//div[@class="messbox_info"]/span[2]/a[1]/text()').extract_first('暂无')
        book_dict['publist_time'] = response.xpath('//div[@class="messbox_info"]/span[3]/text()').extract_first('暂无').replace('\xa0','')
        book_dict['commentnum'] = response.xpath('//a[@id="comm_num_down"]/text()').extract_first('暂无')
        book_dict['now_price'] = response.xpath('//p[@id="dd-price"]/text()').extract_first('暂无')
        # book_dict['hotnum'] = response.xpath('')
        # book_dict['locakImagePath'] = response.xpath('')
        yield book_dict