# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql,scrapy,os,pymongo
from scrapy.contrib.pipeline.images import ImagesPipeline
from twisted.enterprise import adbapi
from chainzproject.items import ChainzprojectItemWebInfoItem,ChainzprojectItem
from scrapy.utils.project import get_project_settings
images_store=get_project_settings().get('IMAGES_STORE')
# class ChainzprojectPipeline(object):
#     def __init__(self,dbpool):
#         self.dbpool=dbpool
#     #def from_crawl
#     @classmethod
#     def from_crawler(cls,crawler):
#         db_parmars={
#             'host':crawler.settings['MYSQL_HOST'],
#             'user':crawler.settings['MYSQL_USER'],
#             'password':crawler.settings['MYSQL_PWD'],
#             'db':crawler.settings['MYSQL_DB'],
#             'port':crawler.settings['MYSQL_PORT'],
#             'charset':crawler.settings['MYSQL_CHARSET'],
#         }
#         dbpool=adbapi.ConnectionPool('pymysql',**db_parmars)
#         return cls(dbpool)
#
#     def process_item(self, item, spider):
#         query=self.dbpool.runInteraction(self.insert_data_to_mysql,item)
#         query.addErrback(self.handle_error,item)
#         return item
#
#     def insert_data_to_mysql(self,cursor,item):
#         data_dict=dict(item)
#         sql,data=item.get_insert_sql_data(data_dict)
#         cursor.execute(sql,data)
#         print('正在插入数据')
#
#     def handle_error(self,failure,item):
#         print(failure)
#         print('插入错误')
#
#     def close_spider(self,spider):
#         self.cursor.close()
#         self.client.close()
#         print('爬虫结束')

from twisted.enterprise import adbapi
class ChainzprojectPipeline(object):

    def __init__(self,dbpool):
        self.dbpool=dbpool

    @classmethod
    def from_crawler(cls,crawler):
        """
        MYSQL_HOST = '127.0.0.1'
        MYSQL_USER = 'root'
        MYSQL_PWD = '19951028a'
        MYSQL_DB = 'chinaz'
        MYSQL_PORT = 3306
        MYSQL_CHARSET = 'utf8'
        """
        db_parmars={
            'host':crawler.settings['MYSQL_HOST'],
            'user': crawler.settings['MYSQL_USER'],
            'passwd': crawler.settings['MYSQL_PWD'],
            'db': crawler.settings['MYSQL_DB'],
            'port': crawler.settings['MYSQL_PORT'],
            'charset': crawler.settings['MYSQL_CHARSET'],
        }
        dbpool=adbapi.ConnectionPool('pymysql',**db_parmars)
        return cls(dbpool)

    def process_item(self,item,spider):

        query=self.dbpool.runInteraction(
            self.insert_data_to_mysql,
            item
        )
        query.addErrback(
            self.handle_error,
            item
        )
        return item
    def insert_data_to_mysql(self,cursor,item):

        data_dict=dict(item)
        sql,data=item.get_insert_sql_data(data_dict)
        cursor.execute(sql,data)

    def handle_error(self, failure, item):
        print(failure)
        print('插入错误')

    def close_spider(self,spider):
        self.cursor.close()
        self.client.close()
        print('爬虫结束')

class ChainzProjectImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if isinstance(item,ChainzprojectItemWebInfoItem):
            image_url='http:'+item['coverImage']
            print('获取图片地址',image_url)
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        if isinstance(item,ChainzprojectItemWebInfoItem):
            print('图片下载结果',results)
            paths=[result['path'] for status,result in results if status]
            if len(paths)>0:
                print('图片下载成功')
                os.rename(images_store+'/'+paths[0],images_store+'/'+item['title']+'.jpg')
                imgegeloca_path=images_store+'/'+item['title']+'.jpg'
                item['locakImagepath']=imgegeloca_path

            else:
                from scrapy.exceptions import DropItem
                raise DropItem('没有获取到图片,遗弃item')

            return item
