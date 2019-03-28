import requests
import re
import json
from lxml import etree

class jiayuanspider(object):
    def __init__(self):
        self.start_urls=['http://date.jiayuan.com/eventslist_new.php?page=1&city_id=31&shop_id=15',
                         'http://date.jiayuan.com/eventslist_new.php?page=1&city_id=4201&shop_id=33',]

    def start_requests(self):
        for url in self.start_urls:
            response = self.download_data(url)
            self.parse(response)

    def download_data(self,req_url,parmas=None):
        req_header = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Cookie':'_gscu_1380850711=45703117ccjv7066; accessID=20190223184821263346; SESSION_HASH=40ae332e3170000f007a3630b07e16bf61dda754; jy_refer=www.baidu.com; FROM_BD_WD=%25E4%25B8%2596%25E7%25BA%25AA%25E4%25BD%25B3%25E7%25BC%2598; FROM_ST_ID=1764229; FROM_ST=.jiayuan.com; user_access=1; _gscbrs_1380850711=1; PHPSESSID=05f68462cecbd7d27178c2fd85b2425e; plat=date_pc; _gscs_1380850711=51685336d60cqv83|pv:3; DATE_SHOW_LOC=3301; DATE_SHOW_SHOP=40; uv_flag=124.205.158.242',
            'Referer':'http://date.jiayuan.com/eventslist.php'
        }
        response =requests.get(req_url,headers=req_header,params=parmas)

        if response.status_code==200:
            print(response.url)
            return response
    def parse(self,response):
        html_element = etree.HTML(response.text)
        hot_active = html_element.xpath('//div[@class="hot_detail fn-clear"]')
        for hot_div in hot_active:
            pass