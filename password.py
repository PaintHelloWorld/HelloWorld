from random import choice
import sys
from time import sleep

lowercase=['a','b','c','d','e','f','g', 'h','i','j','k','l','m','n', \
               'o','p','q','r','s','t', 'u','v','w','x','y','z']
uppercase=['A','B','C','D','E','F','G', 'H','I','J','K','L','M','N', \
               'O','P','Q','R','S','T', 'U','V','W','X','Y','Z']
digits=['0','1','2','3','4','5','6','7','8','9']
symbols=["!","@","#","$","%","^","&","*","(",")","+","<",\
             ">","?",":","-","=","/","~","\\"]
fenge = "========已开启新一轮使用========"
def p_or_q():
    while True:
        sleep(0.5)
        choice2 = input("输入P继续，输入Q退出。").upper().strip()
        if choice2 == 'Q':
            sys.exit()
        if choice2 == 'P':
            print(fenge)
            break
        else:
            print("无效输入，请按P或Q！")
            continue
    
def password_input():
    password = input("请输入您的密码：").strip()
    return password

def strength_check_1(password):
    has_lowercase = False
    has_uppercase = False
    has_digits = False
    has_symbols = False
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digits = True
        elif char in symbols:
            has_symbols = True
    strength = sum([has_lowercase,has_uppercase,has_digits,has_symbols])
    if strength == 4:
        print("比铁还硬比钢还强！")
    elif strength == 3:
        print("这个也倒可以了！")
    elif strength == 2:
        print("比鸡蛋壳强一点，但是防不住石头！")
    elif strength == 1:
        print("不要用这个！你的密码可能会被暴力破解！")

def strength_check_2(password):
    has_lowercase = False
    has_uppercase = False
    has_digits = False
    has_symbols = False
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digits = True
        elif char in symbols:
            has_symbols = True
    strength = sum([has_lowercase,has_uppercase,has_digits,has_symbols])
    if strength == 4:
        print("无敌了！")
    elif strength == 3:
        print("放心用你的密码吧，很强！")
    elif strength == 2:
        print("还算可以，算是中强密码了！")
    elif strength == 1:
        print("其实这强度不如硝酸甘油的键能...")

def length_check(password):
    if len(password)<6:
        while True:
            use_or_not = input("密码小于6位，确定要使用吗？！（Y/N）").upper().strip()
            if use_or_not == "Y":
                strength_check_1(password)
                p_or_q()
                break
            elif use_or_not == "N":
                p_or_q()
                break
            else:
                print("无效输入，请按Y或N！")
                continue
    else:
        strength_check_2(password)
        p_or_q()       
    
def function_choice():
    print("欢迎使用密码小工具！")
    print(fenge)
    while True:
        function = input("请按 1/2 选择功能（1.检测密码强度 2.随机生成高强度密码）：").strip()
        if function =='1':
            password = password_input()
            length_check(password)
        elif function == "2":
            password_generate()
            p_or_q()
        else:
            print("无效输入，请按1或2！")
            continue

def password_generate():
    password=(f"{choice(uppercase)}{choice(lowercase)}{choice(lowercase)}{choice(digits)}{choice(digits)}{choice(digits)}{choice(digits)}{choice(symbols)}")
    print(password)

def main():
    password = function_choice()
    
if __name__=="__main__":
    main()
