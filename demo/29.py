#pyquery语法规则类似于jquery,可以对hml文本进行解析
#pip3 install pyquery
"""
pq=pyquery(html文档)
pq(’css选择器‘)
items():获取到多个标签时，使用items()将pyquery转换为一个生成器
然后在使用for in 循环
filter('css选择器')：过滤
text():获取标签文本
attr('属性名')获取属性值
"""
from pyquery import PyQuery
import requests
def tencentjob(full_url):
    html=load_data(full_url)
    next_url = parse_page_data(html)
    if 'javascript:;' != next_url:
        next_url='https://hr.tencent.com/'+next_url
        tencentjob(next_url)
def load_data(url):
    """
    发起请求，获取职位列表页面源码
    :param url:
    :return:
    """
    req_header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    response = requests.get(url,headers=req_header)
    if response.status_code==200:
        return response.text
def parse_page_data(html):
    """
    解析页面源码数据
    :param html:
    :return:
    """
    #实例化一个pyquery对象
    html_pq = PyQuery(html)
    #提取职位信息
    tr_even = html_pq('tr').filter('.even')
    tr_odd= html_pq('tr').filter('.odd')
    tr_all = tr_even+tr_odd
    tr_all = tr_all.items()
    for tr in tr_all:
        jobinfo = {}
        jobinfo['title']=tr('td.l.square a').text()
        print(jobinfo['title'])
        detail_url = 'https://hr.tencent.com/'+tr('td.l.square a').attr('href')
        print(detail_url)
        #职位类型eq(1):获取之地那个索引的标签,索引值从0开始
        jobinfo['type']=tr('td').eq(1).text()
        #招聘人数
        jobinfo['needpeople']=tr('type').eq(2).text()
        #地点
        jobinfo['address']=tr('td').eq(3).text()
        #发布时间
        jobinfo['publishtime']=tr('td').eq(4).text()
        print(jobinfo)
        #工作详情内容
        html = load_data(detail_url)
        jobinfo['content']=parse_detail_data(html)

def parse_detail_data(html):
    """
    解析详情数据
    :param html:
    :return:
    """
    #实例化一个pyquery()对象
    html_pq=PyQuery(html)
    #提取详情内容所在的li标签
    lis = html_pq('ul.square li')
    content = []
    for li in lis.items():
        li_text = li.text()
        content.append(li_text)

    return ','.join(content)

if __name__ == '__main__':
    #设置起始偏移量
    offset=0
    full_url = 'https://hr.tencent.com/position.php?&start='+str(offset)
    tencentjob(full_url)


