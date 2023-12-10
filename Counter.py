import tkinter as tk
from tkinter import *       # type: ignore
from tkinter import ttk

tk = Tk()
tk.title("Counter")
#Blocked window resizing and dark background
tk.resizable(width=False, height=False)
tk.configure(bg='#595959')
ttks = ttk.Style()
ttks.configure("TButton", background='#595959')

def Plus1(event=None):
    num = count.get()
    x = int(num) + 1
    count.delete(0, END)
    count.insert(0, x)      # type: ignore
def Plus5(event=None):
    num = count.get()
    ans = int(num) + 5
    count.delete(0, END)
    count.insert(0, ans)    # type: ignore

def Minus1(event=None):
    num = count.get()
    x = int(num) - 1
    count.delete(0, END)
    count.insert(0, x)      # type: ignore
def Minus5(event=None):
    num = count.get()
    ans = int(num) - 5
    count.delete(0, END)
    count.insert(0, ans)    # type: ignore

def Copy():
    num = count.get()
    tk.clipboard_clear()   # type: ignore
    tk.clipboard_append(num)
def Reset():
    count.delete(0, END)
    count.insert(0, '0') 

#Create window in the center of the screen
screen_width = tk.winfo_screenwidth()
screen_height = tk.winfo_screenheight()
window_width = 220
window_height = 80
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
tk.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

lbl = Label(tk, text = "Counter", background='#595959', foreground='white')
lbl.pack(side=TOP)

#Center buttons
fcenter = Frame(tk)
count = ttk.Entry(fcenter, width=15)
count.insert(END,'0')

minus1 = ttk.Button(fcenter, text = "-", width=3,style="C.TButton", command= Minus1)
tk.bind('-', Minus1)
minus5 = ttk.Button(fcenter, text = "-5", width=3, command = Minus5)
tk.bind('<Control-minus>', Minus5)
plus1 = ttk.Button(fcenter, text="+", width=3, command = Plus1)
tk.bind('+', Plus1)
plus5 = ttk.Button(fcenter, text="+5", width=3, command = Plus5)
tk.bind('<Control-+>', Plus5)

#Bottom buttons
fbottom = Frame(tk)
copy = ttk.Button(fbottom, text= "Copy", command=lambda:Copy())
reset = ttk.Button(fbottom, text= "Reset", command=lambda:Reset())

#Displaying buttons
fcenter.pack()
minus5.pack(side=LEFT)
minus1.pack(side=LEFT)
count.pack(side=LEFT, fill=X, expand=True)
plus1.pack(side=LEFT)
plus5.pack(side=LEFT)

fbottom.pack()
copy.pack(side=LEFT)
reset.pack(side=LEFT)

tk.mainloop()
