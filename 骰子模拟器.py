from random import randint
from time import sleep

def welcome():
    print("欢迎使用骰子模拟器！")
    sleep(0.3)
    print("此代码为lfw在学习python的第13天所写，现在是15:22。哦耶！")
    sleep(0.3)
    print()

def get_dice_number():
    while True:
        try:
            dice_number=int(input("请输入骰子数量（1~6）："))
            if dice_number<1 or dice_number>6:
                print("骰子数量必须在1~6之间！")
                continue
            return dice_number
        except ValueError:
            print("请输入有效数字！")
            continue
         
def roll_dice(dice_number):
    results=[randint(1,6) for _ in range(1,dice_number+1,1)]
    print(results)

def main():
    welcome()
    dice_number=get_dice_number()
    while True:
        roll_dice(dice_number)
        while True:
            user_choice=input("输入回车继续，输入P更改骰子数量，输入Q退出。").strip()
            if user_choice=="":
                break
            if user_choice.lower()=="p":
                dice_number=get_dice_number()
                break
            if user_choice.lower()=="q":
                return
            else:
                print("无效输入，请重新输入！")
                continue

if __name__=="__main__":
    main()
            
