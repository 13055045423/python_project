
from manageip import ManageIp
import time

manage_ip = ManageIp(database='proxydb',col_name='proxycol')

for i in range(400):
    print('随机获取代理为：', manage_ip.get_random_ip())
    time.sleep(1)