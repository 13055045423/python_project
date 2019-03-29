#　beautifulsoup:作用是从html/xml中提取数据,会载入整个HTML DOM,
# 比lxml解析器效率要低
# pip3 install beautifulsoup4

#以腾讯招聘数据提取为例

#https://hr.tencent.com/position.php (第一页url地址)
#https://hr.tencent.com/position.php?&start=10(第二页)
#https://hr.tencent.com/position.php?&start=20(第三页)
import requests
#使用BeautifulSoup,需要这么导入模块
from bs4 import BeautifulSoup

def tencentJob(full_url):
    html = loda_data(full_url)
    next_url = parse_page_data(html)
    if 'javascript:;' != next_url:
        next_url = 'https://hr.tencent.com/'+next_url
        tencentJob(next_url)

    #这种根据偏移量构建下一页的方式并不好
    #如果页面源码里面有下一页字样,可以提取该标签的href属性
    # #构建下一页的偏移量
    # next_offset = offset+10
    # #继续发起请求,解析数据
    # tencentJob(next_offset)

def loda_data(url):
    """
    发起请求,获取职位列表页页面源码
    :param url:
    :return:
    """
    req_header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    response = requests.get(url,headers=req_header)

    if response.status_code == 200:

        return response.text

def parse_page_data(html):
    """
    解析分页的页面源码数据
    :param html:
    :return:
    """
    """
    features=None：指明bs解析器
    lxml:使用lxml下的html解析器
    html.parser:是python自带的一个解析器模块
    """
    html_bs = BeautifulSoup(html,features='lxml')
    #找到职位列表
    # html_bs.find():查找一个节点
    # html_bs.find_all():查找所有符合条件的节点
    """
    name=None, 指定你要查找的标签名,可以是一个字符串,正则表达式,或者列表
    attrs={}, 根据属性的值查找标签（dict）{'属性名称':'属性的值'}
    text=None, 可以是一个字符串,正则表达式,查找符合条件的文本内容
    limit=None　限制返回的标签的个数
    find_all方法返回的吧标签都放在列表中
    """
    tr_even = html_bs.find_all(name='tr',attrs={'class':'even'})
    tr_odd = html_bs.find_all(name='tr',attrs={'class':'odd'})
    print(tr_odd)
    print(tr_even)

    for tr in tr_even+tr_odd:
        # print(tr)
        jobinfo = {}
        #职位的名称
        #.get_text()表示取标签的文本
        jobinfo['title'] = tr.select('td.l.square > a')[0].get_text()
        # #职位的类型
        # jobinfo['type'] = tr.select('td')[1].get_text()
        jobinfo['type'] = tr.select('td:nth-of-type(2)')[0].get_text()
        # #职位人数
        # jobinfo['peopleNum'] = tr.select('td:nth-child(3)')[0].get_text()
        jobinfo['peopleNum'] = tr.select('td')[2].get_text()
        # #地点
        # jobinfo['adress'] = tr.select('td:nth-child(4)')[0].get_text()
        jobinfo['adress'] = tr.select('td')[3].get_text()
        # #发布时间
        # jobinfo['publistTime'] = tr.select('td:nth-child(5)')[0].get_text()
        jobinfo['publistTime'] = tr.select('td')[4].get_text()
        # 职位详情地址
        #https://hr.tencent.com/position_detail.php?id=46553&keywords=&tid=0&lid=0
        detail_url = 'https://hr.tencent.com/' + tr.select('td.l.square > a')[0].attrs['href']
        #职位详情的html页面源码
        html = loda_data(detail_url)
        #获取职位的要求和描述
        jobinfo['content'] = parse_detail_data(html)
        #数据持久化
        # print(jobinfo)
        print(jobinfo, detail_url)

    #提取下一页的url链接
    next_url = html_bs.select('a#next')[0].attrs['href']
    return next_url


def parse_detail_data(html):
    #创建一个BeautifulSoup对象
    html_bs = BeautifulSoup(html,features='lxml')
    #使用css语法取出li标签
    content_li = html_bs.select('ul.squareli li')

    content = []
    #取出li标签的文本,放入列表中
    for li in content_li:
        li_text = li.get_text()
        content.append(li_text)

    return ','.join(content)





if __name__ == '__main__':
    #设置起始偏移量
    offset = 0
    full_url = 'https://hr.tencent.com/position.php?&start=' + str(offset)
    tencentJob(full_url)



