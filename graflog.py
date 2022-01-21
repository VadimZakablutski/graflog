from tkinter import*
user=loe_failist_listisse("users.txt")
passw=loe_failist_listisse("passwords.txt")
passw=passauto()
def lg():
	user=user_entry.get()
	passw=passw_entry.get()

log=Tk()
Label(text="Логин:").grid(row=0,column=0)
login=Entry(width=30)
login.grid(row=0,column=1,columnspan=3)
Label(text="Пароль:").grid(row=1,column=0)
psw=Entry(width=30)
psw.grid(row=1,column=1,columnspan=3)
Button(text="Регистрация",width=10).grid(row=2,column=0)
Button(text="Вход",width=20,command=lg).grid(row=2,column=3)






log.mainloop()