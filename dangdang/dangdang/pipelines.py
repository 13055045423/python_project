# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql,scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
from dangdang.items import DangdangprojectcontentItem

class DangdangprojectImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if isinstance(item,DangdangprojectcontentItem):
            image_url=item['coverImage']
            print('获取图片地址',image_url)
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        if isinstance(item,DangdangprojectcontentItem):
            print('图片下载结果',results)
            paths=[result['path'] for status,result in results if status]
            if len(paths)>0:
                print('图片下载成功')
                print(paths)
                imgageloca_path=paths[0]
                item['locakImagePath']=imgageloca_path
            else:
                from scrapy.exceptions import DropItem
                raise DropItem('没有获取到图片,遗弃item')
        return item

class DangdangPipeline(object):
    def __init__(self):
        self.client=pymysql.Connect('127.0.0.1','root','19951028a','dd',3306,charset='utf8')
        self.cursor=self.client.cursor()

    def open_spider(self,spider):
        print('爬虫开始')

    def process_item(self,item,spider):
        data_dict=dict(item)
        sql = """insert into Persons(%s) values(%s)"""%(','.join(data_dict.keys()),','.join(['%s']*len(data_dict)))
        try:
            self.cursor.execute(sql,list[data_dict.values()])
            self.client.commit()
        except Exception as err:
            self.client.rollback()
            print(err)
        return item
        print('经过了管道')

    def close_spider(self,spider):
        self.cursor.close()
        self.client.close()
        print('爬虫结束')
