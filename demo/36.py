from selenium import webdriver
import time
diver = webdriver.Chrome(executable_path='/home/lsj/下载/chromedriver')
diver.get('https://passport.douyu.com/member/login')
time.sleep(1)
diver.find_element_by_xpath('//span[@class="scancide-to js-to-link js-need-param fr"]').click()
diver.find_element_by_xpath('//input[@class="fr ipt ipt-need-parent country-phonenum"]').send_keys('18518753265')
diver.find_element_by_xpath('//input[@class="ipt showpw1 notsub"]').send_keys('ljh12345678')
time.sleep(3)
diver.find_element_by_xpath('//input[@class="loginbox-sbt btn-sub"]').click()
time.sleep(2)
dive_image = diver.find_element_by_xpath('//div[@class="geetest_panel_box"]')
location =dive_image.location
size = dive_image.size
print(dive_image.location)
print(dive_image.size)
top,bottom,right,left = location['y']+2,location['y']+size['height']-42,location['x']-4,location['x']-size['width']

#获取屏幕截图
from PIL import Image
from io import BytesIO
screen_image = diver.get_screenshot_as_png()
screen_image = Image.open(BytesIO(screen_image))

caption_image = screen_image.crop((left,top,right,bottom))
caption_image.save('caption_image.png')