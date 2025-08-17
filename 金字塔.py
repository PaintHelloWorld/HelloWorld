from time import sleep

WAITING_TIME_NORMAL=0.1

WAITING_TIME_FINAL=15

print("欢迎来看机主写的屎山代码！")

while True:

    try:
        HEIGHT=int(input("请输入你想要的屎山高度（推荐不超过60）："))
        #超过60会显示不下

        if HEIGHT <=0:
            print("高度应为正整数！")

        for i in range(1,HEIGHT+1):
        
            spaces=" "*(HEIGHT-i)
            print(spaces+"\U0001F4A9"*i)

            if i==HEIGHT:
                sleep(WAITING_TIME_FINAL)
            else:
                sleep(WAITING_TIME_NORMAL)

    except ValueError:
        print("高度应为正整数！")
        
