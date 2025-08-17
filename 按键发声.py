from winsound import Beep
from msvcrt import getch
from threading import Thread

notes={b"1":262, b"2":294, b"3":330, b"4":349, \
       b"5":392, b"6":440, b"7":494, b"8":523}

def play_sound(frequency,duration):
    Thread(target=Beep,args=(frequency,duration)).start()

def key_beep():
    print("按1~8发声......")
    while True:
        key=getch()
        if key in notes:
            play_sound(notes[key],500)

if __name__=="__main__":
    key_beep()
