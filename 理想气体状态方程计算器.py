from time import sleep

wait_time1=1
wait_time2=2
wait_time3=3

def user_input():
    
    while True:
        try:
            p=float(input("压强（atm）：")or 0)
            v=float(input("体积（L）：")or 0)
            n=float(input("物质的量（mol）：")or 0)
            r=0.0821#理想气体常数，单位：L*atm/(mol*K)
            t=float(input("温度（注意是K）：")or 0)
            return p,v,n,r,t
        except ValueError:
            print("哎呀，打错字了！没关系，我们重来~")
            print()
            sleep(wait_time1)
            continue

def calculation(p,v,n,r,t):
    
    def negative_result_check():
        if result>0:
            print(f"计算得到的结果：{result:.2f}")
            print()
            return(result)
        else:
            print(f"此结果为{result:.2f}，但无物理意义，别忘了取绝对值哦~")
            print()
            return(result)
        
    unknown_item=sum(x==0 for x in [p,v,n,r,t])

    if unknown_item!=1:
        print("必须提供3个参数，否则无法计算哦，我们重新计算一下吧！")
        print()
        return
    if p==0:
        result=(n*r*t)/v
        negative_result_check()
    elif v==0:
        result=(n*r*t)/p
        negative_result_check()
    elif n==0:
        result=(p*v)/(r*t)
        negative_result_check()
    elif t==0:
        result=(p*v)/(n*r)
        negative_result_check()
    
def main():
    print("欢迎使用lfw的理想气体状态方程计算器！")
    sleep(wait_time1)
    print("此代码为lfw在学习python的第7天所写，\
附加了负负得正的人性化功能（不信的话，可以输入2个负数变量试一试）~")
    sleep(wait_time3)
    print("需提供3个参数（已知量），以计算第4个。")
    sleep(wait_time2)
    print("第4个参数（未知量）直接输入回车或0。")
    print()
    sleep(wait_time2)
    while True:
        p,v,n,r,t=user_input()
        calculation(p,v,n,r,t)
        sleep(wait_time1)
        input("输入回车即可继续计算~")
        print()

if __name__=="__main__":
    main()
