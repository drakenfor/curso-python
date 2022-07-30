from tkinter import *
from tkinter import ttk
from unittest import result
from matplotlib.pyplot import grid

from traitlets import Int

# Calcular area
def area(*args):
    result.set(float(base.get()) * float(height.get()))

# Raiz
root = Tk()
root.title('Calcular el area')

main_frame = ttk.Frame(root, padding="12 12 12 12")

main_frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)

# Para la base
base = StringVar()
base_entry = ttk.Entry(main_frame, width=10, textvariable=base)
base_entry.grid(column=2, row=1, sticky=(W, E))

base_label = ttk.Label(main_frame, text='Base: ')
base_label.grid(column=2, row=0, sticky=(W, E))

# Para la altura 
height = StringVar()
height_entry = ttk.Entry(main_frame, width=10, textvariable=height)
height_entry.grid(column=3, row=1, sticky=(W, E))

height_label = ttk.Label(main_frame, text='Altura: ')
height_label.grid(column=3, row=0, sticky=(W, E))

# Boton para calcular
btn = ttk.Button(main_frame, text='Calcular', command=area)
btn.grid(column=3, row=3)

print(root.children)

# Variable resultado
result = StringVar(value='Resultado')
label_result = ttk.Label(main_frame, textvariable=result)
label_result.grid(column=1, row=2)

# Mandarlo a ejecutar
root.mainloop()