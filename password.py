from random import choice
import string

def generate_password():
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits=string.digits
    symbols=["!","@","#","$","%","^","&","*","(",")","_","+","<",\
             ">","?",":","-","=",";",",",".","/","~","|","\\","`"]
    password=[choice(lowercase),choice(uppercase),choice(digits),\
              choice(symbols)]
    print(f"{choice(lowercase)}{choice(uppercase)}{choice(digits)}\
{choice(symbols)}")

def main():
    while True:
        generate_password()
        input("按下回车换一个")

if __name__=="__main__":
    main()
