from math import log10

print("Welcome to pH calculator!")

while True:
    user_input=input("请输入氢离子浓度（以mol/L计）:")

    try:

        concentration=float(user_input)

        if concentration<0:
            print("你家氢离子浓度是负数啊？？？")
        
        elif concentration==0:
            print("没有氢离子，你测什么pH？回家吧孩子回家吧")
        
        elif concentration>0:
            ph=-log10(concentration)
            ph_str=f"{ph:.2f}".replace("-0.00","0.00")
            print(f"该溶液的pH值为{ph_str}。")

    except ValueError:
        print("请输入正常的阿拉伯数字！别乱打字呜呜呜")
    print()
