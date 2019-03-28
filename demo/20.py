import requests
#url,目标url
#data=None:post请求要上传的表单数据
url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
form_data={
    'first':'true',
    'pn':1,
    'kd':'python',
}
# proxies ={
#     'http':'180.168.13.26:8000',
#     'https':'218.76.253.201:61408',
# }
#设置请求头
req_header={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_c%2B%2B?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
}
response=requests.post(url,data=form_data,headers=req_header)

print(response.status_code)
print(response.text)

#可以将返回的json字符串转换为python数据类型
data=response.json()
print(type(data))
