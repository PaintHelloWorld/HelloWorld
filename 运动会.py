import random
import time

#确定不在抽签范围的学号
excluded_numbers = [] 


numbers = [num for num in range(1, 32) if num not in excluded_numbers]

selected_numbers = random.sample(numbers, 14)

print("正在抽取14个神秘数字...")
time.sleep(1.5)


print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)

print("\n随机选择的14个不重复数字:")
for i, num in enumerate(selected_numbers, 1):
    print(f"第{i}个数字: {num}")
    time.sleep(0.3)

print("\n抽取完成！")

input("按回车（enter）退出")
