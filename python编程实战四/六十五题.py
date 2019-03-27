#constellation = [3,"白羊座",4"金牛座",5"双子座",6"巨蟹座",7"狮子座",8"处女座",9"天秤座",10"天蝎座",11"射手座",12"摩羯座",1"水瓶座",2"双鱼座"]
#month_list = [1,2,3,4,5,6,7,8,9,10,11,12]
def constellation(mouth,day):
    if (mouth==3 and day>=21) or (mouth==4 and day<=20):
       a = "白羊座"
       return a  
    if (mouth==4 and day>=21) or (mouth==5 and day<=20):
       b = "金牛座"
       return b   
    if (mouth==5 and day>=21) or (mouth==6 and day<=21):
       c = "双子座"
       return c    
    if (mouth==6 and day>=22) or (mouth==7 and day<=22):
       d = "巨蟹座"
       return d   
    if (mouth==7 and day>=23) or (mouth==8 and day<=22):
       e = "狮子座"
       return e    
    if (mouth==8 and day>=23) or (mouth==9 and day<=22):
       f = "处女座"
       return f    
    if (mouth==9 and day>=23) or (mouth==10 and day<=22):
       g = "天秤座"
       return g   
    if (mouth==10 and day>=23) or (mouth==11 and day<=21):
       h = "天蝎座"
       return h    
    if (mouth==11 and day>=22) or (mouth==12 and day<=21):
       l = "射手座"
       return l    
    if (mouth==12 and day>=22) or (mouth==1 and day<=19):
       k = "摩羯座"
       return k    
    if (mouth==1 and day>=20) or (mouth==2 and day<=18):
       j = "水瓶座"
       return j    
    if (mouth==2 and day>=19) or (mouth==3 and day<=20):
       m = "双鱼座"
       return m    
month = int(input("请输入月份 (例如:5) :"))
day = int(input("请输入日期 (例如:17) :"))
result = constellation(month,day)
print("%s月%s日星座为:%s"%(month,day,result))
#for month1 in range(1,13):
#    if month1 = month and 

