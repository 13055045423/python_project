from urllib import parse,request

url = 'https://httpbin.org/post'

fordata={
    'name':'红红火火',
    'age':18,
    'gender':'男'
}

formdata = parse.urlencode(fordata).encode('utf-8')

resonse=request.urlopen(url,data=formdata)

print(resonse.status)
print(resonse.read().decode('utf-8'))

req_header={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
req =request.Request(url,headers=req_header,data=formdata)

response=request.urlopen(req)

print(response.status)
print(response.read().decode('utf-8'))

