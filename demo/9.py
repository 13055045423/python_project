from fake_useragent import UserAgent
user_agent=UserAgent()

print(user_agent.chrome)
print(user_agent.firefox)
print(user_agent.safari)

print('-------------')
print(user_agent.random)
print(user_agent.random)
print(user_agent.random)
print(user_agent.random)

from urllib import request

url = 'https://github.com/hellysmile/fake-useragent'

req_header ={
    'User-Agent':user_agent.random
}

req = request.Request(url,headers=req_header)

req.add_header('Referer','https://github.com/search?q=fake-useragent')
print(req.get_header('Referer'))
response=request.urlopen(req,timeout=10)
print(response.status)
print(response.url)