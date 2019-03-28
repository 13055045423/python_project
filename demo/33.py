from concurrent.futures import ThreadPoolExecutor
import requests
from lxml.html import etree
import threading
def down_load_data(page):
    print(page)
    print('正在下载第' + str(page) + '页', threading.currentThread().name)
    full_url = 'http://blog.jobbole.com/all-posts/page/%s/' % str(page)
    req_header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    response = requests.get(full_url, headers=req_header)

    if response.status_code == 200:
        # 将获取到的页面源码存到dataQueue队列中
        print('请求成功')
        return response.text,response.status_code

def download_done(futures):
    print(futures.result())
    #可以在这里做数据的解析
    html = futures.result()[0]
    html_element = etree.HTML(html)
    articles = html_element.xpath('//div[@class="post floated-thumb"]')
    for article in articles:
        articleInfo = {}
        # 标题
        articleInfo['title'] = article.xpath('.//a[@class="archive-title"]/text()')[0]
        # 封面
        img_element = article.xpath('.//div[@class="post-thumb"]/a/img')
        if len(img_element) > 0:
            articleInfo['coverImage'] = img_element[0].xpath('./@src')[0]
        else:
            articleInfo['coverImage'] = '暂无图片'
        p_as = article.xpath('.//div[@class="post-meta"]/p[1]//a')
        if len(p_as) > 2:
            # tag类型
            articleInfo['tag'] = p_as[1].xpath('./text()')[0]
            # 评论量
            articleInfo['commentNum'] = p_as[2].xpath('./text()')[0]
        else:
            # tag类型
            articleInfo['tag'] = p_as[1].xpath('./text()')[0]
            # 评论量
            articleInfo['commentNum'] = '0'
        # 简介
        articleInfo['content'] = article.xpath('.//span[@class="excerpt"]/p/text()')[0]
        # 时间
        articleInfo['publishTime'] = ''.join(article.xpath('.//div[@class="post-meta"]/p[1]/text()')).replace('\n',
                                                                                                              '').replace(
            ' ', '').replace('\r', '').replace('·', '')
        print(articleInfo)
if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=10)
    for i in range(1,201):
        handler = pool.submit(down_load_data,i)
        #设置回调方法
        handler.add_done_callback(download_done)
    #执行shutdown()实质是执行了join()方法
    pool.shutdown()
