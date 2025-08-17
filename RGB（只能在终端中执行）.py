from time import sleep
import os
os.system('')

wait_time1=0.5

def print_RGB_color(R,G,B,text="      "):
    print(f"\033[48;2;{R};{G};{B}m{text}\033[0m RGB:({R},{G},{B})")

def error_hint():
    print("请输入有效数字！")
    sleep(wait_time1)
    print()

def get_user_RGB():
    while True:
        try:
            R=int(input("请输入红色值（0~255）："))
            if R>255:
                error_hint()
                continue
            G=int(input("请输入绿色值（0~255）："))
            if G>255:
                error_hint()
                continue
            B=int(input("请输入蓝色值（0~255）："))
            if B>255:
                error_hint()
                continue
            return R,G,B
        except ValueError:
            error_hint()
            continue

def user_choice():
    user_input=input("输入回车继续。")
    return user_input==""

def main():
    while True:
        R,G,B=get_user_RGB()
        print_RGB_color(R,G,B,text="      ")
        if user_choice():
            continue

if __name__=="__main__":
    main()
