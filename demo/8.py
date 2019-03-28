from urllib import request
import random
USER_AGENT=[
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
]

url = 'http://www.baidu.com'

req_header={
    'User-Agent':random.choice(USER_AGENT)
}

req=request.Request(url,headers=req_header)
response=request.urlopen(req)

req_header1={
    'User-Agent':random.choice(USER_AGENT)
}

print(response.status)
print(response.read().decode('utf-8'))
print(response.getheaders())
print(response.getheader('Server'))
print(response.reason)
print(response.url)