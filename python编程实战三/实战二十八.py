a = int(input("年龄:"))
b = input("专业:")
c = input("是否重点大学:")
d = "电子信息工程"
e = "是"
f = "计算机"
if a >= 25 and a == d or b == d and c == e or a <= 28 and b == f:
    print("恭喜你，被录取")
else:
    print("抱歉，您为到达要求")
