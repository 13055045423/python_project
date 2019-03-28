# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tagname = scrapy.Field()
    firsturl = scrapy.Field()

class DangdangprojectactileItem(scrapy.Item):
    book_urls=scrapy.Field()
    next_urls=scrapy.Field()

class DangdangprojectContentItem(scrapy.Item):
    book_urls=scrapy.Field()
    next_urls=scrapy.Field()

class DangdangprojectcontentItem(scrapy.Item):

    title=scrapy.Field()
    coverImage=scrapy.Field()
    content=scrapy.Field()
    author=scrapy.Field()
    biming=scrapy.Field()
    chuping=scrapy.Field()
    publish_company=scrapy.Field()
    publist_time=scrapy.Field()
    commentnum=scrapy.Field()
    now_price=scrapy.Field()
    d_price=scrapy.Field()
    hotnum=scrapy.Field()
    locakImagePath=scrapy.Field()

# CREATE TABLE Persons
# (
# id int,
# title varchar(255),
# coverImage varchar(255),
# content varchar(255),
# author varchar(255),
# biming varchar(255),
# chuping varchar(255),
# publish_company varchar(255),
# publist_time varchar(255),
# commentnum varchar(255),
# now_price varchar(255),
# d_price varchar(255),
# primary key(id)
# );


