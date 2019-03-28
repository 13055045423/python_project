from urllib import request
url = 'https://www.douban.com/people/188926794/'
req_header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Cookie':'ll="108305"; bid=CnDREx_pnwM; _ga=GA1.2.1876680516.1545292869; __yadk_uid=Vu1Hwoune2wqpS8oFlZizzRzBK7UmNYK; douban-profile-remind=1; __utmv=30149280.18892; ue="1402051690@qq.com"; _vwo_uuid_v2=D7E3CC049BBAC7C249B1A2E29E4697359|02a59beeabd2ea8456d7a4b7ab689160; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1551403755%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dj4XW9PMWg9M4E1skpa3YTKuXRevAY7Jan1cZO8yQQii%26wd%3D%26eqid%3Def7fea2a000995b5000000035c788ab0%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1876680516.1545292869.1546504937.1551403756.9; __utmc=30149280; __utmz=30149280.1551403756.9.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; dbcl2="188926794:cBo10EG56G4"; ck=oNdQ; ap_v=0,6.0; push_doumail_num=0; _pk_id.100001.8cb4=3d4e1684ec6ad3f4.1545292867.6.1551403787.1546505770.; __utmb=30149280.5.10.1551403756; push_noty_num=1'
}
req = request.Request(url=url,headers=req_header)
response=request.urlopen(req)
if response.status==200:
    with open('doubai.html','w') as file:
        file.write(response.read().decode('utf-8'))
