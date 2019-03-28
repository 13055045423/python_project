from urllib import request
def send_request(req,timeout=100,content=None):
    """
    自己定义一个方法发起请求
    :param req: request请求对象
    :param timeout: 设置请求的超时时间
    :param content: 忽略ssl证书验证
    :return:
    handler:创建handler处理器是为了实现特定功能
    opener:为了使用opener.open方法发起请求
    """
    if content:
        handler=request.HTTPSHandler(context=content,debuglevel=1)
        opener=request.build_opener(handler)
        return opener.open(req,timeout=timeout)
    else:
        #debuglevel默认为0,设置为1的话表示开启debug模式,
        #会对请求进行跟踪,方便查看每一个请求的信息
        handler=request.HTTPSHandler(debuglevel=1)
        opener=request.build_opener(handler)
        return opener.open(req,timeout=timeout)
url='http://www.baidu.com'
req_header={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

req=request.Request(url,headers=req_header)
response=send_request(req)
print(response.read().decode('utf-8'))