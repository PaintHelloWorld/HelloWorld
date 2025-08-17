from time import sleep

wait_time1=1
wait_time2=2

def welcome():
    print("欢迎使用质数搜索器！")
    sleep(wait_time1)
    print("此代码为lfw在学习python的第9天所写，现在是21:10。Cheer for me!!!")
    sleep(wait_time2)
    print()

def error_hint():
    print("请输入正整数！")
    sleep(wait_time1)

def user_input():
    while True:
        try:
            max_num=int(input("请输入你要搜索到几（建议5000以内，除非你的电脑性能很好）："))
            if max_num<=0:
                error_hint()
                sleep(wait_time1)
                continue
            if max_num>100000:
                print("数字太大，小电脑会哭的呜呜呜，换一个10万以内的数字吧！")
                sleep(wait_time1)
                continue
            return max_num
        except ValueError:
            error_hint()
            sleep(wait_time1)
            continue
       
def calculation(max_num):
    primes=[]
    for num in range(2,max_num+1,1):
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            primes.append(num)
    return primes

def print_num(max_num,primes):
    print(f"1到{max_num}的质数为：")
    print(",".join(map(str,primes)))
    sleep(wait_time1)

def main():
    welcome()
    while True:
        max_num=user_input()
        primes=calculation(max_num)
        print_num(max_num,primes)
        user_choice=input("输入回车（或空格）进行下一轮搜索，输入其他任意内容退出程序！").strip()
        if user_choice=="":
            print()
            continue

if __name__=="__main__":
    main()
