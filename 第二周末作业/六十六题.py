
time = 0
#shot_leg = []
for number in range(1,100):
    if number % 7 == 0 or number % 10 == 7:
         time += 1
         print(number,end=",")
         continue
print("拍腿次数:%d"%time)
#        shot_legs.append(number)
#        print(number)
#print(len(shot_legs))
