from time import sleep

wait_time=1
wait_time2=3

def welcome():
    print("欢迎使用BMI计算器！")
    sleep(wait_time)
    print("此代码为lfw在学习python的第9天所写，现在是15:40，我终于学会了return！！！")
    sleep(wait_time2)
    print()
    return None

def wait_and_print():
    sleep(wait_time)
    print()

def user_input():
    while True:
        try:
            weight=float(input("请输入体重（kg）：").strip())
            if weight==0:
                print("您是电场，磁场，或者静止的光子吗？（请重新输入。）")
                wait_and_print()
                continue
            if weight<0:
                print("您是负物质吗？（请重新输入。）")
                wait_and_print()
                continue
            if weight>1000:
                print("您是小行星吗？（请重新输入。）")
                wait_and_print()
                continue
            
            height=float(input("请输入身高（cm）：").strip())
            if height==0:
                print("您是二维生物吗？（请重新输入。）")
                wait_and_print()
                continue
            if height<0:
                print("您要钻入地球内部吗？（请重新输入。）")
                wait_and_print()
                continue
            if height>300:
                print("您要是去扣篮，绝不可能失败！（请重新输入。）")
                wait_and_print()
                continue
            
            return weight,height

        except ValueError:
            print("无效输入，请重新输入！")
            wait_and_print()
            continue

def calculation(weight,height):
    BMI=10000*weight/(height*height)
    return BMI

def classify_BMI(BMI,weight,height):
    if BMI<18.5:
        category="偏低"
        delta_m=((height*height)*24/10000)-weight
    elif 18.5<=BMI<24:
        category="正常"
        delta_m=0
    elif 24<=BMI<28:
        category="偏重"
        delta_m=weight-((height*height)*24/10000)
    else:
        category="肥胖"
        delta_m=weight-((height*height)*24/10000)
    print(f"您的BMI是{BMI:.2f}，属于{category}类型，离正常标准还有{delta_m:.2f}kg。")
    wait_and_print()
    return category,delta_m

def main():
    welcome()
    while True:
        weight,height=user_input()
        BMI=calculation(weight,height)
        category,delta_m=classify_BMI(BMI,weight,height)
        user_choice=input("输入回车继续计算，输入任意键退出。")
        if user_choice=="":
            print()
            continue
        else:
            break

if __name__=="__main__":
    main()
