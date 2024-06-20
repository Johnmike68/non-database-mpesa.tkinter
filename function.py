from tkinter import * 
from tkinter import messagebox

def withdraw():
    withdraw = Tk()
    withdraw.geometry("400x600")
    withdraw.title("withdraw")
    withdraw.config(bg="green")

    top = Frame(withdraw,bg="green")
    top.pack(side="top")
    bottom = Frame(withdraw,bg="green")
    bottom.pack(side="top")
    between = Frame(withdraw,bg="green")
    between.pack(side="top")

    tpo = Label(top,font=60,text="withdraw",bg="green")
    tpo.grid(column=2,row=1)

    ent = Entry(bottom,width=60)
    ent.pack()
   
    
    def okey():
        amount = ent.get()
        if (amount > "2000"):
            ent.delete(0,END)
            ent.insert(0,"to much to withdraw!!!")
        elif(amount <"2000"):
            ent.delete(0,END)
            ans = (2000 - int(amount))
            ent.insert(0,f"{str(ans)} is your balance")
        else:
            ent.delete(0,END)
            ent.insert(0,"value entered is incorrect")

    def cancel():
        ent.delete(0,END)
        
    ok = Button(between,text="okay",padx=40,pady=20,command= okey )
    cancel = Button(between,text="cancel",padx=40,pady=20,command= cancel)
    cancel.grid(column=0,row=0)
    ok.grid(column=3,row=0)
    withdraw.mainloop()


def deposit():
    deposit = Tk()
    deposit.geometry("400x600")
    deposit.title("deposit")
    deposit.config(bg="green")

    top = Frame(deposit,bg="green")
    top.pack(side="top")
    bottom = Frame(deposit,bg="green")
    bottom.pack(side="top")
    between = Frame(deposit,bg="green")
    between.pack(side="top")

    tpo = Label(top,font=60,text="deposit",bg="green")
    tpo.grid(column=2,row=1)

    ent = Entry(bottom,width=60)
    ent.pack()
   
    
    def okey():
        amount = ent.get()
        if (amount<="0"):
            ent.delete(0,END)
            ent.insert(0,"to low to deposit!!!")
        elif(amount>"0"):
            ent.delete(0,END)
            ans = (2000 + int(amount))
            ent.insert(0,f"{str(ans)} is your balance")
        else:
            ent.delete(0,END)
            ent.insert(0,"value entered is incorrect")

    def cancel():
        ent.delete(0,END)
        
    ok = Button(between,text="okay",padx=40,pady=20,command= okey )
    cancel = Button(between,text="cancel",padx=40,pady=20,command= cancel)
    cancel.grid(column=0,row=0)
    ok.grid(column=3,row=0)
    deposit.mainloop()

def check_bal():
    check_bal = Tk()
    check_bal.geometry("400x600")
    check_bal
    check_bal.title("check_bal")
    check_bal.config(bg="green")

    top = Frame(check_bal,bg="green")
    top.pack(side="top")
    bottom = Frame(check_bal,bg="green")
    bottom.pack(side="top")
    between = Frame(check_bal,bg="green")
    between.pack(side="top")

    tpo = Label(top,font=60,text="check_bal",bg="green")
    tpo.grid(column=2,row=1)

    ent = Entry(bottom,width=60)
    ent.pack()
   
    
    def okey():
        ent.delete(0,END)
        ent.insert(0,f"your mpesa is ksh 2000")
        

    def cancel():
        ent.delete(0,END)
        
    ok = Button(between,text="okay",padx=40,pady=20,command= okey )
    cancel = Button(between,text="cancel",padx=40,pady=20,command= cancel)
    cancel.grid(column=0,row=0)
    ok.grid(column=3,row=0)


    check_bal.mainloop()



def accInfo():
    accInfo = Tk()
    accInfo.geometry("400x600")
    accInfo
    accInfo.title("accInfo")
    accInfo.config(bg="green")

    top = Frame(accInfo,bg="green")
    top.pack(side="top")
    bottom = Frame(accInfo,bg="green")
    bottom.pack(side="top")
    between = Frame(accInfo,bg="green")
    between.pack(side="top")

    tpo = Label(top,font=60,text="accInfo",bg="green")
    tpo.grid(column=2,row=1)

    ent = Entry(bottom,width=60)
    ent.pack()
   
    
    def okey():
        ent.delete(0,END)
        ent.insert(0,f"your mpesa balance is is ksh 2000")
        

    def cancel():
        ent.delete(0,END)
        
    ok = Button(between,text="okay",padx=40,pady=20,command= okey )
    cancel = Button(between,text="cancel",padx=40,pady=20,command= cancel)
    cancel.grid(column=0,row=0)
    ok.grid(column=3,row=0)


    accInfo.mainloop()

def exit():
    egcit = Tk()
    egcit.geometry("400x600")
    egcit
    egcit.title("exit")
    egcit.config(bg="green")

    top = Frame(egcit,bg="green")
    top.pack(side="top")
    """
    bottom = Frame(egcit,bg="green")
    bottom.pack(side="top")
    between = Frame(egcit,bg="green")
    between.pack(side="top")
"""
    tpo = Label(top,font=60,text="thanks for using our services!!",bg="green")
    tpo.grid(column=2,row=1)

    egcit.mainloop()
"""
    ent = Entry(bottom,width=60)
    ent.pack()
   
    
    def okey():
        ent.delete(0,END)
        ent.insert(0,f"your mpesa balance is is ksh 2000")
        

    def cancel():
        ent.delete(0,END)
        
    ok = Button(between,text="okay",padx=40,pady=20,command= okey )
    cancel = Button(between,text="cancel",padx=40,pady=20,command= cancel)
    cancel.grid(column=0,row=0)
    ok.grid(column=3,row=0)
"""

    



