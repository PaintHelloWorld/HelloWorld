from random import choice

choices=["\u270A","\u270B","\u270C"]

while True:
    print("按下回车，让电脑和你猜拳~")
    input()
    print(choice(choices))
