set_meal = ["考神套餐","单人套餐","情侣套餐"]
price = ["13元","9.9元","20元"]
print("米线店套餐如下:1.考神套餐 2.单人套餐 3.情侣套餐")
for subscript1,set_meal1 in enumerate(set_meal):
#    print(set_meal1)
    for subscript2,price1 in enumerate(price):
        if subscript1 == subscript2:
            print(set_meal[subscript1],price[subscript2])
