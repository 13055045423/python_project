from selenium import webdriver
import time
dirver = webdriver.Chrome('/home/lsj/下载/chromedriver')
dirver.get('https://lol.qq.com/')
time.sleep(1)
dirver.find_element_by_xpath('//p[@class="unlogin"]/a').click()
time.sleep(1)
dirver.switch_to.frame('loginIframe')
dirver.find_element_by_id('switcher_plogin').click()

dirver.find_element_by_xpath('//input[@id="u"]').send_keys('1970008493')
dirver.find_element_by_xpath('//input[@id="p"]').send_keys('19971127ljk')

dirver.find_element_by_xpath('//input[@id="login_button"]').click()

cookies = {cookie['name']:cookie['value'] for cookie in dirver.get_cookie()}
print(cookies)