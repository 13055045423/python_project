from urllib import request
import ssl

url = 'https://www.baidu.com/'
response=request.urlopen(url,timeout=10,context=ssl._create_unverified_context())

req_header={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

req = request.Request(url,headers=req_header)
response=request.urlopen(req)

print(response.status)
print(response.read().decode('utf-8'))
print(response.getheaders())
print(response.getheader('Server'))
print(response.reason)
print(response.url)
