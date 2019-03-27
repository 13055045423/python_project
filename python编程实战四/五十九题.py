def clrcultion():
    source = []
    while True:
        lsj_user = int(input("请输入要添加列表的值:"))
     #   source.append(lsj_user)
        if lsj_user != 0:
            source.append(lsj_user)
        elif lsj_user == 0:
            print("退出输入,进行排序")
            return source
source = clrcultion()
#source = []
num = len(source)
k = 1
while True:
    for i in range(num-k):
        if source[i] > source[i+1]:
            temp = source[i]
            source[i] = source[i+1]
            source[i+1] = temp
    k += 1
#    print(source)
    if k == num - 1:
        break
print("排序结果为:",end = "")
print(source)
