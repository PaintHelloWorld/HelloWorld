def get_user_input():
    while True:
        try:
            i=int(input('请输入最后一项的幂指数：'))
            if i<1:
                print("请输入大于零的数字！")
                continue
            return i
        except ValueError:
            print("请输入大于零的数字！")
            continue

def calculation(i):
    print(f'从 2的1次幂 到 {i}次幂 是:')
    for power in range(1,i+1,1):
        print(2**power)

def main():
    while True:
        print("======新一轮计算======")
        i = get_user_input()
        calculation(i)
        while True:
            choice = input("按Y继续，按N退出。").upper()
            if choice not in ["Y","N"]:
                print("无效输入，请重新输入。")
                continue
            if choice == "Y":
                break
            if choice =="N":
                return

if __name__=="__main__":
    main()
