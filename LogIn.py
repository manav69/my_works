
from tkinter import *
import time



def LogIn():
    def refresh():
        frame.destroy()
    def matchLogIn():
        file = open("D:/Sublime Text 3/Login.txt", "r")
        un = e.get()
        p = e1.get()
        arrayofnames = file.readlines()
        c = 0
        for items in arrayofnames:
            g = items.find('$')
            f = items.find('$', g + 1)
            h = items.find('$', f + 1)
            uunn = items[g + 1:f]
            pp = items[f + 1:h]
            if un == uunn and pp == p:
                c = c + 1
                Label(window,text="Welcome "+items[0:g],font=("Arial",20),width=30,height=2,bg="black",fg="white",borderwidth=5).pack( anchor='center')

        if c == 0:
            Label(window,text="USER NOT FOUND",font=('arial',20),width=30,height=2,bg='black',fg='white').pack(anchor="center")

        file.close()
        refresh()
    frame=Frame(window)
    frame.pack(side=LEFT)
    Label(frame,text="User_Name: ").pack(anchor='nw')
    e =Entry(frame)
    e.pack(anchor='nw')
    Label(frame,text="Password: ").pack(anchor='nw')
    e1 =Entry(frame)
    e1.pack(anchor='nw')
    Button(frame,text="LogIn",command=matchLogIn).pack(anchor='nw')

def SignIn():
    def refresh():
        frame.destroy()


    def createnewacc():
        file = open("D:/Sublime Text 3/Login.txt", "a")
        n = e2.get()
        un = e3.get()
        p = e4.get()
        file.write(n + "$" + un + "$" + p + "$\n")
        Label(window,text="Account Has Been Created",font=("Arial",20),width=30,height=2,bg="black",fg="white",borderwidth=5).pack(anchor='center')
        file.close()
        refresh()
    frame=Frame(window)
    frame.pack(side=LEFT)
    Label(frame,text="Name: ").pack(anchor='nw')
    e2=Entry(frame)
    e2.pack(anchor='nw')
    Label(frame,text="User_Name: ").pack(anchor='nw')
    e3=Entry(frame)
    e3.pack(anchor='nw')
    Label(frame,text="Password: ").pack(anchor='nw')
    e4=Entry(frame)
    e4.pack(anchor='nw')
    Button(frame,text="SignIn",command=createnewacc).pack(anchor='nw')




def main():
    window.title("LogIn")
    window.geometry("500x400")
    button_quit=Button(window,text="Exit",command=window.quit)
    Label(window,text="Welcome to the LogIn Window",font=("Arial",20),width=30,height=2,bg="black",fg="white",borderwidth=5).pack()

    button1=Button(window,text="Have a Account",width=15,command=LogIn)
    button2=Button(window,text="Create a new Account",width=20,command=SignIn)
    button1.pack()
    button2.pack()
    button_quit.pack(anchor='s')
    window.mainloop()
window=Tk()

main()




