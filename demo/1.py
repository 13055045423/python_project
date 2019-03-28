from urllib import request
import ssl

#目标url
url = 'https://www.baidu.com/'
# request.urlopen()
# url, \
# data=None,
#
# timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
#
# *, cafile=None,\
#
# capath=None,\
#
# cadefault=False,\
#
# context=None
content=ssl._create_unverified_context()
response=request.urlopen(url,timeout=10,context=content)
code=response.status
print(code)
b_html=response.read()
res_headers=response.getheaders()
print(res_headers)
cook_data=response.getheaders()
print(cook_data)
reason=response.reason
print(reason)
str_html=b_html.decode('utf-8')
print(type(str_html))

with open('b_baidu.page.html','w') as file:
    file.write(str_html)


req_header = {
    'user-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

req = request.Request(url,headers=req_header)

response=request.urlopen(req)

print(response.status)
response.read()
response.getheaders()
response.getheader('Server')
response.reason






