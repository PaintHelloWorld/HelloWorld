from time import sleep

total=30
wait_time=0.3

for i in range(total+1):
    bar="▓"*i+"░"*(total-i)
    print(f"\r加载中......{bar}{i*100//total}%",end="")
    sleep(wait_time)
print("加载完成")
