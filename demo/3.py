from urllib import parse,request
from fake_useragent import UserAgent

def searchspider(kw,start_page,end_page):
    quote_str = parse.quote(kw)
    print(quote_str)
    # unquote_str=parse.unquote(quote_str)
    # print(unquote_str)
    for page in range(start_page,end_page+1):
        parmars = {
            'wd':kw,
            'pn':(page-1)*10
        }
        result=parse.urlencode(parmars)
        print(result)
        full_url='https://www.baidu.com/s?'+result
        html=load_page(full_url)
        filename='第'+str(page)+'页'+kw+'.html'
        save_page_html(html,filename)

def save_page_html(html,filename):
    with open('baiduseach/'+filename,'w',encoding='utf-8') as file:
        file.write(html)

def load_page(url):
    req_header={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    req=request.Request(url,headers=req_header)
    response=request.urlopen(req)
    if response.status==200:
        print('请求成功',response.url)
        return response.read().decode('utf-8')

if __name__ == '__main__':
    user_agent=UserAgent()
    kw=input('请输入关键字')
    start_page=int(input('输入起始页'))
    end_page=int(input('输入结束页'))

    searchspider(kw, start_page, end_page)

