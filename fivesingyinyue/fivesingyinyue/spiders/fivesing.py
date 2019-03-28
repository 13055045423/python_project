# -*- coding: utf-8 -*-
import scrapy
from fivesingyinyue.items import FivesingyinyueyuanchuangItem,FivesingyinyueyuanchuangfenleiItem,FivesingprojectcontentItem

class FivesingSpider(scrapy.Spider):
    name = 'fivesing'
    allowed_domains = ['kugou.com']
    start_urls = ['http://5sing.kugou.com/index.html']

    def parse(self, response):
        print(response.status,response.url)
        gedan_url=response.xpath('//div[@class="nav"]/ul/li[6]/a/@href').extract_first('')
        print(gedan_url)
        yield scrapy.Request(gedan_url,callback=self.gedan_page)

    def gedan_page(self,respose):
        print(respose.status,respose.url)
        fenlei_wenben=respose.xpath('//div[@class="rbox r_list"]//div/ul//li/a')
        #print(fenlei_wenben)
        for fenlei in fenlei_wenben[2:3]:
            print(fenlei)
            item=FivesingyinyueyuanchuangItem()
            item['fenleiname'] = fenlei.xpath('./text()').extract_first('')
            fenleiurl = 'http://5sing.kugou.com/gd/gdList?tagName='+fenlei.xpath('./text()').extract_first('')
            print(fenleiurl)
            item['fenleiurl']=fenleiurl
            item['mokuai']='歌单'
            yield item
            yield scrapy.Request(fenleiurl,callback=self.fenlei_page)
    def fenlei_page(self,response):
        print(response.status,response.url)
        li_list=response.xpath('//div[@class="lbox l_recom l_alist"]/ul[@class="fix"]//li')
        for li in li_list:
            #print(li)
            gedan_item=FivesingyinyueyuanchuangfenleiItem()
            gedan_item['zhonglei'] = response.xpath('//span[@id="tagName"]/text()').extract_first('')
            #yield gedan_item
            gedan_item['image_url'] = li.xpath('./dl/dt/a/img/@src').extract_first('')
            gedan_item['bofangliang'] = li.xpath('./dl/dt/div/span/text()').extract_first('')
            gedan_item['gedanname'] = li.xpath('./dl/dd/a/text()').extract_first('')
            gedan_item['zuozhe'] = li.xpath('./dl/dd[2]/a[2]/text()').extract_first('')
            gedanurl = li.xpath('./dl/dt/a/@href').extract_first('')
            gedan_item['gedanurl']=gedanurl
            yield gedan_item
            yield scrapy.Request(gedanurl,callback=self.content_page)

    def content_page(self,response):
        print(response.status,response.url)
        content_item=FivesingprojectcontentItem()
        content_item['gendan_title'] = response.xpath('//dd[@class="lt w_70 p_rel"]/h2/span[2]/text()').extract_first('')
        content_item['chuangjianshijian'] = response.xpath('//div[@class="c_wap s_cont"]/span[1]').extract_first('').replace('<span class="lt">','').replace('</span>','').replace('<em>','').replace('</em>','')
        content_item['chuangjianren'] = response.xpath('//div[@class="c_wap s_cont"]/span[2]/a/text()').extract_first('')
        content_item['bofangcishu'] = response.xpath('//div[@class="c_wap s_cont"]/span[3]/text()').extract_first('')
        content_item['shoucang'] = response.xpath('//div[@class="c_wap act_box"]/a[2]/text()').extract_first('').replace('\xa0\xa0(','').replace(')','').replace('收藏','')
        # fenxiang=scrapy.Field()
        content_item['biaoqian'] = response.xpath('//div[@class="c_wap tag_box"]//label/text()').extract_first('')
        content_item['jianjie'] = response.xpath('//p[@id="normalIntro"]/text()').extract_first('')
        content_item['gequshuliang'] = response.xpath('//span[@class="lt bicon"]/span/text()').extract_first('').replace('（','').replace('）','')
        ge_list=response.xpath('//ul[@class="c_wap dj_songitems"]//li')
        for ge in ge_list:
            content_item['gequxuhao'] = ge.xpath('./cite/text()').extract_first('')
            content_item['gequmingcheng'] = ge.xpath('./span[1]/a/text()').extract_first('')
            content_item['gequurl'] = ge.xpath('./span[1]/a/@href').extract_first('')
            content_item['gequzuozhe'] = ge.xpath('./span[2]/a/text()').extract_first('')
            content_item['danqubofangliang'] = ge.xpath('./span[4]/text()').extract_first('')

        yield content_item







