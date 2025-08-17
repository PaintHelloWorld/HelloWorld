from time import sleep

wait_time=1

def error_hint():
    print("请输入有效数字！")
    print()
    sleep(wait_time)

def user_input():
    while True:
        
        try:
            c1=float(input("请输入溶液1的浓度（mol/L）："))
            if c1<=0:
                error_hint()
                continue
        except ValueError:
            error_hint()
            continue
            
        try:
            v1=float(input("请输入溶液1的体积（L）："))
            if v1<=0:
                error_hint()
                continue
        except ValueError:
            error_hint()
            continue
            
        try:
            c2=float(input("请输入溶液2的浓度（mol/L）："))
            if c2<=0:
                error_hint()
                continue
        except ValueError:
            error_hint()
            continue
            
        try:
            v2=float(input("请输入溶液2的体积（L）："))
            if v2<=0:
                error_hint()
                continue
        except ValueError:
            error_hint()
            continue
            
        return c1,v1,c2,v2

def calculation(c1,v1,c2,v2):
    n_total=c1*v1+c2*v2
    v_total=v1+v2
    c_final=n_total/v_total
    print(f"混合后浓度：{c_final:.4f}mol/L。")
    print()
    sleep(wait_time) 
    return c_final,v1,v2

def dilution_or_not(c_final,v1,v2):
    while True:
        c_target=input("若要继续稀释，请输入目标浓度，否则输入N：")
        if c_target.upper()=="N":
            break
        else:
            try:
                c_target=float(c_target)
                if c_target >= c_final:
                    print("计算失败！目标浓度应小于稀释浓度，请重新输入！")
                    print()
                    sleep(wait_time)
                    continue
                else:
                    water=(c_final*(v1+v2)/c_target)-(v1+v2)
                    print(f"应加水{water:.4f}L，最终体积为{water+v1+v2:.4f}L。")
                    print()
                    sleep(wait_time)
                    break
            except (ValueError,ZeroDivisionError):
                error_hint()
                continue
            
def main():
    print("欢迎使用混合溶液浓度计算器！")
    sleep(wait_time)
    print("此代码（足足103行！！！）为lfw学习python的第8天所写，现在是19:00，lfw很开心！")
    print()
    sleep(wait_time)
    while True:
        print("======新一轮计算======")
        sleep(wait_time)
        c1,v1,c2,v2=user_input()
        c_final,v1,v2=calculation(c1,v1,c2,v2)
        dilution_or_not(c_final,v1,v2)
        user_choice=input("按回车继续计算，输入任意键退出。")
        print()
        if user_choice.upper()=="":
            continue
        else:
            break
            
if __name__=="__main__":
    main()
