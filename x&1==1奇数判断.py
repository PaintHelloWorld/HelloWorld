while True:
    try:
        user_input=int(input("请输入一个整数："))
        if user_input&1==1:
            print("这是一个奇数。")
        else:
            print("这是一个偶数。")
    except ValueError:
        print("请输入整数！")
