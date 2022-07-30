

personas = {
    'Volumen (m^3)': 1,
    'Metric tons (t)':3,
    'Total hole depth (m)':3,
    'Number of production holes': '',
    '9 7/8" diameter holes, meters drilled (m)': ''
}

for i in personas:
    print(i)

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Prueba')

fram = ttk.Frame(root, padding="5 5 5 5")
fram.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)

i = 1
for person in personas:

    label = ttk.Label(fram, text=person)
    label.grid(column=1, row=i, sticky=(W, E))
    input = ttk.Entry(fram, text=personas[person])
    input.grid(column=3, row=i, sticky=(W, E))
    i += 1

root.mainloop()