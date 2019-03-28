from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

class taobao(object):
    def __init__(self):
        self.driver=webdriver.Chrome('/home/lsj/下载/chromedriver')

    def get_url(self,url):
        self.driver.get(url)
        self.driver.find_element_by_xpath('//i[@class="iconfont static"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@class="login-text J_UserName"]').send_keys('13055045423')
        self.driver.find_element_by_xpath('//input[@class="login-text"]').send_keys('19951219a')
        time.sleep(2)
        #self.driver.find_element_by_xpath('//button[@id="J_eSubmitStatic"]').click()
        a=self.driver.find_element_by_xpath('//span[@id="nc_1_n1z"]')
        e=self.driver.find_element_by_xpath('//span[@class="nc-lang-cnt"]')
        action = ActionChains(self.driver)
        time.sleep(5)
        action.drag_and_drop_by_offset(a,258,0)
        # action.reset_actions()
        # action.move_to_element(a)
        # action.move_by_offset(1094,423).click()
        action.perform()
        # c=a.location
        # b=a.size
        # print(c)
        # print(b)
        # f=e.location
        # g =e.size
        # print(f)
        # print(g)
        # #x:1094 y:423




if __name__ == '__main__':
    url='https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm%3Fspm%3Da21bo.2017.754894437.3.5af911d96zONFh%26ad_id%3D%26am_id%3D%26cm_id%3D%26pm_id%3D1501036000a02c5c3739%26nekot%3DdGIzMTE3MzY4Mg%3D%3D1552459425613'
    obj=taobao()
    obj.get_url(url)