#导入random和tkinter模块
import random
from tkinter import Tk,Label
#创建窗口
game=Tk()
game.geometry("150x75")
game.overrideredirect(True)
#定义逃跑函数，设定随机范围
def flee(e):
    game.geometry(f"+{random.randint(0,1500)}+{random.randint(0,800)}")
#将鼠标进入（enter）与逃跑绑定  
game.bind("<Enter>",flee)
#在弹窗内注入文字，并使其居中
Label(game,text="抓我呀\n来抓我呀").pack(expand=True)
#游戏循环
game.mainloop()
