# import requests
# from lxml.html import etree
# def zhiwang(url):
#     html=request_data(url)
#     #print(html)
#     lxml_data=etree.HTML(html)
#     tr_list=lxml_data.xpath('//table[@class="GridTableContent"]/tbody//tr')[2:]
#     print(tr_list)
#     for tr in tr_list:
#         a_href=tr.xpath('./td[2]/a/@href').extract_first('')
#         print(a_href)
#
#
#
#
#
# def request_data(url):
#     req_header={
#         'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
#         'Cookie':'Ecp_ClientId=4190311195802360101; ASP.NET_SessionId=qghvpa5s0mdjhehdvha0bgcg; SID_kns=123119; SID_klogin=125141; SID_crrs=125132; KNS_SortType=; RsPerPage=20; SID_krsnew=125132; cnkiUserKey=3811ea06-76e6-ba0a-5f7c-a78e14162862; SID_kinfo=125105; Ecp_IpLoginFail=190311218.98.33.180; _pk_ref=%5B%22%22%2C%22%22%2C1552315340%2C%22http%3A%2F%2Fwww.cnki.net%2F%22%5D; _pk_ses=*; c_m_LinID=LinID=WEEvREcwSlJHSldTTEYzU3EydDRPQVBSVlIrcUgrWkpKeFIyME41ZkZtRT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=03/11/2019 23:11:02; LID=WEEvREcwSlJHSldTTEYzU3EydDRPQVBSVlIrcUgrWkpKeFIyME41ZkZtRT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; c_m_expire=2019-03-11 23:11:02; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"1402051690@qq.com","ShowName":"1402051690%40qq.com","UserType":"jf","r":"zHiWE3"}',
#         'Referer':'http://www.cnki.net/'
#     }
#     response=requests.post(url=full_url,headers=req_header)
#     if response.status_code==200:
#         print(response.status_code)
#         #print(response.text)
#         return response.text
#
#
# if __name__ == '__main__':
#     full_url = 'http://kns.cnki.net/kns/brief/brief.aspx?pagename=ASP.brief_default_result_aspx&isinEn=1&dbPrefix=SCDB&dbCatalog=%e4%b8%ad%e5%9b%bd%e5%ad%a6%e6%9c%af%e6%96%87%e7%8c%ae%e7%bd%91%e7%bb%9c%e5%87%ba%e7%89%88%e6%80%bb%e5%ba%93&ConfigFile=SCDBINDEX.xml&research=off&t=1552354125974&keyValue=%E7%A7%91%E6%8A%80&S=1&sorttype='
#
#     zhiwang(full_url)

from selenium import webdriver
import time, requests, json
from lxml.html import etree

dirver = webdriver.Chrome('/home/lsj/下载/chromedriver')
dirver.get('http://www.cnki.net/')
time.sleep(1)
dirver.find_element_by_xpath('//input[@class="search-input"]').send_keys('科技')
# time.sleep(1)
dirver.find_element_by_xpath('//input[@class="search-btn"]').click()
time.sleep(10)
dirver.switch_to.frame('iframeResult')
response=etree.HTML(dirver.page_source)
print(response)
#print(type(response))
li_list=response.xpath('//table[@class="GridTableContent"]/tbody//tr')[2:]
html = dirver.page_source
#print(html)
element = etree.HTML(html)
tr_list = element.xpath('//table[@class="GridTableContent"]/tbody//tr')[2:]
for tr in tr_list:
    a_href = tr.xpath('./td[2]/a/@href')[0]
    print(a_href)

dirver.close()


