class useragentdownloadmiddlerware(object):
    def process_request(self,request,spider):
        import random
        from fake_useragent import UserAgent
        useragent=UserAgent()
        ua=useragent.random
        if ua:
            print('User-Agent设置成功')
            request.headers['User-Agent']=ua

class proxydownloadmiddermare(object):
    def process_request(self,request,spider):
        proxies=spider.settings['PROXIES']
        import random
        proxies_rm=random.choice(proxies)
        if proxies_rm['pwd']:
            import base64
            base64_pwd=base64.b64encode(proxies_rm['pwd'].encode('utf-8')).decode('utf-8')
            request.headers['Proxy-Authorization']='Basic '+base64_pwd
            request.meta['proxy']=proxies_rm['ip']
        else:
            request.meta['proxy']=proxies_rm['ip']

class cookiesdownloadmidderware(object):
    def process_request(self,request,spider):
        cookies=spider.setting('COOKIES')
        import random
        cookies_rm=random.choice(cookies)
        if cookies_rm:
            request.cookies=cookies_rm

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse
class seleniumdownloadmidderwre(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='')
        self.driver.set_page_load_timeout(10)

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.closed,signal=signals.spider_closed)
        return s

    def process_request(self,request,spider):
        if spider.name == "test":
            url=request.url
            if url:
                try:
                    spider.driver.get(url)
                    pagesource=spider.driver.page_source
                except TimeoutException as err:
                    print('请求超时',url)
                    return HtmlResponse(url=url,status=408,body=b'',request=request)

    def spider_closed(self, spider):
        import time
        time.sleep(5)
        spider.driver.close()

import pymysql
class ciachufangpipeline(object):
    def __init__(self,host,port,user,pwd,db,charset):
        self.client=pymysql.Connect(host,user,pwd,db,port,charset)
        self.cursor=self.client.cursor()
    @classmethod
    def from_crawler(cls,crawler):
        host=crawler.setting['']
        port=crawler.setting['']
        user=crawler.setting['']
        pwd=crawler.setting['']
        db=crawler.setting['']
        charset=crawler.setting['']
        return cls(host,port,user,pwd,db,charset)
    def process_item(self,item,spider):
        sql,data=item.insert_data_to_db(dict(item))
        try:
            self.cursor.execute(sql,data)
            self.client.commit()
        except Exception as err:
            print(err)
            self.client.rollback()

        return item

    def close_spider(self):
        self.cursor.close()
        self.client.close()

MYSQL_HOST='127.0.0.1'
MYSQL_PORT=3306
MYSQL_USER='1402051690'
MYSQL_PWD='19951028a'
MYSQL_DB='haha'
MYSQL_CHARSET='utf8'

#MYSQL异步存储
from twisted.enterprise import adbapi
class chinaprojectpipeline(object):
    def __init__(self,dbpool):
        self.dbpool=dbpool

    @classmethod
    def from_crawler(cls,crawler):
        db_parmars = {
            'host':crawler.setting['MYSQL_HOST'],
            'port':crawler.setting['MYSQL_PORT'],
            'user':crawler.setting['MYSQL_USER'],
            'pwd':crawler.setting['MYSQL_PWD'],
            'db':crawler.setting['MYSQL_DB'],
            'charset':crawler.setting['MYSQL_CHARSET'],
        }
    def process_item(self,item,spider):
        query=self.dbpool.runInteraction(
            self.insert_data_to_mysql,
            item
        )
        query.addErrback(
            self.insert_err,
            item
        )
        return item

    def insert_data_to_mysql(self,cursor,item):
        data_dict=dict(item)
        sql,data=item.get_insert_sql_data(data_dict)
        cursor.execute(sql,data)

    def insert_err(self,failure,item):
        print(failure,'插入失败',item)

https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false/ POST first=true&pn=1&kd=c++

https://music.163.com/weapi/cdns?csrf_token= POST params=TEZESs0vHiIPXEZFNf0CopfjDeE/FML0SdkCR+ngznmEkGVxry2P31M/KX67wEls&encSecKey=c10e4b6ce39bc3ec310f9f5c89534ab9c8a9b7d34f9f7aafec957345f439547df83ff5fdb242eba9db276416bb4a45ce7528f3515bab5d07b49a112e7de5062e817b58aaea1267f5a0852bddfc536a3d26c864547b5bd27405ff79a91637bae0ccdd6d2169b65d8672f2f979ec6e58d5bb672dc3e19c82816c4cf56c8f2186ea




