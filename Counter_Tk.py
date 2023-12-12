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

def Plus(x):
    num = count.get()
    count.delete(0, END)
    count.insert(0, int(num)+x)      # type: ignore
     # type: ignore

def Minus(x):
    num = count.get()
    count.delete(0, END)
    count.insert(0, int(num)-x)      # type: ignore

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

minus1 = ttk.Button(fcenter, text = "-", width=3,style="C.TButton", command = lambda:Minus(1))
tk.bind('-', lambda _:Minus(1))
minus5 = ttk.Button(fcenter, text = "-5", width=3, command = lambda:Minus(5))
tk.bind('<Control-minus>', lambda _:Minus(5))

plus1 = ttk.Button(fcenter, text="+", width=3, command = lambda:Plus(1))
tk.bind('+', lambda _:Plus(1))
plus5 = ttk.Button(fcenter, text="+5", width=3, command = lambda:Plus(5))
tk.bind('<Control-+>', lambda _:Plus(5))

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
