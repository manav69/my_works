from tkinter import *
from time import strftime
from datetime import datetime
window=Tk()
window.title("CLOCK")


def time():
    STRING=strftime('%H:%M:%S %p')
    label.config(text=STRING)
    label.after(1000,time)
label=Label(window,font=("arial",80),bg='black',fg='cyan')
label.pack(anchor='center')
time()
window.mainloop()
