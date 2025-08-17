from time import sleep
from time import perf_counter
from random import randint
cheat_count=0
print("========反应速度测试========")
print()
sleep(2)
print("======人类反应时间参考======")
sleep(1)
print("       超常反应：80-120ms")
sleep(1)
print("       电竞选手：120-160ms")
sleep(1)
print("         正常人：160-250ms")
sleep(1)
print("  疲劳/轻度分心：250-350ms")
sleep(1)
print("       睡眠不足：350-500ms")
sleep(1)
print("脑损伤/药物作用：500ms以上")
sleep(3)
print()
print("==========游戏规则==========")
sleep(2)
print("1.看到“\u26A1”符号后，尽可能快速按下回车！")
sleep(2)
print("2.只能按一次哦，而且不要疯狂敲击回车！")
sleep(2)

print("3.看明白了的话，现在先按下回车，启动测试...")
while True:
    input()

    print("请等待...")
    sleep(randint(1,10))
    print("\u26A1")

    start=perf_counter()
    input()
    end=perf_counter()
    reaction_time=(end-start)*1000
    sleep(0.3)
        
    print(f"你的反应时间：{reaction_time:.1f}毫秒")
    sleep(1)
    print("按下回车可重新测试（或按下ctrl+c退出）！")

    
    if reaction_time<80:
        print("只能按一次哦，而且不要疯狂敲击回车！")
        cheat_count+=1
        if cheat_count>=3:
            print("检测到多次异常输入，程序强制退出！")
            sleep(3)
            exit()
            
  

            
        

