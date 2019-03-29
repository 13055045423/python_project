import queue
import requests
import threading
from lxml.html import etree
import json

# #maxsize:指定队列中能够存储的最大的数据量
# dataqueue = queue.Queue(maxsize=40)
#
# for i in range(0,50):
#     if not dataqueue.full():
#         dataqueue.put(i)
#
# #判断队列是否为空
# isempty = dataqueue.empty()
# print(isempty)
#
# #判断队列是否存满了
# isfull = dataqueue.full()
# print(isfull)
#
# #n发挥对列的大小
# size = dataqueue.qsize()
# print(size)
#
# #FIFO(先进的先出)
# print(dataqueue.get())

#注意：队列是线程之间常用的数据交换形式,因为队列在线程间,是线程安全的
"""
1.创建一个任务队列：存放的是带爬取的url地址
2.创建爬取线程,执行任务的下载
3.创建数据队列:存放爬取线程获取的页面源码
4.创建解析线程:解析html源码,提取目标数据,数据持久化
"""
#获取jobbole的文章列表
#http://blog.jobbole.com/all-posts/page/1/
#http://blog.jobbole.com/all-posts/page/2/
#http://blog.jobbole.com/all-posts/page/3/

def download_page_data(taskQueue,dataQueue):
    """
    执行下载任务
    :param taskQueue: 从任务队列里面取出任务
    :param dataQueue: 将获取到的页面源码存到dataQueue队列中
    :return:
    """
    while not taskQueue.empty():
        page = taskQueue.get()
        print('正在下载第'+str(page)+'页',threading.currentThread().name)
        full_url = 'http://blog.jobbole.com/all-posts/page/%s/' % str(page)
        req_header = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        response = requests.get(full_url,headers=req_header)

        if response.status_code == 200:
            #将获取到的页面源码存到dataQueue队列中
            dataQueue.put(response.text)
        else:
            taskQueue.put(page)


def parse_data(dataQueue,lock):
    """
    解析数据,从dataQueue中取出数据进行解析
    :param dataQueue:
    :return:
    """
    while not dataQueue.empty():
        print('正在解析', threading.currentThread().name)
        html = dataQueue.get()
        html_element = etree.HTML(html)
        articles = html_element.xpath('//div[@class="post floated-thumb"]')

        for article in articles:
            articleInfo = {}
            #标题
            articleInfo['title'] = article.xpath('.//a[@class="archive-title"]/text()')[0]
            #封面
            img_element = article.xpath('.//div[@class="post-thumb"]/a/img')
            if len(img_element) > 0:
                articleInfo['coverImage'] = img_element[0].xpath('./@src')[0]
            else:
                articleInfo['coverImage'] = '暂无图片'
            p_as = article.xpath('.//div[@class="post-meta"]/p[1]//a')
            if len(p_as) > 2:
                #tag类型
                articleInfo['tag'] = p_as[1].xpath('./text()')[0]
                #评论量
                articleInfo['commentNum'] = p_as[2].xpath('./text()')[0]
            else:
                # tag类型
                articleInfo['tag'] = p_as[1].xpath('./text()')[0]
                # 评论量
                articleInfo['commentNum'] = '0'
            #简介
            articleInfo['content'] = article.xpath('.//span[@class="excerpt"]/p/text()')[0]
            #时间
            articleInfo['publishTime'] = ''.join(article.xpath('.//div[@class="post-meta"]/p[1]/text()')).replace('\n','').replace(' ','').replace('\r','').replace('·','')

            lock.acquire() #加锁
            with open('jobbole.json','a+') as file:
                json_str = json.dumps(articleInfo,ensure_ascii=False) + '\n'
                file.write(json_str)
            lock.release() #解锁

if __name__ == '__main__':

    #创建任务队列
    taskQueue = queue.Queue()

    for i in range(1,201):
        taskQueue.put(i)

    #创建数据队列
    dataQueue = queue.Queue()

    #创建线程执行下载任务
    threadName = ['下载线程1号','下载线程2号','下载线程3号','下载线程4号']
    crawl_thread = []
    for name in threadName:
        #创建线程
        thread_crawl = threading.Thread(
            target=download_page_data,
            name=name,
            args=(taskQueue,dataQueue)
        )
        crawl_thread.append(thread_crawl)
        #开启线程
        thread_crawl.start()

    #让所有的爬取线程执行完毕,在回到主线程中继续执行
    for thread in crawl_thread:
        thread.join()

    #加线程锁
    lock = threading.Lock()
    #创建解析线程,从dataQueue队列中取出页面源码进行解析
    threadName = ['解析线程1号', '解析线程2号', '解析线程3号', '解析线程4号']
    parse_thread = []
    for name in threadName:
        # 创建线程
        thread_parse = threading.Thread(
            target=parse_data,
            name=name,
            args=(dataQueue,lock)
        )
        parse_thread.append(thread_crawl)
        # 开启线程
        thread_parse.start()

    for thread in parse_thread:
        thread.join()

    print('结束了')








