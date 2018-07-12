zhanghao = "1402051690"
mima = "19951028a"
jine = "1000"
yonghuzhanghao = int(input())
yonghumima = int(input())
if yonghuzhanghao == zhanghao and yonghumima == mima:
    print("可以取钱了")
yonghushurujine = int(input("请输入取钱金额"))
    if yonghushurujine <= 1000:
        print('取了%s' % yonghushurujine and '还剩' jine - yonghujine)
    else:
        print("没钱取毛线")
else:
    print("非法账户")
