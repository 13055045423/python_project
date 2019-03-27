print("查询能量来源！退出程序请输入0：",end = "")
#print("能量来源如下：")
#print("生活缴费，行走捐，共享单车，线下支付，网络购票")
a = input("")
while True:
    if a == "行走捐":
        print("能量来源如下：")
        print("生活缴费，行走捐，共享单车，线下支付，网络购票")
        print("200")
        break
    elif a == "生活缴费":
        print("能量来源如下：")
        print("生活缴费，行走捐，共享单车，线下支付，网络购票")
        print("300")
        break
    elif a == "共享单车":
        print("能量来源如下：")
        print("生活缴费，行走捐，共享单车，线下支付，网络购票")
        print("350")
        break
    elif a == "线下支付":
        print("能量来源如下：")
        print("生活缴费，行走捐，共享单车，线下支付，网络购票")
        print("380")
        break
    elif a == "网络购票":
        print("能量来源如下：")
        print("生活缴费，行走捐，共享单车，线下支付，网络购票")
        print("500")
        break
    else:
        if a == "0":
            print("以退出")
            break
