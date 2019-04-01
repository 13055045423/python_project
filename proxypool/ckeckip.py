#　检测模块：定时从存储模块获取所有代理，并且对代理进行检测,
# 根据代理的检测结果做不同的处理

import requests
from requests.exceptions import ProxyError,ConnectionError,SSLError,ReadTimeout,ConnectTimeout
import manageip
import queue,time

class CheckIp(object):

    def __init__(self,test_url='https://www.baidu.com/',timeout=5,req_header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0'}):
        #要检测的url,用来判断ip是否可用
        self.test_url = test_url
        #设置请求的超时时间，如果超时则认为代理不可用
        self.timeout = timeout
        #设置请求头
        self.headers = req_header
        #创建一个ip管理器
        self.managerIp = manageip.ManageIp(database='proxydb',col_name='proxycol')
        #创建一个队列存放需要检测的ip
        self.ipqueue = queue.Queue()


    def check_proxy_with_proxies(self,proxies):
        """
        目前暂时没有用到
        :param proxies: 代理列表,检测代理是否可用，可用则加入数据库
        :return:
        """
        from concurrent.futures import ThreadPoolExecutor

        if proxies and len(proxies) > 0 :

            pool = ThreadPoolExecutor(10)

            for proxy in proxies:
                proxy_dict = {
                    'type':'https',
                    'proxy':proxy
                }
                handler = pool.submit(self.check_proxy_isused,proxy_dict)
                handler.add_done_callback(self.checkDone)

            pool.shutdown()


    def check_proxy_isused(self,proxy_dict):
        '''
        检测代理是否可用
        '''
        #记录检测代理的起始时间
        start_time = time.time()
        try:
            proxies = {
                'https': proxy_dict['proxy'],
            }
            print('正在检测：', proxies)
            response = requests.get(self.test_url, timeout=self.timeout, proxies=proxies)
            print('111',response.status_code,response.url)
            end_time = time.time()
            used_time = end_time - start_time
            if response.status_code == requests.codes.ok:
                print('(代理可用)Proxy Valid'+proxy_dict['proxy'], 'Used Time:', used_time)
                return True, used_time,proxy_dict
            else:
                print('(不代理可用)Proxy Valid' + proxy_dict['proxy'], 'Used Time:', used_time)
                return False, used_time, proxy_dict
        #出现异常则代理不可用
        except (ProxyError, ConnectTimeout, SSLError, ReadTimeout, ConnectionError):
            end_time = time.time()
            used_time = end_time - start_time
            print('(代理不可用)Proxy Invalid:', proxy_dict['proxy'],'Used Time:', used_time)
            return False,used_time,proxy_dict


    def checkDone(self,future):
        result = future
        # 检测代理是否可用，如果可用则存入,mongodb数据库
        status, usedtime , proxy_dict = future.result()
        if status == True:
            self.managerIp.save_proxydict(proxy_dict)

    def run(self):
        """
        检查ip是否可用
        { 'type':'https', 'proxy':proxy }
        """

        #外部不断从队列中取出代理检测，直到队列为空，重新获取
        #为了提高执行的效率，这里定义一个线程池，加快检测的速度
        print('正在执行检测代理模块')

        while True:
            if self.ipqueue.empty():
                proxies = self.managerIp.get_collection_proxies()
                for proxy_dict in proxies:
                    self.ipqueue.put(proxy_dict)
                print('获取需要检测的代理获取完毕', len(proxies))
            else:
                proxy_dict = self.ipqueue.get()
                if proxy_dict:
                    status, usedtime, proxy_dict = self.check_proxy_isused(proxy_dict)
                    if status == False:
                        self.managerIp.delete_proxy(proxy_dict)

if __name__ == '__main__':

    check_proxy = CheckIp(test_url='https://www.baidu.com/')
    check_proxy.run()


