shengao = int(input())
shenjia = int(input())
yanzhifen = int(input())
if shengao > 180 and shenjia > 1000000 and yanzhifen > 99:
    print("高富帅")
elif shenjia > 10000000 and yanzhifen > 99:
    print("富帅")
elif yanzhifen > 99:
    print("帅")
else: 
    if shengao <= 160 and shenjia < 100 and yanzhifen <60:
        print("矮穷锉")
