# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FivesingyinyueyuanchuangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fenleiname=scrapy.Field()
    fenleiurl=scrapy.Field()
    mokuai=scrapy.Field()

    def insert_sql_data_by_dictdata(self, dictdata):
        sql = """
        INSERT INTO yuanchuangfenlei (%s)
        VALUES (%s)
        """ % (
            ','.join(dictdata.keys()),
            ','.join(['%s'] * len(dictdata))
        )
        data = list(dictdata.values())
        return sql,data

# create table yuanchuangfenlei(
#     id int auto_increment not null,
#     fenleiname varchar(255),
#     fenleiurl varchar(255),
#     mokuai varchar(255),
#     primary key(id)
# )


class FivesingyinyueyuanchuangfenleiItem(scrapy.Item):
    zhonglei=scrapy.Field()
    image_url=scrapy.Field()
    bofangliang=scrapy.Field()
    gedanname=scrapy.Field()
    zuozhe=scrapy.Field()
    gedanurl=scrapy.Field()

    def insert_sql_data_by_dictdata(self, dictdata):
        sql = """
        INSERT INTO gedaninfo (%s)
        VALUES (%s)
        """ % (
            ','.join(dictdata.keys()),
            ','.join(['%s'] * len(dictdata))
        )
        data = list(dictdata.values())
        return sql, data

# create table gedaninfo(
#     id int auto_increment not null,
#     zhonglei varchar(255),
#     image_url varchar(255),
#     bofangliang varchar(255),
#     gedanname varchar(255),
#     zuozhe varchar(255),
#     gedanurl varchar(255),
#     primary key(id)
# )

class FivesingprojectcontentItem(scrapy.Item):
    gendan_title=scrapy.Field()
    chuangjianshijian = scrapy.Field()
    chuangjianren = scrapy.Field()
    bofangcishu = scrapy.Field()
    shoucang = scrapy.Field()
    # fenxiang=scrapy.Field()
    biaoqian = scrapy.Field()
    jianjie = scrapy.Field()
    gequshuliang = scrapy.Field()
    gequxuhao = scrapy.Field()
    gequmingcheng = scrapy.Field()
    gequurl = scrapy.Field()
    gequzuozhe = scrapy.Field()
    danqubofangliang = scrapy.Field()

    def insert_sql_data_by_dictdata(self, dictdata):
        sql = """
        INSERT INTO gedancontentinfo (%s)
        VALUES (%s)
        """ % (
            ','.join(dictdata.keys()),
            ','.join(['%s'] * len(dictdata))
        )
        data = list(dictdata.values())
        return sql,data

# create table gedancontentinfo(
#     id int auto_increment not null,
#     gendan_title varchar(255),
#     chuangjianshijian varchar(255),
#     chuangjianren varchar(255),
#     bofangcishu varchar(255),
#     shoucang varchar(255),
#     biaoqian varchar(255),
#     jianjie varchar(255),
#     gequshuliang varchar(255),
#     gequxuhao varchar(255),
#     gequmingcheng varchar(255),
#     gequurl varchar(255),
#     gequzuozhe varchar(255),
#     danqubofangliang varchar(255),
#     primary key(id)
# )

