# import requests,json
# from lxml.html import etree
# def jingdong(url):
#     html_data=request_data(url)
#     print(html_data)
#     #data_json=json.loads(html_data.lstrip('fetchJSON_comment98vv3464(').rstrip(');'))
#     data_json = json.loads(html_data.lstrip('/**/jQuery21109878394943171129_1552361878786(').rstrip(');'))
#     #print(data_json)
#     data={}
#     for i in range(3,4):
#         #data['content']=data_json['comments'][i]['content']
#         data['title']=data_json['result']['wall']['docs'][i]['title']
#         data['clientUrl'] = data_json['result']['wall']['docs'][i]['clientUrl']
#         html=request_data(data['clientUrl'])
#         print(html)
#         #print(data)
#
#
# def request_data(url):
#     req_headers={
#         'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
#         #'Cookie':'__jdu=372559662; areaId=12; PCSYCityID=1000; shshshfpa=c5fe053d-af20-c60b-558c-f79c9c8dcb48-1552316588; __jdc=122270672; shshshfpb=zJ9txC4BH%20cP%2FXSGD3SFyig%3D%3D; __jda=122270672.372559662.1545925302.1552316637.1552316705.3; xtest=5528.cf6b6759; ipLoc-djd=1-72-2799-0; rkv=V0200; qrsc=1; mt_xid=V2_52007VwEUUVlcWl0YSikOVzIERwBVXE5eHEEcQABmCxBOVF5TXwNJG1tVZgEbUFlcVwgvShhcDXsCEE5dWENZHUIYWA5nCyJQbVhiWB9AG1QNYQUXYl1dVF0%3D; unpl=V2_ZzNtbRECQxYnC0Bdek4JAWILEl0RVRNHdwsSA38YXAxiVkEIclRCFX0UR1ZnGVwUZAEZXERcQRxFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHkfXwFjCxVaQWdzEkU4dl18HV0BZDMTbUNnAUEpDU5cexBdSGUFEVlGX0QSdjhHZHg%3d; __jdb=122270672.9.372559662|3.1552316705; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_8fc6d820322c4c7e9d8daa1f08bd06af|1552316873950; shshshfp=eaa2826a44ccec526edf475cb90fdb61; shshshsID=de378483267cc7acf2895672c08304fb_12_1552316874693',
#         #'Referer':'https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d10da4070f9c469ea09a678f8e8f3e94'
#     }
#     response=requests.get(url,headers=req_headers)
#     if response.status_code == 200:
#         print(response.status_code)
#         return response.text




    # html=etree.HTML(html_data)
    # li_list=html.xpath('//ul[@class="gl-warp clearfix"]//li[@class="gl-item"]')
    # for li in li_list[2:3]:
    #     a_href='https:'+li.xpath('./div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]/a/@href')[0]
    #     print(a_href)
    #     html=request_data(a_href)
    #     print(html)
    #     parse_data(html)

# def parse_data(html):
#     xiangqing_data=etree.HTML(html)
#     div_list=xiangqing_data.xpath('//div[@id="comment-0"]//div')
#     for div in div_list:
#         print(div)
#
#
#
#
#
# if __name__ == '__main__':
#     url = 'https://list.mogujie.com/search?callback=jQuery21109878394943171129_1552361878786&_version=8193&ratio=3%3A4&cKey=15&page=1&sort=pop&ad=0&fcid=51716&action=boyfriend&acm=3.mce.1_10_1ksa2.128038.0.0j2UNrkthKdwk.pos_7-m_484857-sd_119&ptp=1.n5T00.0.0.Qrteowd8&_=1552361878787'
#     jingdong(url)
import requests,json
from lxml.html import etree
def mogujie(url):
    html=request_data(url)
    print(html)
    #pyrhon_data=json.loads(html.lstrip('jQuery21109553044801891435_1552369361704,jQuery21109553044801891435_1552369361704(').rstrip(')'))
    lxml_data=etree.HTML(html)
    #data={}
    #if lxml_data:
        # data['content']=pyrhon_data['data']['list'][0]['content']
        # print(data)
    div_list=lxml_data.xpath('//div[@class="grid g-clearfix"]/div[1]//div')
    print(div_list)
    for div in div_list:
        a_href=div.xpath('./div[3]/div[2]/a/href').extract_first('')

        print(a_href)




def request_data(url):
    req_header={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Cookies':'_uab_collina=155237084187810679706803; t=36c2ec3c424cf4dec9c94e8691ab6f1c; cna=fdegFLwAk1ICASv6yT7o8kYh; thw=cn; cookie2=192f4b13bbd5272a838b6c47228c8ff4; _tb_token_=5639ee537e533; lid=tb31173682; lc=VypS3Bdlmhj778r4Mhfx; tg=0; enc=I%2FtMeK01toZfCCEoGQrD5GfxFUEBwg41R803%2ByWkqCpxG91qSNfjsini6KmYUjsMqUMqNKMoYesHtih65IuVMg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; XSRF-TOKEN=98e452bd-b903-4c90-9dab-c3b14d6945d4; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; miid=1215633468583507099; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zfvmw%2Fq5hkaVbNAJEuHk8Y1DOHlLCyJ8as3HJuVymu8pQ2s0VH1wPbiH9mlHj14Wch44yQ3Gzm234kvc1swkAqA8axA2cZsOEnGctuTflek5aeEYLcLn99Qp0VrOeoZdDp1ISgiGXXBmZ1o%2F4ZzOE6SrlqGUX0kGxuGMSQpwMy9gve6HDY6UBHA1pBDNF2qurKpK8S7%2BU%2F7fxEH0CKlR3Dy%2FUyymBKDSH7ajz6HUoZoF8im0%2FsTmFyKoaTRxqRkJoWVg%3D%3D; whl=-1%260%260%261552378032971; cookieCheck=42245; v=0; unb=1719407697; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=WqG3DMC9Fb5mPLIQo9kR&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie14=UoTZ5iY212OuYw%3D%3D&tag=8&lng=zh_CN; sg=27d; _l_g_=Ug%3D%3D; skt=434e2e1943bb41fe; log=lty=Ug%3D%3D; cookie1=UNQ1xI9QCUUyXvVTjtk%2F4%2FOTq6t91J8h8F%2BNZbKDKXE%3D; csg=5480dc09; uc3=vt3=F8dByEv9pNGduU6sDYs%3D&id2=UoYfqC%2FCnY5Tjg%3D%3D&nk2=F5RGNwnEddfKFA%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; existShop=MTU1MjM3OTA0Mg%3D%3D; tracknick=tb31173682; lgc=tb31173682; _cc_=WqG3DMC9EA%3D%3D; dnk=tb31173682; _nk_=tb31173682; cookie17=UoYfqC%2FCnY5Tjg%3D%3D; mt=ci=0_0&np=; isg=BDQ0YmO21OAmhECfJ0qvaOcDBfsKGVL1r3u9Fs6Vn79yOdWD9h9Whx37uTFEwZBP; l=bBx5Sh4nv___Zr7yBOCg5Qhfh87OYIRfguSJcRvMi_5CZ6L2AebOl_xiXFp6Vj5Pt_TB45h40WytGFMbJzpf.',
        'Referer':'https://www.taobao.com/markets/nanzhuang/2017new?spm=a21bo.2017.201867-main.2.5af911d92xW2CU'
    }
    # form_data={
    #     'callback': 'jQuery21109553044801891435_1552369361704',
    #     'pageSize': 20,
    #     'sort': 1,
    #     'isNewDetail': 1,
    #     'itemId': '1ls0rxo',
    #     'type': 1,
    #     'marketType': 'market_mogujie',
    #     '_': '1552369361705',
    # }
    s=requests.session()
    response=s.get(url,headers=req_header)
    if response.status_code==200:
        print(response.status_code)
        return response.text

if __name__ == '__main__':
    url = 'https://s.taobao.com/list?spm=a217m.8316598.313651-static.3.859b33d5s9xu5g&q=%E5%A4%B9%E5%85%8B&cat=50344007&style=grid&seller_type=taobao'
    mogujie(url)

# //detail.tmall.com/item.htm?id=582050733168&rn=3b96276187850e5bdc23e1edd1714643&abbucket=20
# https://lianchuangfs.tmall.com//detail.tmall.com/item.htm?id=574264730422&rn=7c60df05765ee18188be767008caeab1&abbucket=20
# https://lianchuangfs.tmall.com//detail.tmall.com/item.htm?id=582050733168&rn=2c6552ec9249358b381d08c7e4e3f20f&abbucket=20
#
# https://s.taobao.com//item.taobao.com/item.htm?id=587567829896&ns=1&abbucket=5