from selenium import webdriver
import time
from selenium.common import exceptions

class douyuspider(object):
    def __init__(self):
        self.dirver = webdriver.Chrome(executable_path='/home/lsj/下载/chromedriver')

    def download_page_data(self,url):
        """
        根据起始url加载页面
        :param url:
        :return:
        """
        self.dirver.get(url)
        time.sleep(1)
        self.parse_page_data()
    def parse_page_data(self):
        """
        根据加载出来的页面进行数据解析
        :return:
        """
        self.dirver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        video_lis = self.dirver.find_element_by_xpath('//ul[@id="live-list-contentbox"]/li')
        for li in video_lis:
            videoInfo = {}
            videoInfo['coverImage']=li.find_element_by_xpath('.//img[@class="JS_listthumb"]').get_attribute('src')
            videoInfo['title']=li.find_element_by_xpath('.//h3[@class="ellipsis"]').text
            videoInfo['type']=li.find_element_by_xpath('.//span[@class="tag ellipsis"]').text
            videoInfo['author']=li.find_element_by_xpath('.//span[@class="dy-name ellipsis fl"]').text
            videoInfo['watchnum']=li.find_element_by_xpath('.//span[@class="dy-num fr"]').text
            print(videoInfo)
        try:
            a = self.dirver.find_element_by_xpath('//a[@class="shark-pager-next"]')
            a.click()
            time.sleep(2)
            self.parse_page_data()
        except exceptions.NoSuchElementException as err:
            print('没有下一页了')
            self.dirver.quit()

if __name__ == '__main__':
    spider = douyuspider()
    spider.download_page_data('https://www.douyu.com/directory/all')
