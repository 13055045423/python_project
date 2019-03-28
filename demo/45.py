import requests
from lxml.html import etree
from concurrent.futures import ThreadPoolExecutor

class guazi(object):
    def __init__(self,url):
        #print('初始化方法')
        self.url=url
        self.pool = ThreadPoolExecutor(10)

    def get_url(self,url):
        #print(url)
        req_header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Referer': 'https://www.guazi.com/bj/?scode=10103000312&ca_s=pz_baidu&ca_n=tbmkbturl',
            'Cookie':'uuid=d4b9684e-b386-49e9-c02d-7aefd00f1785; ganji_uuid=7238585730004897488497; d4b9684e-b386-49e9-c02d-7aefd00f1785_views=1; f243211d-d229-44e6-e742-0ec4d230a684_views=1; Hm_lvt_e6e64ec34653ff98b12aab73ad895002=1551189719; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1552631172; lg=1; financeCityDomain=anshan; jr_from=web_index_tc; jr_apply_platform=web; cityDomain=bj; user_city_id=12; antipas=8650pP7026471q76Z449h88; clueSourceCode=10103000312%2300; sessionid=4bf74148-42c4-4241-a8ab-c7138c471803; cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22ca_i%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22d4b9684e-b386-49e9-c02d-7aefd00f1785%22%2C%22sessionid%22%3A%224bf74148-42c4-4241-a8ab-c7138c471803%22%7D; GZ_TOKEN=096edcwJoht2JZ0ZYPJd%2FuEKlcTO9w%2B6FNROOqsxwIKrL8zEa5XtDKCweOHf%2FGO6nX%2BfooJ7EmBx1v4ELSBd7UCG0gOoSKBNUqL175fHsi1sTGpeTqRJ%2Bp9WRWnTiR7ju4XdNwGXfz%2BZayeizg; guaZiUserInfo=aMS2ncH0qpWB9vkmyTzta7; userid=702544767; preTime=%7B%22last%22%3A1552650789%2C%22this%22%3A1551189575%2C%22pre%22%3A1551189575%7D'
        }
        try:
            response=requests.get(url,headers=req_header)

            if response.status_code==200:
                #print(response.status_code,response.url)
                return response.content
            else:
                pass
        except Exception as err:
            #pass
            print(err)
            print('状态码不对')


    def get_a(self,html):

        lxml_html=etree.HTML(html)
        url=lxml_html.xpath('//div[@class="entry-buycar fl"]/div[@class="buycar-brand clearfix"]/a[1]/@href')[0]
        #print(url)
        new_url='https://www.guazi.com'+url
        list_html=self.get_url(new_url)
        # if list_html:
        #     res=self.pool.submit(self.get_url,new_url)
        #     res.add_done_callback(self.dazhong_list)
        self.dazhong_list(list_html)

    def dazhong_list(self,list_html):
        # if future.result():
        lxml_dazhong=etree.HTML(list_html)
        li_list=lxml_dazhong.xpath('//ul[@class="carlist clearfix js-top"]//li')
        url=[]
        # pool = ThreadPoolExecutor(10)
        for li in li_list:
            #print(li)
            name=li.xpath('./a/h2/text()')[0]
            ever_url=li.xpath('./a/@href')[0]
            #print(ever_url)
            xaingqing_url='https://www.guazi.com'+ever_url
            html=self.get_url(xaingqing_url)
            if html:
                url.append(xaingqing_url)
                # handler = pool.submit(self.get_url, xaingqing_url)
                # handler.add_done_callback(self.detail_data)
        # pool=ThreadPoolExecutor(4)
        for u in url:
            handler=self.pool.submit(self.get_url,u)
            handler.add_done_callback(self.detail_data)
        #pool.shutdown()

        next_url=lxml_dazhong.xpath('//ul[@class="pageLink clearfix"]/li[last()]/a[@class="next"]')
        #print(next_url)
        if next_url:
            new_url='https://www.guazi.com'+lxml_dazhong.xpath('//ul[@class="pageLink clearfix"]/li[last()]/a[@class="next"]/@href')[0]
            #print(next_url)

            detail_url=self.get_url(new_url)
            # if detail_url:
            #     #print('获取第二页')
            #     result=self.pool.submit(self.get_url,detail_url)
            #     result.add_done_callback(self.dazhong_list)
            self.dazhong_list(detail_url)
        #self.pool.shutdown()

    def detail_data(self,future):

        html_etree=etree.HTML(future.result())
        data={}
        if html_etree.xpath('//h2[@class="titlebox"]'):
            data['name']=html_etree.xpath('//h2[@class="titlebox"]/text()')[0].replace('\n','').replace(' ','').replace('\r','')
        else:
            data['name']='暂无数据'
        if html_etree.xpath('//h2[@class="titlebox"]/span[1]'):
            data['span1'] = html_etree.xpath('//h2[@class="titlebox"]/span[1]/text()')[0]
        else:
            data['span1']='暂无数据'
        if html_etree.xpath('//h2[@class="titlebox"]/span[2]'):
            data['span2'] = html_etree.xpath('//h2[@class="titlebox"]/span[2]/text()')[0]
        else:
            data['span2']='暂无数据'
        if html_etree.xpath('//h2[@class="titlebox"]/span[3]'):
            data['span3'] = html_etree.xpath('//h2[@class="titlebox"]/span[3]/text()')[0]
        else:
            data['span3']='暂无数据'
        if html_etree.xpath('//ul[@class="assort clearfix"]/li[1]/span'):
            data['name1'] = html_etree.xpath('//ul[@class="assort clearfix"]/li[1]/span/text()')[0]
        else:
            data['name1']='暂无数据'
        if html_etree.xpath('//ul[@class="assort clearfix"]/li[2]/span'):
            data['name2'] = html_etree.xpath('//ul[@class="assort clearfix"]/li[2]/span/text()')[0]
        else:
            data['name2']='暂无数据'
        if html_etree.xpath('//ul[@class="assort clearfix"]/li[3]/span'):
            data['name3'] = html_etree.xpath('//ul[@class="assort clearfix"]/li[3]/span/text()')[0]
        else:
            data['name3']='暂无数据'
        if html_etree.xpath('//ul[@class="assort clearfix"]/li[4]/span'):
            data['name4'] = html_etree.xpath('//ul[@class="assort clearfix"]/li[4]/span/text()')[0]
        else:
            data['name4']='暂无数据'
        if html_etree.xpath('//ul[@class="assort clearfix"]/li[5]/span'):
            data['name5'] = html_etree.xpath('//ul[@class="assort clearfix"]/li[5]/span/text()')[0]
        else:
            data['name5']='暂无数据'
        if html_etree.xpath('//div[@class="pricebox js-disprice"]/span[1]'):
            data['name6'] = html_etree.xpath('//div[@class="pricebox js-disprice"]/span[1]/text()')[0].replace(' ','')
        else:
            data['name6']='暂无数据'
        if html_etree.xpath('//div[@class="pricebox js-disprice"]/span[2]'):
            data['name7'] = html_etree.xpath('//div[@class="pricebox js-disprice"]/span[2]/text()')[0].replace('\n','').replace(' ','').replace('\r','')
        else:
            data['name7']='暂无数据'
        print(data)

if __name__ == '__main__':
    url='https://www.guazi.com/bj/?scode=10103000312&ca_s=pz_baidu&ca_n=tbmkbturl'
    obj=guazi(url)
    html=obj.get_url(url)
    obj.get_a(html)
