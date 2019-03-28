import requests
#文件上传
#测试接口
url='https://httpbin.org/post'
files={
    'file':open('cookies.txt','r')
}
response=requests.post(url,files=files)
print(response.status_code)
print(response.text)