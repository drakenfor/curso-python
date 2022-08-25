import math
import re
from tkinter import *
from tkinter import ttk


# Eliminar letras
def validator(text1, text2, d, new_text):

    print(text1, text2, new_text)

    if len(text2) > 1:
        if text2[0] == '0' and text1 == '0' and text2[1] != '.':
            print(True)
            return False
    
    if '.' in text2 and d =='1':
        if text1 == '.':
            return False;

    
    return text1.isdecimal() or text1 == '.'

def validator_sv(*args):

    i = int(args[0][-1])

    if len(variables[i].get()) > 1:
        if variables[i].get()[0] == '0' and variables[i].get()[1] != '.':
            variables[i].set(variables[i].get()[1:])
            
    if len(variables[i].get()) > 1:
        variables[i].set(re.sub(r'^0+', '', variables[i].get()))
    #     if '.' == variables[i].get()[0]:
    #         variables[i].set('0' + variables[i].get())


def cal(*args):
    pass

root = Tk()
# TODO: Poner un titulo apropiado
root.title('Equipos')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

########## Tabs ##########
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, sticky='nwe')

########## Tab: production-drill##########
production = ttk.Frame(notebook)
notebook.add(production, text='Production Drill')
production.columnconfigure(0, weight=1)
production.rowconfigure(0, weight=1)

ttk.Label(
        production,
        text='Physical Development parameters',
        font=('Arial', 12),
    ).grid(row=0, column=0, sticky='nw')


iFrame = ttk.Frame(production)
iFrame.grid(row=1, column=0, sticky='nwe')
iFrame.columnconfigure(0, weight=1)
iFrame.rowconfigure(0, weight=1)

entries = [
    'Bench Area (m)',
    'Bench Height (m)',
    'Rock density (m)',
    'Burden (m)',
    'Space, (m)',
    'Hole depth, (m)',
    'Sub-drilling, %', 
    ]

def calc_production(*args):
    # Volumen
    validator_sv(*args)
    try:
        results[0][1].set(
            round(float(variables[0].get()) * float(variables[1].get()),2)
        )
    except:
        results[0][1].set(0)

    try:
        
        results[1][1].set(
            round(float(results[0][1].get()) * float(variables[2].get()), 2)
        )
    except:
        results[1][1].set(0)
    

    try:
        results[2][1].set(
            round(float(variables[-2].get()) + float(variables[-2].get()) * float(variables[-1].get()) / 100, 2)
        )
    except:
        results[2][1].set(0)

    try:
        vol = float(results[0][1].get())
        burden = float(variables[3].get())
        space = float(variables[4].get())
        hole = float(variables[5].get())

        results[3][1].set(math.ceil( vol/(burden * space * hole)))
    except:
        results[3][1].set(0)

    try:
        results[4][1].set(round(float(results[2][1].get()) * float(results[3][1].get()), 2))
    except:
        results[4][1].set(0)

variables = []
for i, entry in enumerate(entries):
    variables.append(StringVar())
    variables[i].trace('w', calc_production)
    ttk.Entry(
            iFrame,
            justify=RIGHT,
            validate='key',
            textvariable=variables[i],
            validatecommand=(root.register(validator), "%S", "%s", "%d", "%P"),
            width=20
        ).grid(row=i, column=2, sticky='nw')
    ttk.Label(iFrame, text=entry + ': ').grid(row=i, column=0, pady=5, padx=5, sticky='nw')

oFrame = ttk.Frame(production)
oFrame.grid(row=1, column=2, sticky='nwe', padx=20)
oFrame.columnconfigure(0, weight=1)
oFrame.rowconfigure(0, weight=1)

### ounts ###
outs = [
    'Volumen, (m3)',
    'Metric Tons, (t)',
    'Total hole depth, (m)',
    'Number of production holes',
    '9 7/8" diameters holes, meters drilled, (m)'
]



results = [(out, StringVar()) for out in outs]

for i, out in enumerate(outs):
    ttk.Label(
        oFrame,
        text = out + ': ',

    ).grid(row=i, column=0, pady=5, sticky='w')

    ttk.Label(oFrame, textvariable=results[i][1]).grid(row=i, column=1, sticky='e')



######### Tab-End: production-drill#########

######### Tab: Shovel ##############
shovel = ttk.Frame(notebook)
notebook.add(shovel, text='Shovel')

######### Tab: Truck ############## truck = ttk.Frame(notebook)
truck = ttk.Frame(notebook)
notebook.add(truck, text='Truck')


####################
root.mainloop()