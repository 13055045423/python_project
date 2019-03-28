from selenium import webdriver
import time
import requests
from io import BytesIO
from PIL import Image
from chaojiying import Chaojiying_Client
from selenium.webdriver import ActionChains
driver=webdriver.Chrome(executable_path='/home/lsj/下载/chromedriver')
driver.get('https://passport.douyu.com/member/login?lang=cn&type=login&client_id=1')
driver.find_element_by_xpath('//span[@https://passport.douyu.com/member/login?lang=cn&type=login&client_id=1]').click()
driver.find_element_by_name('')