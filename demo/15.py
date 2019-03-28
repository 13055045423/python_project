#urllib.error:在发送请求的过程中,可能会以为各种情况
#导致请求出现异常,因而导致代码崩溃,所以我们悬疑处理这些异常的请求
from urllib import error,request
def check_urlerror():
    """
    1.没有网络
    2.服务器链接失败
    3.找不到指定服务器
    :return: 
    """
    url='http://www.baidu.com/'
    try:
        response=request.urlopen(url,timeout=10)
        print(response.status)
    except error.URLError as err:
        print(err.reason)

check_urlerror()

def check_httperror():
    url='https://www.qidian.com/all/nsacnscn.htm'
    try:
        response=request.urlopen(url)
        print(response.status)
    except error.HTTPError as err:
        print(err.code)
        print(err.reason)
        print(err.headers)
    except error.URLError as err:
        print(err.reason)

check_httperror()