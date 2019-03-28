from urllib import parse,request

import re
def tiebaspider(name,start_page,end_page):
    for page in range(start_page,end_page+1):
        parmars={
            'kw':name,
            'ie':'utf-8',
            'pn':(page-1)*50
        }
        result=parse.urlencode(parmars)
        full_url ='https://tieba.baidu.com/f?'+result
        print(full_url)
        html=load_data(full_url)
        #print(html)
        tizi_urlinfo=parse_page_detail_url(html)
        #print(tizi_urlinfo)
        for note in tizi_urlinfo:
            print(note)
            detail_url = 'https://tieba.baidu.com'+note[0]
            print(detail_url)
            title = note[1]
            print('正在获取'+title+'的帖子详情')
            html=load_data(detail_url)
            #print(html)
            images=parse_page_imageurl(html)
            download_image(images)

def download_image(images):

    for image_url in images:
        req_header={
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        req=request.Request(image_url,headers=req_header)
        response=request.urlopen(req)
        if response.status==200:
            filname=response.url[-20:]
            with open('tiebaprctue/'+filname,'wb') as file:
                file.write(response.read())
                print(filname,'下载完毕')


def parse_page_imageurl(html):
    """
    <img class="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/sign=c585c0c2f903918fd7d13dc2613c264b/892397dda144ad34ff2010a5dea20cf431ad8571.jpg" size="193348" changedsize="true" width="560" height="755">
    :param html:
    :return:
    """
    pattern=re.compile('<img.*?class="BDE_Image".*?src="(.*?)".*?>',re.S)
    result=re.findall(pattern,html)
    print('图片链接',result)
    return result


def load_data(url):
    req_header={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    req = request.Request(url,headers=req_header)
    response=request.urlopen(req)
    print(response.status)

    if response.status==200:
        return response.read().decode('utf-8','ignore')


def parse_page_detail_url(html):

    """
    <a rel="noreferrer" href="/p/6050646923" title="有一起玩游戏吗？快乐的那种you" target="_blank" class="j_th_tit ">有一起玩游戏吗？快乐的那种you</a>
    :param html:
    :return:
    """
    pattern=re.compile('div\sclass="threadlist_title pull_left j_th_tit "'+
                       '.*?<a.*?href="(.*?)".*?>(.*?)</a>.*?</div>',re.S)


    result =re.findall(pattern,html)
    print(result)
    return result

if __name__ == '__main__':
    name = input('请输入贴吧名称')
    start_page=int(input('输入起始页：'))
    end_page=int(input('请输入截止页'))
    tiebaspider(name,start_page,end_page)



