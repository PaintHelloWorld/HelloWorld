from time import sleep

def main():
    while True:
        try:
            number=float(input("请输入数字："))
            if number>0:
                print("正数")
            elif number<0:
                print("负数")
            else:
                print("0")
        except ValueError:
            print("请输入有效数字")

if __name__=="__main__":
    main()
