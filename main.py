from tkinter import *
from function import *

root = Tk()
root.title("mpesa")
root.geometry("400x600")
root.config(bg="green")

top = Frame(root)
top.pack(side="top")

bottom = Frame(root,bg="green")
bottom.pack(side="top")


title = Label(top,font=("calibri",50,"bold"),text="mpesa",padx=40,pady=5,bg="green")
deposit = Button(bottom,font=("Harlow Solid Italic",30),text="deposit",padx=90,pady=5,bg="green",command= deposit)
withdraw = Button(bottom,font=("Harlow Solid Italic",30),text="withdraw",padx=70,pady=5,bg="green",command= withdraw)
check = Button(bottom,font=("Harlow Solid Italic",30),text="check balance",padx=40,pady=5,bg="green",command= check_bal)
exiting = Button(bottom,font=("Harlow Solid Italic",30),text="exit",padx=120,pady=5,bg="green",command= exit)
accInfo = Button(bottom,font=("Harlow Solid Italic",30),text="Account info",padx=40,pady=5,bg="green",command= accInfo)


title.pack()
deposit.grid(column=0,row=1)
withdraw.grid(column=0,row=2)
check.grid(column=0,row=3)
accInfo.grid(column=0,row=4)
exiting.grid(column=0,row=5)


root.mainloop()