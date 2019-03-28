#web客户端验证
import requests
#设置认证信息
auth=('username','password')
url='http://192.168.1.110'
response=requests.get(url,auth=auth)
print(response.status_code)
