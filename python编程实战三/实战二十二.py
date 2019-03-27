print("------跳一跳，输入 开始 即可游戏")
print("欢迎回来，请开始游戏")
print("请输入\(中心、音乐模块、微信支付模块)")
a = input("请输入:")
while True:
    if a != "中心" and a != "音乐模块" and a != "微信支付模块" and a != "退出":
        print("您输入有误")
        a = input("请出重新输入：")
    else:
        if a == "中心":
            print("您的分数为：32")
            a = input("请输入:")
        elif a == "音乐模块":
            print("您的分数为：30")
#else:
#    break
            a = input("请输入:")
        elif a == "微信支付模块":
            print("您的分数为：42")
#else:
#    break
            a = input("请输入:")
        elif a == "微信支付":
            print("输入有误，请重新输入")
            a = input("请输入:")
        elif a == "退出":
            print("以退出")
            break

