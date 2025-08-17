from random import choice
from time import sleep

symbols=["\U0001F600","\U0001F970","\U0001F602","\U0001F60E"]

print("======简易老虎机======")
print("按回车键拉杆，匹配3个相同符号即可获胜！")

while True:
    input("按下回车键开始...")

    result=[choice(symbols)for _ in range(3)]
    print("转动中......")
    sleep(0.5)

    print("结果："+"|".join(result))

    if result[0]==result[1]==result[2]:
        print ("恭喜！你赢了！")
        sleep(5)
        break
    else:
        print("别灰心，再试一次吧！")

