# # from tkinter import *
# #
# # win = Tk()
# # win.geometry("300x400+800+300")
# #
# # head = Frame(win, width=300, height=100)
# # head.grid(row=0, column=0)
# #
# # lb = Label(head, text="hello pls submit")
# # lb.place(x=50, y=45)
# #
# # contain = Frame(win, width=300, height=250)
# # contain.grid(row=1, column=0)
# #
# # lb3 = Label(contain, text="password")
# # lb3.place(x=30, y=30)
# #
# # et = StringVar()
# #
# # enPass = Entry(contain, textvariable=et)
# # enPass.place(x=120, y=30)
# #
# # chint = IntVar()
# # Checkbutton(contain, text="OK", variable=chint).place(x=120, y=60)
# #
# # contain2 = Frame(win, width=300, height=250)
# #
# # def clear():
# #     et.set("")
# #
# # def sub():
# #     if enPass.get() == "456":
# #         if chint.get() == 1:
# #             contain.grid_forget()
# #             contain2.grid(row=1, column=0)
# #         else:
# #             et.set("please check box")
# #
# #     win.after(2000, clear)
# #
# # Button(contain, text="Submit", command=sub).place(x=120, y=100)
# #
# # win.mainloop()
# #
#
#
# # from matplotlib.pyplot import title
# # from tkinter import *
# # win= Tk()
# # win.geometry("400x500+600+300")
# # win.title("Login App")
# # head= Frame(win,width=400,height=200,bg="black")
# # head.grid(row=0,column=0)
# # contain= Frame(win,width=400,height=250,bg="green")
# # contain.grid(row=1,column=0)
# # foot= Frame(win,width=400,height=100,bg="blue")
# # foot.grid(row=2,column=0)
# # title= Label(head,text="Login",fg="white",bg="black",font=("Arial",20))
# # title.place(x=100,y=50)
# # l1= Label(contain,text="Username",bg="green")
# # l1.place(x=50,y=50)
# # l2=Label(contain,text="password",bg="green")
# # l2.place(x=50,y=80)
# # e1= Entry(contain)
# # e1.place(x=120,y=60)
# # e2= Entry(contain,show="*")
# # e2.place(x=120,y=90)
# # def check():
# #     if e1.get()=="Jigar" and e2.get()=="100100":
# #      print("YUY")
# #     else:
# #      print("Try again")
# # btn = Button(contain,text="Login",command=check)
# # btn.place(x=150,y=160)
# # win.mainloop()
#
# from tkinter import *
# win = Tk()
# win.geometry("200x400+300+300")
# lb = Label(win, text="Hello World")
# lb.pack()
# def f(event):
#     lb.config(bg="yellow")
#     print(event.x, event.y, ",", event.x_root, ",", event.y_root)
# def f1(event):
#     lb.config(bg="#fff")
# lb.bind("<Enter>", f)
# lb.bind("<Leave>", f1)
# def f2(event):
#     # if event.keysym == "Shift_L" or event.keysym == "Shift_R":
#     #     pass
#     # else:
#     #     print(event.keysym_num)
#
#     if (event.keysym_num >=97 and event.keysym_num <= 122) or (event.keysym_num >= 65 and event.keysym_num <= 90) :
#         print(event.keysym)
#     else:
#         en.delete(len(en.get() - 1), END)
#
# # win.bind("<Key>", f2)
#
#
# en = Entry(win)
# en.pack()
# en.bind("<key>", f2)
# def f3():
#     en.delete(len(en.get()-1), END)
# button = Button(win, text="Click Me", command=f3)
#
# win.mainloop()

from tkinter import *
from tkinter import messagebox
win = Tk()

def f():
    messagebox.showerror("Error", "Error")

bt = Button(text="click", command=f)
bt.pack()
mainloop()
