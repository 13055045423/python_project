# from urllib import parse,request
#
# import json
#
#
# url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
#
# formdata={
#     'i': '我的祖国',
#     'from': 'AUTO',
#     'to': 'AUTO',
#     'smartresult': 'dict',
#     'client': 'fanyideskweb',
#     'doctype': 'json',
#     'version': '2.1',
#     'keyfrom': 'fanyi.web',
#     'action': 'FY_BY_CLICKBUTTION',
#     'typoResult': 'false',
#     }
#
# formdata=parse.urlencode(formdata).encode('utf-8')
# req_header={
#     'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
# }
# req=request.Request(url,headers=req_header,data=formdata)
#
# response=request.urlopen(req)
#
# print(response.status)
# json_str=response.read().decode('utf-8')
# print(json_str)
from urllib import parse,request
import json

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

formdata = {
    'i': '我的祖国',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'typoResult': 'false',
}

formdata = parse.urlencode(formdata).encode('utf-8')

req_header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

req = request.Request(url,headers=req_header,data=formdata)

response = request.urlopen(req)

print(response.status)
# print(response.read().decode('utf-8'))
json_str = response.read().decode('utf-8')
print(json_str)

# json.loads():将json字符串,转换为python的数据类型；
# json类型的数据（对象和数组）对象－＞dict 数组->list
# json.load()
# json.dumps()
# json.dump()
"""
{
"type":
"ZH_CN2EN",
"errorCode":0,
"elapsedTime":23,
"translateResult":
    [
        [
            {"src":"我的祖国","tgt":"My motherland"}
        ]
    ]
}

"""
#{"name":"xxx","age":18,"info":["1","2","3"]}

data = json.loads(json_str)
print(type(data))

result = data['translateResult'][0][0]['tgt']
print(result)