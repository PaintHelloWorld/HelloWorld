import random
import time
target=random.randint(1,100)
while True:
    
    try:
        guess=int(input("请你输入1到100的整数（按下enter以确认）："))
        
    except ValueError:
        print("请你输入整数数字！")
        continue
    if guess<1 or guess>100:
        print("请你输入1到100的整数数字！")
        continue

    if guess<target:
        print("猜小了，换一个继续吧！")
    elif guess>target:
        print("猜大了，换一个继续吧！")
    else:
        print("恭喜你猜对了，5秒后将自动退出游戏~")
        for i in range(5,0,-1):
            time.sleep(1)
            print(i)
        break
    
