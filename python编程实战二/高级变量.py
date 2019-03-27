a = [1,2,3,4,5]#列表a
name_list = ["a","b","c","d"]#列表name_list

name_list.insert(0,"e") #在指定位置插入数据
print(name_list) 

name_list.append('w') #在末尾追加数据
print(name_list)

name_list.extend(a) #列表a合并到name_list列表
print(name_list)

name_list[0] = "g"#修改列表索引0位置的数据
print(name_list) 

del name_list(0)
print(name_list)#删除制定索引数据

name_list.pop()#删除末尾数据
print(name_list)

name_list.popitmes()#随机删除一个数据
print(name_list)

name_list.count(4)#查看数据在列表出现过几次
len(name_list)#查看列表长度

name_list.remove(2)#删除数据第一次出现的位置
print(name_list)

name_list.sort()#让列表升序排序
print(name_list)

name_list.sort(reverse=True)#降序排序
print(name_list)

name_list.reverse()#逆序，反转
print(name_list)

for a in name_list:#遍历列表方法一
    print(a)

for c,d in enumerate name_list:#遍历列表方法二
    print(c,d)

test("b","c","d","e","f")#创建元组
test1(1,)#当元祖为一个字符的时候后面要跟一个逗号，特别要注意。

test.count("c")#查看元素c在元组出现过几次
test.index()

for e in test:#遍历元组
    print(e)

for s,h in enumerate test:
    print(s,h)

#元组和列表之间互换

list(test) #将元组转换成列表
print(type(test)) #查看test类型

apple = {name:"liusijia",age:23,phone:123456}#定义一个字典
print(apple)

apple.keys()#查看字典所有keys健
apple.values()#查看所有values值

apple.popitmes()#随机删除一个健值对
apple.pop(name)#删除指定健值对
apple.clear()#清空字典

l = apple[age]#根据健取值并定义给l
print(l)

apple.get(age)#取值

