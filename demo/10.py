"""
.:表示匹配除了换行符之外的任意字符
\:转义字符
[a-z]:匹配a-z里面的任意一个字符
\d:匹配数字　-> [0-9]
\D:匹配非数字[^\d]
\s:匹配空白字符(空格,\n,\t...)
\S:匹配非空白字符
\w:匹配单个字符[A-Za-z0-9]
\W:匹配非单个字符
^:匹配以....开头
$:匹配以....结尾
():分组
|:或

多字符匹配
*:匹配*前面的字符任意次数
+:匹配+号前面的字符至少一次
?:匹配?前面字符零次或者一次
{m}:匹配{m}前面字符m次
{m,n}:匹配{m,n}前面的字符m-n次

"""

import re
# 把正则表达式构建为一个patern对象
sub_str='abcdefabcd'
pattern = re.compile('b')
#从字符串的起始位置开始匹配,开头就符合必须符合正则规则
#如果匹配到了返回结果，如果匹配不到就返回NONE,单词匹配
result=re.match(pattern,sub_str)
print(type(result))
if result:
    print(result.group())

#在整个字符串中进行匹配，同样是单词匹配,匹配到结果立即返回
#匹配不到则返回ＮＯＮＥ
result=re.search(pattern,sub_str)
print(result.group())

#在整个字符串中国进行匹配,匹配出所有符合正则规则的结果
#以列表的形式返回
result=re.findall(pattern,sub_str)
print(result)

#在整个字符串中进行匹配，匹配出所有符合正则规则的结果
#但是返回一个迭代器
result=re.finditer(pattern,sub_str)
print(type(result))
for note in result:
    print(type(note))
    print(note.group())

#替换re.sub()
url='http://www.baidu.com/s?kw=aaa&pn=20'
#pattern,正则规则
#repl,要替换的字符串
#string,原始字符串
pattern=re.compile('pn=\d+')
result=re.sub(pattern,'pn=30',url)
print(result)
#分割re.spilt
pattern=re.compile('[=:&]]')
result=re.split(pattern,url)
print(result)

sub_html="""
<div class="threadlist_title pull_left j_th_tit ">
    
    
    <a rel="noreferrer" href="/p/5982749825" title="来聊" target="_blank" class="j_th_tit ">来聊</a>
</div>
"""
#re.S让点可以匹配包括换行的任意字符
pattern=re.compile('div.*?class="threadlist_title pull_left j_th_tit ">'+
                   '.*?<a.*?href="(.*?)".*?</div>',re.S)

result=re.findall(pattern,sub_html)
print(result)
