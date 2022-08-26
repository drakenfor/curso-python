from tkinter import *
from tkinter import ttk

root = Tk()
globals().update({'my': StringVar()})
ttk.Entry(root, textvariable=my).pack()


my.trace('w', lambda *args: print(args[0]))
root.mainloop()