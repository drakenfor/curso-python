from tkinter import ttk
from tkinter import *

def validator(text1, text2, d):

    print(text1, text2)

    if len(text2) > 0:
        if text2[0] == '0' and text1 == '0':
            print(True)
            return False
    
    if len(text2) == 0 and text1 == '.':
        return False
    elif '.' in text2 and d =='1':
        if text1 == '.':
            return False;

    
    return text1.isdecimal() or text1 == '.'
    

root = Tk()
root.config(bg='#121212')
root.geometry('500x500')
area = StringVar()
area.set(0)

entry = ttk.Entry(
    validate='key',
    validatecommand=(root.register(validator),'%S', '%s', '%d'),
    textvariable=area
)
entry.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()