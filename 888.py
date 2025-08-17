from time import sleep
attempts=0

print("恭喜您找到了这里！")
user_name=input("请在此输入您至高无上的用户名：")
user_gender=input("请输入您的性别（男/女/沃尔玛购物袋/其他）：")

if user_gender=="男":
    print(f"尊贵的{user_name}先生，您好！")
elif user_gender=="女":
    print(f"尊贵的{user_name}女士，您好！")
elif user_gender=="沃尔玛购物袋":
    print(f"尊贵的沃尔玛{user_name}购物袋，您好！")
else:
    print(f"尊贵的{user_name}{user_gender}，您好！")
print("请输入三位数密码，若密码正确，可获取机主最新机密：")
while True:
    user_input=input()

    if user_input=="888":
        print("恭喜您破解密码！")
        sleep(1)
        print()
        print("最新机密：")
        sleep(0.5)
        print("机主lfw正在收一个关门弟子，学费888元/节。现在下单，赠送关灯&关窗教程！")
        sleep(3)
        print()
        print("按下回车即可付费！心动不如行动，快来试逝吧！")

        input()

        print("支付处理中，请您耐心等待，这可能会花费3秒左右...")
        sleep(3)

        print("恭喜您已成功支付888元！系统正在下载《关门教程》《关灯教程》《关窗教程》......")
        sleep(4)
        print()
        print("下载完成！请检查您的邮箱（如果没收到，那大概率是被lfw关门外了......）！")
        sleep(4)
        print()
        print("谢谢惠顾！徒弟编号：#250xswl，记得给五星好评！")
        print()
        sleep(2)

        while True:
            choice=input("是否支付8888元升级至尊VIP套餐？（输入y/n确认）：")
            if choice=="y":
                print("支付成功！VIP教程已传至您的大脑皮层！")
                sleep(2)
                print("按下回车退出！")
                input()
                break
            elif choice=="n":
                print("穷鬼不配当关门弟子！")
                print()
                sleep(2)
                print("系统正在卸载《关门教程》《关灯教程》《关窗教程》......")
                print()
                sleep(3)
                print("卸载完成！")
                print()
                sleep(1)
                print("888元你也别想要了！你与关门弟子无缘！")
                sleep(5)
                break
            else:
                print("好嘛好嘛，动动你的小手指输入y，8888元的至尊待遇很难得的！")
                sleep(1)
        break
    else:
        attempts+=1
        print("密码错误，建议您去庙里求个签。")

        if attempts>=5:
            print("失败次数过多，请5秒后再试")
            for i in range(5,0,-1):
                sleep(1)
                print(i)
                attempts=0
            print(f"尊贵的{user_name}，看您有缘，直接告诉您，密码是888！")
            sleep(2)
            print("请再次输入密码：")
 
