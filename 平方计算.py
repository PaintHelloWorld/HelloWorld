from time import sleep

def user_input():
    while True:
        try:
            end_num=int(input("请输入你想显示到多少个数的平方："))
            if end_num<=0:
                print("无效输入，请重新输入！")
        except ValueError:
                pass
        return end_num

def calculation(end_num):
    for num in range(1,end_num+1,1):
        square_num=num*num
        print(square_num,end=",")

def user_choice():
    user_choice=input("输入0退出，输入其他内容继续计算。")
    return user_choice=="0"

def main():
    while True:
        try:
            num=user_input()
            calculation(num)
            if user_choice():
                break
        except UnboundLocalError:
            print("无效输入，请重新输入！")

if __name__=="__main__":
    main()
