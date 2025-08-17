from time import sleep
waiting_time1=1
print("欢迎使用吉布斯自由能计算器！")
sleep(waiting_time1)
def gibbs_calculation():
    while True:
        T=input("请输入温度（若要默认278K，直接回车即可）：")
        if T=="":
            T=278
            break
        else:
            try:
                T=float(T)
                break
            except ValueError:
                print("请你好好打字...")
                
    while True:
        try:
            H=float(input("请输入焓变（KJ/mol）："))
            if H==0:
                print("好家伙，焓变=0？你给我重来...")
                sleep(waiting_time1)
                continue
            break
        except ValueError:
           print("请你好好打字...")
           sleep(waiting_time1)
    while True:
        try:
            S=float(input("请输入熵变[J/（mol*K）]："))
            if S==0:
                print("好家伙，焓变=0？你给我重来...")
                sleep(waiting_time1)
                continue
            break
        except ValueError:
            print("请你好好打字...")
            sleep(waiting_time1)
    G=H-T*(S/1000)
    print(f"deltaG={G}")
    sleep(waiting_time1)
    if G>0:
        print("该反应不可自发进行。")
    elif G<0:
        print("该反应可自发进行。")
    else:
        print("该反应已平衡。")
    sleep(waiting_time1)
    input("按回车继续计算~")
    print()
def main():
    while True:
        gibbs_calculation()
if __name__=="__main__":
    main()
