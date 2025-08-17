print("请输入密码，您有三次尝试机会！")
from time import sleep

attempts=1
while attempts<=3:
    password=input(f"第{attempts}次尝试，请输入您的密码：")
    
    if password=="the world owner":
       print("欢迎回家，世界的主人！")
       sleep(5)
       break
    else:
        print(f"密码错误，这已经是您第{attempts}次尝试。大楼已经启动自毁程序！")
        attempts=attempts+1
        
    if attempts>3:
        print("您已错误三次，5秒后大楼崩塌！")
        sleep(5)
        break
       
