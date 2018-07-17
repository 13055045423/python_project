b = int(input("请输入你的收入"))
a = 0
income = 3500
c = b - income
while True:
    if c <= 1500:
        c = c*0.03
        d = b-c
        print("税额为:%d"%c)
        print("实际收入:%d"%d)
        break
    elif c > 1500 and c <= 4500:
        c = c*0.1
        d =b-c
        print("税额为:%d"%c)
        print("实际收入:%d"%d)
        break
    elif c >4500 and c <= 9000:
        c =c*0.2
        d =b-c
        print("税额为:%d"%c)
        print("实际收入:%d"%d)
        break
    elif c > 9000 and c <= 35000:
        c =c*0.25
        d =b-c
        print("税额为:%d"%c)
        print("实际收入:%d"%d)
        break
    elif c > 35000 and c <= 55000:
        c =c*0.3
        d =b-c
        print("税额为:%.2f"%c)
        print("实际收入:%d"%d)
        break
    elif c > 55000 and c <= 80000:
        c =c*0.35
        d =b-c
        print("税额为:%d"%c)
        print("实际收入:%d"%d)
        break
    elif c > 80000:
        c =c*0.45
        d =b-c
        print("税额为:%d"%c)
        print("实际收入:%d"%d)
        break
