#目标url:
#https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false

#post请求要提交的数据
#first: true
# pn: 1
# kd: C++
from urllib import request,parse
import json,pymysql,time

def lagouspider(url,fromdata):
    response_data=load_page_data(url,fromdata)
    #得到的数据是一个json字符串,需要转为python类型的数据
    data=json.loads(response_data)
    print(data)
    if data['success']:
        print('请求成功')
        #拿到职位信息
        postionJobs = data['content']['positionResult']['result']
        for jobdata in postionJobs:
            jobdata={}
            jobdata['positionName']=jobdata['positionName']
            jobdata['createTime'] = jobdata['createTime']
            jobdata['salary'] = jobdata['salary']
            jobdata['workYear'] = jobdata['workYear']
            jobdata['education'] = jobdata['education']
            jobdata['industryLables'] = jobdata['industryLables']
            jobdata['financeStage'] = jobdata['financeStage']
            jobdata['companySize'] = jobdata['companySize']
            jobdata['companyLabelList'] = ','.join(jobdata['companyLabelList'])
            jobdata['positionAdvantage'] = jobdata['positionAdvantage']

            #create table lagou(id int(11) not null auto_increment,positionName varchar(255),createTime varchar(255),salary varchar(255),workYear varchar(255),education varchar(255),industryLables varchar(255),financeStage varchar(255),companySize varchar(255),companyLabelList varchar(255),positionAdvantage varchar(255),primary key(id))
            save_data_to_db(jobdata)
        #判断是否需要发起下一次请求
        #去除当前页码
        cur_page=int(data['content']['pageNo'])
        #每页返回多少条数据
        page_size=int(data['content']['pageSize'])
        #职位总数
        totalcount=int(data['content']['positionResult']['totalCount'])
        if cur_page*page_size<totalcount:
            next_page=cur_page+1
            print('继续发起请求'+str(next_page)+'页')
            fromdata['pn']=next_page
            time.sleep(1)
            lagouspider(url,formdata)
    else:
        print('请求不成功,休息一会继续发起请求')
        time.sleep(10)
        print('重新发起第'+str(formdata['pn'])+'页请求')
        lagouspider(url,formdata)

def save_data_to_db(jobdata):
    """
    存储数据
    :param jobdata:
    :return:
    """
    sql="""
    insert into lagou(%s) values (%s)
    """%(','.join(jobdata.keys()),
         ','.join(['%s']*len(jobdata))
         )

    try:
        cursor.execute(sql,list(jobdata.values()))
        mysql_client.commit()

    except Exception as err:
        print(err)
        mysql_client.rollback()


def load_page_data(url,fromdata):
    """
    发起请求
    :param url:
    :param fromdata:
    :return:
    """
    #将表单数据转化为ＷＥＢ服务器能识别的url编码格式的bytes类型的数据
    from_data=parse.urlencode(fromdata).encode('utf-8')
    req_header={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Referer':'https://www.lagou.com/jobs/list_c%2B%2B?labelWords=&fromSearch=true&suginput=',

    }
    req=request.Request(url,headers=req_header,data=from_data)
    response=request.urlopen(req)
    if response.status==200:
        return response.read().decode('utf-8')



if __name__ == '__main__':
    """
    数据库链接
    """
    mysql_client=pymysql.Connect(host="127.0.0.1", user="root", password="19951028a",
                 database="dd", port=3306,
                 charset="utf8")
    cursor=mysql_client.cursor()

    url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    formdata={
        'first':'true',
        'pn':1,
        'kd':"c++"
    }
    lagouspider(url,formdata)