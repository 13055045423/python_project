#使用requests模块设置代理
import requests
proxies={
    'http':'219.238.186.188:8118',
    'https':'222.76.204.110:808',
    'https':'https://username:password@ip:port',
    'http':'http://username:password@ip:port'
}
url='https://httpbin.org/get'
response=requests.get(url,proxies=proxies,timeout=10)
print(response.text)