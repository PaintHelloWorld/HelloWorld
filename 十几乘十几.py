from random import randint
from time import sleep

wait_time1=0.3

def generate_question():
        num1=randint(10,20)
        num2=randint(10,20)
        question=f"{num1}*{num2}=?"
        answer=num1*num2
        return question,answer  #返回这个question字符串和answer整数

def main():
    generate_question()
    print("欢迎来到十几乘十几速算挑战！")
    sleep(wait_time1)

while True:
    question,answer=generate_question() #接受line 11 return返回的值，并调用line 6 定义的generate_question()函数
    print(question)

    while True:
        try:
            user_input=int(input("请输入答案："))
            if user_input==answer:
                print("回答正确！")
                print()
                sleep(wait_time1)
                break
            else:
                print("回答错误！")
                sleep(wait_time1)
        except ValueError:
            print("请输入有效数字！")
            
if __name__=="__main__":
    main()
