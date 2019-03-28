#使用cookiejar的目的:管理cookie,保存cookie值
#一旦存储cookie之后,下一次发起请求的时候会携带cookie
#cookie是保存在内存里面的,最后会进行垃圾回收

from urllib import request,parse
from http.cookiejar import CookieJar
#创建cookiejar,目的如上
cookie_jar=CookieJar()
#httpcookieprocess创建handle处理器,管理cookiejar
handler=request.HTTPCookieProcessor(cookie_jar)
#自定义opener
opener=request.build_opener(handler)
#分析发现

