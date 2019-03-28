#urllib下使用代理
#http/https代理
#一定是一个高匿代理
#隐藏真是ip
from urllib import request

#自定义proxyHandler的目的是为了设置代理,使用代理发起请求
#proxies:对应的是一个字典
#代理有免费代理（西刺,快代理....）
#和收费代理(西刺,快递里....阿布云)
proxies ={
    # 'http':'180.168.13.26:8000',
    'https':'218.76.253.201:61408',
}
#独享代理,需要找好密码验证的
# proxies={
#     'http':'http://2295808193:6can7hyh@106.12.23.200:16818',
#     'https':'https://2295808193:6can7hyh@106.12.23.200:16818'
# }
handler =request.ProxyHandler(proxies=proxies)
#自定义opener
opener=request.build_opener(handler)
url='http://httpbin.org/get'
req_header={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
req=request.Request(url,headers=req_header)
response=opener.open(req)

print(response.status)
print(response.read().decode('utf-8'))
