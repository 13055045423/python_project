from urllib import parse,request


url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

fromdata= {
    'first':'true',
    'pn':'1',
    'kd':'c++'
}

formdata= parse.urlencode(fromdata).encode('utf-8')
req_header={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_%E6%B1%A0%EF%BC%8B%EF%BC%8B?labelWords=&fromSearch=true&suginput='
}
req=request.Request(url,headers=req_header)
response=request.urlopen(req)
print(response.status)
print(response.read().decode('utf-8'))
