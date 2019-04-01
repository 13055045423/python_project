#代理池
from crawlproxy import CrawlProxy
from ckeckip import CheckIp
from multiprocessing import Process

class Scheduler(object):

    def __init__(self):
        pass

    def run_crawl_proxy(self):
        req_url = 'http://api3.xiguadaili.com/ip/?tid=558375694420659&num=10&delay=5&category=2&protocol=https&filter=on'
        crawl_proxy = CrawlProxy(req_url=req_url)
        for _ in range(2):
            crawl_proxy.crawl_proxy_data()

    def run_check_proxy(self):
        check_proxy = CheckIp(
            test_url='https://www.qichacha.com/',
            req_header={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            },
        )
        check_proxy.run()

    def run(self):
        #创建一个进程执行代理爬取
        process1 = Process(target=self.run_crawl_proxy)
        process1.start()
        #创建一个进程进行代理检测
        process2 = Process(target=self.run_check_proxy)
        process2.start()

        process1.join()
        process2.join()

if __name__ == '__main__':

    scheduler = Scheduler()
    scheduler.run()
        

    
