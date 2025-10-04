from tkinter import Tk,Label
import random
import threading
import winsound


def blessing():
    def play_sound():
        time = 1000
        try:
            winsound.Beep(261,time)
            winsound.Beep(330,time)
            winsound.Beep(392,time)
            winsound.Beep(523,time)
        except:
            pass

    threading.Thread(target=play_sound).start()
    game = Tk()
    window_width = 300
    window_height = 300
    screen_width = game.winfo_screenwidth()
    screen_height = game.winfo_screenheight()
    x = (screen_width - window_width)//2
    y = (screen_height - window_height)//2
    game.geometry(f"{window_width}x{window_height}+{x}+{y}")
    game.title("代码跑通了!!!")
    Label(game,text = "运行成功!\n芜湖!",font = ("微软雅黑",44)).pack(expand = True)
    game.mainloop()

blessing()
