from urllib import parse,request
import pymysql,re
def maoyanspider(start_url):
    """
    根据url发起请求,解析数据,构造下一页请求
    :param start_url:
    :return:
    """
    html,current_url=load_page_data(start_url)
    #解析数据
    movies=parse_page_data(html)
    if len(movies)>0:
        for movie in movies:
            moviedata={}
            moviedata['rank']=int(movie[0])
            moviedata['coverimage']=movie[1]
            moviedata['name']=movie[2]
            moviedata['actor']=movie[3].replace('\n','').replace(' ','')
            moviedata['publishtime']=movie[4].replace('上映时间:','')
            moviedata['scorenum']=float(movie[5]+movie[6])

            save_data_to_db(moviedata)
        #如何构造下一页的链接，什么时候停
        pattern=re.compile('.*?offset=(\d+)')
        current_offset=int(re.findall(pattern,current_url)[0])
        nextpage_offset=current_offset+10
        #方式二:通过正则替换
        pattern=re.compile('offset=\d+')
        next_url=re.sub(pattern,'offset='+str(nextpage_offset),current_url)
        maoyanspider(next_url)


def save_data_to_db(movieinfo):
    """
    存储数据库
    :param movieinfo:
    :return:
    """
    pass


def parse_page_data(html):
    """
    从页面源码中提取目标数据
    :param html:
    :return:
    """
    pattern=re.compile(
        '<dd>.*?<i.*?>(.*?)</i>'+
        '.*?<img.*?data-src="(.*?)"'+
        '.*?<p.*?>.*?<a.*?>(.*?)</a>'+
        '.*?<p.*?>(.*?)</p>'+
        '.*?<p.*?>(.*?)</p>'+
        '.*?<i.*?>(.*?)</i>'+
        '.*?<i.*?>(.*?)</i>.*?</dd>',re.S
    )

    result=re.findall(pattern,html)
    print(result)
    return result


def load_page_data(url):
    req_header={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

    }
    req=request.Request(url,headers=req_header)
    response=request.urlopen(req)
    if response.status==200:
        return response.read().decode('utf-8'),response.url

if __name__ == '__main__':
    mysql_client=pymysql.Connect(host='127.0.0.1',user='root',password='19951028a',db='dd',port=3306,charset='utf8')
    #创建游标
    cursor=mysql_client.cursor()
    start_url='https://maoyan.com/board/4?offset=0'
    maoyanspider(start_url)
