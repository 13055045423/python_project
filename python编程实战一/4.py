import random
玩家 = int(input())
电脑 = random.randint(1,10)
if 玩家 == 电脑:
    print("胜利")
else:
    print("你是个loser")
