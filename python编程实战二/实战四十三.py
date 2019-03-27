def prime_number():# 定义质数
    for i in range(2,100):#质数大于1范围在0到100
        for j in (2,i):
            if i%j==0 and i!= j:#判断是否为质数
                break#不是退出
            else:
                print(i)#是输出
prime_number()#调用定义函数
        
