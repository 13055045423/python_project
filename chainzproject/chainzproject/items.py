# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChainzprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tagname=scrapy.Field()
    firsturl = scrapy.Field()
    # def get_insert_sql_data(self,datadict):
    #     sql = """insert into china(%s) values (%s)"""%(','.join(datadict.keys()),','.join(['%s']*len(datadict)))
    #     data=list(datadict.values())
    #     return sql,data
# create table china(
#     id int,
#     tagname varchar(255),
#     firsturl varchar(255),
#     primary key(id)
# )
    def get_insert_sql_data(self, datadict):
        """
        １创建sql语句
        2返回要存储的数据
        :param datadict:
        :return:
        """
        sql = """insert into china(%s) values(%s)""" % (','.join(datadict.keys()), ','.join(['%s'] * len(datadict)))
        data = list(datadict.values())
        return sql, data


class ChainzprojectItemWebInfoItem(scrapy.Item):
    coverImage=scrapy.Field()
    title=scrapy.Field()
    domenis=scrapy.Field()
    week_rank=scrapy.Field()
    ulink=scrapy.Field()
    info=scrapy.Field()
    score=scrapy.Field()
    rank=scrapy.Field()
    locakImagePath=scrapy.Field()
    # def get_insert_sql_data(self,datadict):
    #     sql = """insert into chinatable(%s) values(%s)"""%(','.join(datadict.keys()),','.join(['%s']*len(datadict)))
    #     data=list(datadict.values())
    #     return sql,data

    def get_insert_sql_data(self, datadict):
        """
        １创建sql语句
        2返回要存储的数据
        :param datadict:
        :return:
        """
        sql = """insert into chinatable(%s) values(%s)""" % (','.join(datadict.keys()), ','.join(['%s'] * len(datadict)))
        data = list(datadict.values())
        return sql, data

# create table chinatable(
#     id int,
#     coverImage varchar(255),
#     title varchar(255),
#     domenis varchar(255),
#     week_rank varchar(255),
#     ulink varchar(255),
#     info varchar(255),
#     score varchar(255),
#     rank varchar(255),
#     locakImagePath varchar(255),
#     primary key(id)
# )