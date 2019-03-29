
from urllib import request
import re,os

def zuowenSpider():
    # 构建请求头
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    req_url = 'https://www.99zuowen.com/xiaoxuezuowen/ynjzuowen/'
    print('正在请求' + req_url)
    # 构建request对象
    req = request.Request(req_url, headers=req_headers)
    # 发起请求
    response = request.urlopen(req)
    if response.status == 200:

        #获取页面源码
        html = response.read().decode('utf-8')

        #获取每个分类的链接
        pattern = re.compile('<div\sclass="xbt">.*?<span.*?>.*?<a.*?href="(.*?)".*?>.*?<h3>(.*?)</h3>',re.S)
        classifys = re.findall(pattern,html)
        print(classifys)

        for classify in classifys:

            dirpath = '99作文/'+classify[1]
            if not os.path.exists(dirpath):
                os.mkdir(dirpath)

            req_url = classify[0]
            if 'https://www.99zuowen.com' not in req_url:
                req_url = 'https://www.99zuowen.com' + req_url

            get_zuowen_article_list(req_url,dirpath)

def get_zuowen_article_list(req_url,dirpath):
    """
    req_url:每一个分类的分页页面的url地址
    dirpath:作文要存储的文件路径
    """
    # 构建请求头
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    print('正在请求' + req_url)
    # 构建request对象
    req = request.Request(req_url, headers=req_headers)
    # 发起请求
    response = request.urlopen(req)

    if response.status == 200:
        #在列表中提取作文的详情地址和标题
        print('正在提取作文列表',dirpath,response.url)
        html = response.read().decode('utf-8')
        pattern = re.compile('<li\sclass="lis">.*?<a.*?href="(.*?)".*?>(.*?)</a>',re.S)
        zuowen_list = re.findall(pattern,html)
        print(zuowen_list)

        for zuowen in zuowen_list:
            print('正在获取'+zuowen[1])
            get_article_detail(zuowen[0],dirpath)

    # 构造下一页的url,并且发起请求??思考??自己实现
    # next_page_url=????
    # self.get_zuowen_article_list(next_page_url,dirpath)

def get_article_detail(req_url,dirpath):
    """
    req_url:作文详情url地址
    dirpath:作文要存储的文件路径
    """
    # 构建请求头
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    print('正在请求' + req_url)
    # 构建request对象
    req = request.Request(req_url, headers=req_headers)
    # 发起请求
    response = request.urlopen(req)
    if response.status == 200:
        # print(response.read().decode('utf-8'))
        html = response.read().decode('utf-8')
        #空字典，一会存放提取的作文数据
        zuowen_dict = {}
        #提取作文详情中的作文数据
        pattern1 = re.compile(
            '<div.*?class="title">.*?<h1>(.*?)</h1>'+
            '.*?<div.*?>.*?<span>来源:.*?<a.*?>(.*?)</a>'+
            '.*?<span>(.*?)</span>'+
            '.*?<span>(.*?)</span>'
            ,re.S
        )
        info = re.findall(pattern1,html)[0]
        zuowen_dict['标题'] = info[0]
        zuowen_dict['来源'] = info[1]
        zuowen_dict['作者'] = info[2]
        zuowen_dict['发布时间'] = info[3]

        pattern2 = re.compile('<div\sclass="content">.*?<div\sclass="article_page">',re.S)
        div_content = re.findall(pattern2,html)[0]

        pattern3 = re.compile('<p>(.*?)</p>',re.S)
        content = ';'.join(re.findall(pattern3,div_content))
        zuowen_dict['内容'] = content

        print(zuowen_dict)

        write_data_to_file(zuowen_dict,dirpath)


def write_data_to_file(zuowen_dict,dirpath):
    filename = dirpath + '/' + zuowen_dict['标题']

    with open(filename, 'w') as file:
        file.write(
            '标题：' + zuowen_dict['标题'] + '\n' +
            '来源:' + zuowen_dict['来源'] + '\n' +
            zuowen_dict['作者'] + '\n' +
            '发布时间：' + zuowen_dict['发布时间'] + '\n' +
            zuowen_dict['内容']
        )

if __name__ == '__main__':
    zuowenSpider()

