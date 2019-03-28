print("能量查询请输入！退出程序请输入0：",end = "")
b = "共享单车"
c = "生活缴费"
d = input("")
a = "行走捐"
e = "线下支付"
f = "网络购票"
while True:
    if d == "0":
        print("能量来源如下：")
        print("生活缴费、行走捐、共享单车、线下支付、网络购票")
        print("以退出")
        break
    else:
        if d != a and d != b and d != c and d != e and d != f and  d != 0:
            print("您输入有误")
            d = input("请重新输入")
        else:
            if d == a:
                print("能量生活来源如下：")
                print("生活缴费、行走捐、共享单车、线下支付、网络购票")
                print("200")
                d = input("请重新输入")
            elif d == c:
                print("能量生活来源如下：")
                print("生活缴费、行走捐、共享单车、线下支付、网络购票")
                print("300")
                d = input("请重新输入")
            elif d == b:
                print("能量生活来源如下：")
                print("生活缴费、行走捐、共享单车、线下支付、网络购票")
                print("350")
                d = input("请重新输入")
            elif d == e:
                print("能量生活来源如下：")
                print("生活缴费、行走捐、共享单车、线下支付、网络购票")
                print("380")
                d = input("请重新输入")
            elif d == f:
                print("能量生活来源如下：")
                print("生活缴费、行走捐、共享单车、线下支付、网络购票")
                print("500")
                d = input("请重新输入")

