from selenium import webdriver
import time
from io import BytesIO
from PIL import Image
from chaojiying import Chaojiying_Client
from selenium.webdriver import ActionChains
dirver = webdriver.Chrome('/home/lsj/下载/chromedriver')
dirver.get('https://passport.douyu.com/member/login?lang=cn&type=login&client_id=1')
dirver.find_element_by_xpath('//span[@class="scancide-to js-to-link js-need-param fr"]').click()
dirver.find_element_by_name('phoneNum').send_keys('18518753265')
dirver.find_element_by_name('password').send_keys('ljh12345678')
time.sleep(1)
dirver.find_element_by_xpath('//input[@class="loginbox-sbt btn-sub"]').click()
time.sleep(4)

image_element_div = dirver.find_element_by_xpath('//div[@class="geetest_widget geetest_medium_fontsize"]')
location = image_element_div.location
size=image_element_div.size
print(location)
print(size)

top,bottom,left,right = location['y']+2,location['y']+size['height']-42,location['x']-size['width']-2,location['x']-4
print(top,bottom,left,right)
screen_image = dirver.get_screenshot_as_png()
screen_image = Image.open(BytesIO(screen_image))
captcha = screen_image.crop((left,top,right,bottom))


captcha.save('image.png')
