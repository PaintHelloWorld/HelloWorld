from time import sleep
waiting_time=1.5
def wait():
    print()
    sleep(waiting_time)
def generate_fibonacci():
    while True:
        try:
            length=int(input("请输入你想斐波那契数列位数，输入0退出："))
            if length<0:
                print("你家数列有负数项啊？？？")
                wait()
                continue
            elif length==0:
                break
            elif length<=3:
                print("前3位是1,1,2。1+1=2你不知道？回家吧孩子回家吧")
                wait()
                continue
            elif length>100:
                print("你用得了那么多吗？")
                wait()
                continue
            a,b=1,1
            print(f"前{length}项为：")
            for i in range(1,length+1,1):
                a,b=b,a+b
                if i ==length:
                    print(a)
                else:
                    print(a,end=",")
            wait()
        except ValueError:
            print("请输入正整数！")
            wait()
def main():
    generate_fibonacci()
if __name__=="__main__":
    main()
            
                    
