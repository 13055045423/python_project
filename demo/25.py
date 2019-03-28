#pip3 install requests
#requests模块:是对urllib的封装,可以实现urllib的所有功能
#并且api调用更加简单方便
import requests
#url='http://www.baidu.com/'
url='http://www.sina.com'
#url要请求的url
#params:get请求后面要拼接的参数
"""
:param method: 要发起的请求是什么
:param url: 要请求的目标url
:param params: get请求的目标url
:param data: Dictionary, post请求的表单数据
:param json: 传递json数据跟上面的data效果类似
:param headers: (optional) Dictionary 请求头
:param cookies: (optional) Dict or CookieJar object (设置cookies信息模拟用户请求)
:param files: 上传文件
:param auth: 网站需要验证的信息（账号和密码）
:param timeout: 设置请求的超时时间
:param allow_redirects: bool,是否允许重定向
:param proxies: (optional) Dictionary （设置代理）
:param verify:  Defaults to ``True``.（忽略证书认证,默认为True表示不忽略）
"""
req_header={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
parmars={
    'wd':'豆瓣'
}
response=requests.get(url,headers=req_header)
response.encoding='utf-8'
#从响应结果中获取的信息
#(这里得到的是解码后的字符串)
html=response.text
"""
#如果使用response.text出现了乱码
方式一
#response.content.decode('')
方式二
response.encoding=''设置编码类型
"""

#获取bytes类型的数据
b_html=response.content
#获取状态吗码
code=response.status_code
#获取响应头
response_headers=response.headers
#请求头
req_headers=response.request.headers
#获取当前请求的url地址
current_url=response.url
#response.json():可以将json字符串转换为python数据类型
print(code)
print(html)

