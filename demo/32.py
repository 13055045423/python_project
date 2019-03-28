import queue
import requests
import threading
from lxml.html import etree
import json
#maxsize:指定队列中能够存储的最大数据量
# dataqueue = queue.Queue(maxsize=40)
# for i in range(0,50):
#     if not dataqueue.full():
#         dataqueue.put(i)
#
# #判断队列是否为空
# isempty = dataqueue.empty()
# print(isempty)
# #判断队列是否存满了
# isfull = dataqueue.full()
# print(isfull)
# #n发挥队列的大小
# size = dataqueue.qsize()
# print(size)
# #fifo(先进先出)
# print(dataqueue.get())
# #注意队列是线程之间常用的数据交换形式,以为队列在线程间,是线程安全的
def download_page_data(taskqueue,dataqueue):
    """
    执行下载任务
    :param taskqueue:
    :param dataqueue:
    :return:
    """
    while not taskqueue.empty():
        page = taskqueue.get()
        print('正在下载第'+str(page)+'页',threading.currentThread().name)
        full_url = 'http://blog.jobbole.com/all-posts/page/%s/'%str(page)
        print(full_url)
        req_header = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        response = requests.get(full_url,headers=req_header)
        if response.status_code==200:
            dataqueue.put(response.text)
        else:
            taskqueue.put(page)
def parse_data(dataqueue,lock):
    """
    解析数据,从dataqueue中取出数据进行解析
    :param dataqueue:
    :param lock:
    :return:
    """
    while not dataqueue.empty():
        print('正在解析数据',threading.currentThread().name)
        html= dataqueue.get()
        html_element = etree.HTML(html)
        articles = html_element.xpath('//div[@class="post floated-thumb"]')
        for article in articles:
            articleinfo = {}
            articleinfo['title']=article.xpath('.//[@class="class="archive-title"]/text()')[0]
            img_element = article.xpath('.//div[@class="post-thumb"]/a/img')
            if len(img_element)>0:
                articleinfo['coverimage']=img_element[0].xpath('./@src')[0]
            else:
                articleinfo['coverimage']="暂无照片"
            p_as =article.xpath('.//div[@class="post-meta"]/p[1]//a')
            if len(p_as)>2:
                articleinfo['tag']=p_as[1].xpath('./text()')[0]
                articleinfo['commentnum']=p_as[2].xpath('./text()')[0]
            else:
                articleinfo['tag']=p_as[1].xpath('./text()')[0]
                articleinfo['commentnum']='0'

            articleinfo['content']=article.xpath('.//span[@class="excerpt"]/p/text()')[0]
            articleinfo['publishtime']=''.join(article.xpath('.//div[@class="excerpt"]/p[1]/text()')).replace('\n','').replace(' ','').replace('\r','').replace('.','')
            print(articleinfo)

if __name__ == '__main__':
    taskqueue = queue.Queue()
    for i in range(1,201):
        taskqueue.put(i)

    dataqueue=queue.Queue()
    threadname = ['下载线程１号','下载线程２号','下载线程３号','下载线程４号']
    crawl_thread=[]
    for name in threadname:
        thread_crawl = threading.Thread(
            target=download_page_data,
            name=name,
            args=(taskqueue,dataqueue)
        )
        crawl_thread.append(thread_crawl)
        thread_crawl.start()
    for thread in crawl_thread:
        thread.join()

    lock = threading.Lock()
    threadname=['解析线程1号','解析线程2号','解析线程3号','解析线程4号']
    parse_thread = []
    for name in threadname:
        thread_parse = threading.Thread(
            target=parse_data,
            name=name,
            args=(dataqueue,lock)
        )
        thread_parse.start()
    for thread in parse_thread:
        thread.join()

    print('结束了')
