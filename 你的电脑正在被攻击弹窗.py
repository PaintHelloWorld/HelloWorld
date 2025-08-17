from tkinter import messagebox
from time import sleep
def limitless_errorbox():
    messagebox.showerror("你这个穷鬼！","我要把你电脑卡死机！")
    while True:
        messagebox.showwarning("Windows错误","你的电脑正在被攻击")
        sleep(1)
def main():
    messagebox.showerror("Windows错误","你的电脑正在被攻击")
    messagebox.showinfo("开玩笑的","这只是机主lfw的恶搞代码~")
    sleep(2)
    messagebox.showwarning("但是呀","你怎么知道上个弹窗不是攻击的一部分呢？")
    messagebox.showinfo("系统提示","花费888元即可清除病毒，并成为机主的关门弟子！")
    choice1=messagebox.askyesno("机主已经破解了你的支付密码，建议乖乖投降","是否支付？")
    if choice1:
        messagebox.showinfo("你做出了正确的选择！","支付处理中...")
        messagebox.showinfo("系统提示","支付成功！")
        choice2=messagebox.askyesno("你的支付密码在我手里哦~","是否再支付8888元升级lfw病毒清理大师VIP？")
        if choice2:
            messagebox.showinfo("系统提示","支付成功！")
            messagebox.showinfo("系统提示","祝您生活愉快！")
        else:
            limitless_errorbox()
    else:
        limitless_errorbox()

if __name__=="__main__":
    main()
    
