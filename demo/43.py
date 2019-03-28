from selenium import webdriver
import time

class denglu(object):
    def __init__(self):
        self.driver=webdriver.Chrome('/home/lsj/下载/chromedriver')
    def get_url(self,url):
        self.driver.get(url)
        time.sleep(3)
        iframe=self.driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath('//input[@class="j-inputtext dlemail"]').send_keys('liu1402051690')
        time.sleep(1)
        self.driver.find_element_by_xpath('//input[@class="j-inputtext dlpwd"]').send_keys('19951219a')
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[@id="dologin"]').click()
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    url='https://mail.126.com/'
    obj=denglu()
    obj.get_url(url)

# https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh#en/zh/python POST from=en&to=zh&query=python&transtype=translang&simple_means_flag=3&sign=477811.239938&token=f64b918979fd022f25f894988cbc2d18
# https://api.weibo.cn/2/statuses/show?gsid=_2A25xjIW7DeRxGeNI61UV8S7JyzWIHXVQG55zrDV6PUJbkdAKLXTlkWpNSLm2dm_KHElwriTkkS0CJgrmYugez8ib&sensors_mark=0&wm=3333_2001&i=6fe2e73&sensors_is_first_day=false&from=1092093010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=9acadddd&v_f=1&sensors_device_id=18444D84-882F-4E2B-AF48-0C8F1C91E339&lang=zh_CN&sflag=1&ua=iPhone9,3__weibo__9.2.0__iphone__os12.1.4&ft=0&aid=01AsFvQ4k1C_ZBYAbo0QebWu6_IrRH6KvskgfJ-udgD15n8EM.&id=4349064592172818&mid=4349737019053789&_status_id=4349064592172818&luicode=10000001&featurecode=10000001&uicode=10000002&rid=25_0_8_4727408887121495684_0_0_0&fromlog=100015607410509&isGetLongText=1&has_member=1&lfid=100015607410509&moduleID=feed