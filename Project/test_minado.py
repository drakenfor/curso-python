import re
from tkinter import *
from tkinter import ttk


# Eliminar letras
def validator(text1, text2, d, new_text: str):

    print(text1, text2, new_text)

    if new_text.isdecimal() or len(new_text) == 0:
        return True

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

    value = globals().get(variables_drill[i]).get()

    if len(value) > 1:
        if value[0] == '0' and value[1] != '.':
            globals().get(variables_drill[i]).set(value[1:])
            
    value = globals().get(variables_drill[i]).get()
    if len(value) > 1:
        globals().get(variables_drill[i]).set(re.sub(r'^0+', '', value))
    #     if '.' == variables[i].get()[0]:
    #         variables[i].set('0' + variables[i].get())


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


entries_drill = [
    [
        'Physical Development parameters', [
            ['Bench Area (m)', 'bench_area'],
            ['Bench Height (m)', 'bench_height'],
            ['Rock density (m)', 'name_var3'],
            ['Burden (m)', 'name_var4'],
            ['Space, (m)', 'name_var5'],
            ['Hole depth, (m)', 'name_var6'],
            ['Sub-drilling, %', 'name_var7'],
        ]
    ],
    [
        'Production drill cycle time', [
            ['Tramming speed, k/h', 'name_var8'],
            ['Average distance between bench, km', 'name_var9'],
        ]
    ],
    [
        'Otros inputs', [
            ['Input1', 'name_var10'],
            ['Input2', 'name_var11'],
        ]
    ]
]

# Function for calc
def drill_calc(*args):
    # validator_sv(*args)

    # Write code here
    # Volume
    try:
        volumen.set(round(float(bench_area.get()) * float(bench_height.get()), 2))
    except:
        print('Error on volume')


iFrames = []
variables_drill = []
it = 0
for i, fields in enumerate(entries_drill):


    iFrames.append(ttk.Frame(production))

    iFrames[i].grid(row=i, column=0, sticky='nwe')
    iFrames[i].columnconfigure(0, weight=1)
    iFrames[i].rowconfigure(0, weight=1)

    ttk.Label(
        iFrames[i],
        text=fields[0],
        font=('Arial', 12),
    ).grid(row=0, column=0, pady=[20, 5], sticky='nw', columnspan=4)

    sep = ttk.Separator(iFrames[i], orient=HORIZONTAL)
    sep.grid(row=1, column=0, sticky='ew', columnspan=4)


    for j, field in enumerate(fields[1]):
        globals().update({field[1]: StringVar()})
        variables_drill.append(field[1])
        globals().get(field[1]).trace('w', drill_calc)
        ttk.Entry(
                iFrames[i],
                justify=RIGHT,
                validate='key',
                textvariable=globals().get(variables_drill[it]),
                validatecommand=(root.register(validator), "%S", "%s", "%d", "%P"),
                width=20
            ).grid(row=j + 2, column=1, sticky='nw')
        ttk.Label(iFrames[i], text=field[0] + ': ').grid(row=j + 2, column=0, padx=5, pady=5, sticky='nw')

        it += 1

### Outputs
outs_drill = [
    [
        'Part 1', [
            ['Volume (m3)', 'volumen'],
            ['Bench Height (m)', 'name_var2'],
            ['Rock density (m)', 'name_var3'],
            ['Burden (m)', 0],
        ],
    ],
    [
        'Part 2', [
            ['Space, (m)', 'name_var4'],
            ['Hole depth, (m)', 'name_var5'],
            ['Sub-drilling, %', 'name_var6'],
        ]
    ],
    [
        'Output 3', [
            ['otro ', 'name_var7'],
            ['otro 2 s', 'name_var8']
        ]
    ]
]

for i, out in enumerate(outs_drill):
    for j, text in enumerate(out[1]):
        globals().update({text[1]: StringVar()})
        ttk.Label(iFrames[i], text=f'{text[0]}: ').grid(row=j + 2, column=3, sticky='nw', padx=10)
        ttk.Label(iFrames[i], textvariable=globals().get(text[1]), justify=RIGHT).grid(row= j + 2, column=4, sticky='nw', padx=10)


######### Tab-End: production-drill#########

######### Tab: Shovel ##############
shovel = ttk.Frame(notebook)
notebook.add(shovel, text='Shovel')
entries_shovel = [
    [
        'Physical Development parameters', [
            ['Bench Area (m)', 'bench_area1'],
            ['Bench Height (m)', 'bench_height1'],
            ['Rock density (m)', 'name_var3'],
            ['Burden (m)', 'name_var4'],
            ['Space, (m)', 'name_var5'],
            ['Hole depth, (m)', 'name_var6'],
            ['Sub-drilling, %', 'name_var7'],
        ]
    ],
    [
        'Production drill cycle time', [
            ['Tramming speed, k/h', 'name_var8'],
            ['Average distance between bench, km', 'name_var9'],
        ]
    ],
    [
        'Otros inputs', [
            ['Input1', 'name_var10'],
            ['Input2', 'name_var11'],
        ]
    ]
]

# Function for calc
def shovel_calc(*args):
    # validator_sv(*args)
    print(*args)

    # Write code here
    # Volume
    try:
        volumen1.set(round(float(bench_area1.get()) * float(bench_height1.get()), 2))
    except:
        print('Error on volume')


sFrames = []
variables_shovel = []
it = 0
for i, fields in enumerate(entries_shovel):


    sFrames.append(ttk.Frame(shovel))

    sFrames[i].grid(row=i, column=0, sticky='nwe')
    sFrames[i].columnconfigure(0, weight=1)
    sFrames[i].rowconfigure(0, weight=1)

    ttk.Label(
        sFrames[i],
        text=fields[0],
        font=('Arial', 12),
    ).grid(row=0, column=0, pady=[20, 5], sticky='nw', columnspan=4)

    sep = ttk.Separator(sFrames[i], orient=HORIZONTAL)
    sep.grid(row=1, column=0, sticky='ew', columnspan=4)


    for j, field in enumerate(fields[1]):
        globals().update({field[1]: StringVar()})
        variables_shovel.append(field[1])
        globals().get(field[1]).trace('w', shovel_calc)
        ttk.Entry(
                sFrames[i],
                justify=RIGHT,
                validate='key',
                textvariable=globals().get(variables_shovel[it]),
                validatecommand=(root.register(validator), "%S", "%s", "%d", "%P"),
                width=20
            ).grid(row=j + 2, column=1, sticky='nw')
        ttk.Label(sFrames[i], text=field[0] + ': ').grid(row=j + 2, column=0, padx=5, pady=5, sticky='nw')

        it += 1

### Outputs
outs_shovel = [
    [
        'Part 1', [
            ['Volume (m3)', 'volumen1'],
            ['Bench Height (m)', 'name_var2'],
            ['Rock density (m)', 'name_var3'],
            ['Burden (m)', 0],
        ],
    ],
    [
        'Part 2', [
            ['Space, (m)', 'name_var4'],
            ['Hole depth, (m)', 'name_var5'],
            ['Sub-drilling, %', 'name_var6'],
        ]
    ],
    [
        'Output 3', [
            ['otro ', 'name_var7'],
            ['otro 2 s', 'name_var8']
        ]
    ]
]

for i, out in enumerate(outs_shovel):
    for j, text in enumerate(out[1]):
        globals().update({text[1]: StringVar()})
        ttk.Label(sFrames[i], text=f'{text[0]}: ').grid(row=j + 2, column=3, sticky='nw', padx=10)
        ttk.Label(sFrames[i], textvariable=globals().get(text[1]), justify=RIGHT).grid(row= j + 2, column=4, sticky='nw', padx=10)


################# End Shovel #####################################

######### Tab: Truck ############## truck = ttk.Frame(notebook)
truck = ttk.Frame(notebook)
notebook.add(truck, text='Truck')

entries_truck = [
    [
        'Physical Development parameters', [
            ['Bench Area (m)', 'bench_area2'],
            ['Bench Height (m)', 'bench_height2'],
            ['Rock density (m)', 'name_var3'],
            ['Burden (m)', 'name_var4'],
            ['Space, (m)', 'name_var5'],
            ['Hole depth, (m)', 'name_var6'],
            ['Sub-drilling, %', 'name_var7'],
        ]
    ],
    [
        'Production drill cycle time', [
            ['Tramming speed, k/h', 'name_var8'],
            ['Average distance between bench, km', 'name_var9'],
        ]
    ],
    [
        'Otros inputs', [
            ['Input1', 'name_var10'],
            ['Input2', 'name_var11'],
            ['input 3', 'name_4']
        ]
    ]
]

# Function for calc
def truck_calc(*args):
    # validator_sv(*args)
    print(*args)

    # Write code here
    # Volume
    try:
        volumen2.set(round(float(bench_area2.get()) * float(bench_height2.get()), 2))
    except:
        print('Error on volume')


tFrames = []
variables_truck = []
it = 0
for i, fields in enumerate(entries_truck):


    tFrames.append(ttk.Frame(truck))

    tFrames[i].grid(row=i, column=0, sticky='nwe')
    tFrames[i].columnconfigure(0, weight=1)
    tFrames[i].rowconfigure(0, weight=1)

    ttk.Label(
        tFrames[i],
        text=fields[0],
        font=('Arial', 12),
    ).grid(row=0, column=0, pady=[20, 5], sticky='nw', columnspan=4)

    sep = ttk.Separator(tFrames[i], orient=HORIZONTAL)
    sep.grid(row=1, column=0, sticky='ew', columnspan=4)


    for j, field in enumerate(fields[1]):
        globals().update({field[1]: StringVar()})
        variables_truck.append(field[1])
        globals().get(field[1]).trace('w', truck_calc)
        ttk.Entry(
                tFrames[i],
                justify=RIGHT,
                validate='key',
                textvariable=globals().get(variables_truck[it]),
                validatecommand=(root.register(validator), "%S", "%s", "%d", "%P"),
                width=20
            ).grid(row=j + 2, column=1, sticky='nw')
        ttk.Label(tFrames[i], text=field[0] + ': ').grid(row=j + 2, column=0, padx=5, pady=5, sticky='nw')

        it += 1

### Outputs
outs_truck = [
    [
        'Part 1', [
            ['Volume (m3)', 'volumen2'],
            ['Bench Height (m)', 'name_var2'],
            ['Rock density (m)', 'name_var3'],
            ['Burden (m)', 0],
        ],
    ],
    [
        'Part 2', [
            ['Space, (m)', 'name_var4'],
            ['Hole depth, (m)', 'name_var5'],
            ['Sub-trucking, %', 'name_var6'],
        ]
    ],
    [
        'Output 3', [
            ['otro ', 'name_var7'],
            ['otro 2 s', 'name_var8']
        ]
    ]
]

for i, out in enumerate(outs_truck):
    for j, text in enumerate(out[1]):
        globals().update({text[1]: StringVar()})
        ttk.Label(tFrames[i], text=f'{text[0]}: ').grid(row=j + 2, column=3, sticky='nw', padx=10)
        ttk.Label(tFrames[i], textvariable=globals().get(text[1]), justify=RIGHT).grid(row= j + 2, column=4, sticky='nw', padx=10)



####################
root.mainloop()