from tkinter import Tk,Label
from time import sleep
from random import randrange
from threading import Thread

def boom():
    game = Tk()
    width = game.winfo_screenwidth()
    height = game.winfo_screenheight()
    a = randrange(0, width)
    b = randrange(0, height)
    game.title('py')
    game.geometry("200x50" + "+" + str(a) + "+" + str(b))
    Label(game,text='python天下第一',width=20, height=4).pack(expand=True)
    game.mainloop()

threads = []
for i in range(100):
    t = Thread(target=boom)
    threads.append(t)
    sleep(0.2)
    threads[i].start()
  
