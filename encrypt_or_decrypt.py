from time import sleep
import sys
waittime1=1

def welcome():
    print("欢迎使用文本加密/解密程序（仅限英文字母输入）！")
    sleep(waittime1)
    print("此程序为lfw在学习python的第15天所写，现在是15:33，哈哈哈！")
    sleep(waittime1)

def get_user_choice():
    print()
    print("=====新一轮加密/解密=====")
    while True:
        user_choice=input("请按1或2选择您要执行的操作（1加密，2解密）：")
        if user_choice!="1" and user_choice!="2" :
            print("无效输入，请重新输入！")
            sleep(waittime1)
            continue
        return user_choice

def get_user_text():
    while True:
        user_text=input("请输入文本：").strip()
        if user_text=="":
            print("不可输入空白内容！请重新输入。")
            sleep(waittime1)
            continue
        return user_text

def get_user_shift():
    while True:
        try:
            user_shift=int(input("请输入加密/解密位移（1~25）："))
            if user_shift<1 or user_shift>25:
                print("加密/解密位移必须为1~25中的整数！请重新输入。")
                sleep(waittime1)
                continue
            return user_shift
        except ValueError:
            print("加密/解密位移必须为1~25中的整数！请重新输入。")
            sleep(waittime1)
            continue

def encrypt(user_text,user_shift):
    result=""
    for character in user_text:
        if character.isalpha():
            start = ord('a') if character.islower() else ord('A')
            result += chr((ord(character) - start + user_shift)%26 + start)
        else:
            result += character
    return result

def decrypt(user_text,user_shift):
    return encrypt(user_text,-user_shift)

def continue_or_not():
    while True:
        sleep(waittime1)
        user_choice2 = input("要继续吗（Y继续/N退出）：").upper()
        if user_choice2 not in ["Y","N"]:
            print("无效输入，请输入Y或N！")
            continue
        if user_choice2 == "Y":
            break
        if user_choice2 == "N":
            sys.exit()

def main():
    welcome()
    while True:
        user_choice = get_user_choice()
        user_text = get_user_text()
        user_shift = get_user_shift()
        if user_choice=="1":
            result = encrypt(user_text,user_shift)
            print(f"加密结果：{result}")
        else:
            result = decrypt(user_text,user_shift)
            print(f"解密结果：{result}")
        continue_or_not()

if __name__=="__main__":
    main()
    
