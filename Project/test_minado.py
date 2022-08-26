from multiprocessing.context import SpawnContext
import re
from tkinter import *
from tkinter import ttk
from turtle import width


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
            ['Rock density (t/m3)', 'rock_density'],
            ['Burden (m)', 'burden'],
            ['Space, (m)', 'space'],
            ['Hole depth, (m)', 'hole_depth'],
            ['Sub-drilling, (%)', 'sub_drilling'],
        ]
    ],
    [
        'Production drill cycle time', [
            ['Tramming speed, (km/h)', 'tramming_speed'],
            ['Average distance between bench, km', 'average_distance_between_bench'],
            ['Setup time (min)', 'setup_time'],
            ['Instantaneous penetration rate 9 7/8" holes (m/min)', 'instantaneous_penetration_rate_holes'],
            ['Setup time per hole drilled (min)', 'setup_time_per_hole_drilled'],
        ]
    ],
    [
        'Production drill performance', [
            ['Days per year', 'days_per_year'],
            ['Days worked per week', 'days_worked_per_week'],
            ['Shifts per day', 'shifts_per_day'],
            ['Shift lenght (h)', 'shift_lenght'],
            ['Shift change (h)', 'shift_change'],
            ['No bench available (h)', 'no_bench_available'],
            ['No power (h)', 'no_power'],
            ['Meetings (h)', 'meetings'],
            ['Pump-water problems (h)', 'pump_water_problems'],
            ['Maintenance - breakdown (h)', 'maintenance_breakdown']
        ]
    ],
    [
        'PRODUCCIÓN MINA ', [
            ['Production 2016', 'production_2016'],
            ['Production 2017', 'production_2017'],
        ]
    ],
]
import math
# Function for calc
def drill_calc(*args):
    # validator_sv(*args)

    # Write code here
    # Volume
    try:
        volumen.set(round(float(bench_area.get()) * float(bench_height.get()), 2))
    except:
        print('Error on volume')

    try:
        metric_tons.set(round(float(volumen.get())*float(rock_density.get()), 2))
    except:
        print('Error on metric tons')
    try:
        total_hole_depth.set(round(float(hole_depth.get())+(float(sub_drilling.get())*float(hole_depth.get()))/100,2))
    except:
        print('Error on hole depth')
    try:
        number_of_production_holes.set(math.ceil(float(volumen.get())/(float(burden.get())*float(space.get())*float(hole_depth.get()))))
    except:
        print('Error on number of production holes')
    try:
        diameter_holes_meters_drilled.set(round(float(number_of_production_holes.get())*float(total_hole_depth.get()),2))
    except:
        print('Error on diameter holes meters drilled')
    try:
        tramming_time.set(round((float(average_distance_between_bench.get())/float(tramming_speed.get())*60),2))
    except:
        print('Error on tramming time ')
    try:
        total_setup_time.set(round(float(tramming_time.get())+float(setup_time.get()),2))
    except:
        print('Error on total setup time')
    try:
        setup_time_per_cut.set(round(float(total_setup_time.get())/60,1))
    except:    
        print('Error on setup time per cut')
    try:
        meters_drilled_holes.set(round(float(diameter_holes_meters_drilled.get()),2))
    except:
        print('Error on meters drilled_holes')
    try:
        drilling_time_holes.set(round(float(meters_drilled_holes.get())/float(instantaneous_penetration_rate_holes.get()),1))
    except:
        print('Error on drilling time_holes')
    try:
        total_drilling_time.set(round(float(drilling_time_holes.get())/60,1))
    except:
        print('Error on total drilling_time')
    try:
        holes_drilled.set(round(float(number_of_production_holes.get()),2))
    except:
        print('Error on holes drilled')
    try:
        total_set_up_time.set(round(float(holes_drilled.get())*float(setup_time_per_hole_drilled.get()),2))
    except:
        print('Error on total set up time')
    try:
        total_set_up_time_h.set(round(float(total_set_up_time.get())/60,2))
    except:
        print('Error on total set up time h')
    try:
        total_set_up_and_drill_time.set(round(float(total_drilling_time.get())+float(total_set_up_time_h.get()),1))
    except:
        print('Error on total set up and drill time')
    try:
        total_time_per_face.set(round(float(total_set_up_and_drill_time.get())+float(setup_time_per_cut.get()),1))
    except:
        print('Error on total time per face')
    try:
        days_worked_per_month.set(round(float(days_per_year.get()/12),1))
    except:
        print('Error on Days worked per month')
    try:
        total_delays.set(round(float(shift_change.get())+float(no_bench_available.get())+float(no_power.get())+float(meetings.get())+ float(pump_water_problems.get())+float(maintenance_breakdown.get()),2))
    except:
        print('Error on total delays')
    try:
        balance_of_shift_available.set(round(float(shift_lenght.get())-float(total_delays.get()),2))
    except:   
        print('Error on balance of shift available')
    try:
        rows_drilled_out.set(round(float(balance_of_shift_available.get())/float(total_time_per_face.get()),2))
    except:   
        print('Error on rows drilled out')
    try:
        meters_drilled_per_shift.set(round(float(diameter_holes_meters_drilled.get())*float(rows_drilled_out.get()),2))
    except:   
        print('Error on meters drilled per shift')
    try:
        meters_drilled_per_working_day.set(round(float(meters_drilled_per_shift.get())*float(shifts_per_day.get()),2))
    except:   
        print('Error on Meters drilled per working day')
    try:
        meters_drilled_per_month.set(round(float(meters_drilled_per_working_day.get())*float(days_worked_per_month.get()),2))
    except:   
        print('Error on Meters drilled per month')
    try:
        metrics_tons_per_shift.set(round(float(metric_tons.get())*float(rows_drilled_out.get()),2))
    except:   
        print('Error on Metrics tons per shift')
    try:
        metrics_tons_per_working_day.set(round(float(metrics_tons_per_shift.get())*float(shifts_per_day.get()),2))
    except:   
        print('Error on Metrics tons per working day')
    try:
        metrics_tons_per_month.set(round(float(metrics_tons_per_working_day.get())*float(days_worked_per_month.get()),2))
    except:   
        print('Error on Metrics tons per month')
    


    

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
        ttk.Label(iFrames[i], text=field[0] + ': ').grid(row=j + 2, column=0, padx=5, pady=3, sticky='nw')

        it += 1

### Outputs
outs_drill = [
    [
        'Part 1', [
            ['Volume (m3)', 'volumen'],
            ['Metric tons (tn)', 'metric_tons'],
            ['Total hole depth (m)', 'total_hole_depth'],
            ['Number of production holes', 'number_of_production_holes'],
            ['9 7/8" diameter holes, meters drilled (m)','diameter_holes_meters_drilled'],
        ],
    ],
    [
        'Part 2', [
            ['Tramming time (min)', 'tramming_time'],
            ['Total setup time (min)', 'total_setup_time'],
            ['Setup time (=engine hours) per cut (h)', 'setup_time_per_cut'],
            ['Meters drilled 9 7/8" holes (m)', 'meters_drilled_holes'],
            ['Drilling time 9 7/8" holes (min)', 'drilling_time_holes'],
            ['Total drilling time (h)', 'total_drilling_time'],
            ['Holes drilled ', 'holes_drilled'],
            ['Total set_up time (min)', 'total_set_up_time'],
            ['Total set_up time (h)', 'total_set_up_time_h'],
            ['Total set_up and drill time (h)', 'total_set_up_and_drill_time'],
            ['Total time per face (h)', 'total_time_per_face'],
        ]
    ],
    [
        'Part 3', [
            ['Days worked per month  ', 'days_worked_per_month'],
            ['Total delays (h)', 'total_delays'],
            ['Balance of shift available (h)', 'balance_of_shift_available'],
            ['Rows drilled out', 'rows_drilled_out'],
            ['Meters drilled per shift (m)', 'meters_drilled_per_shift'],
            ['Meters drilled per working day (m)', 'meters_drilled_per_working_day'],
            ['Meters drilled per month (m)', 'meters_drilled_per_month'],
            ['Metrics tons per shift (t)', 'metrics_tons_per_shift'],
            ['Metrics tons per working day (t)', 'metrics_tons_per_working_day'],
            ['Metrics tons per month (t)', 'metrics_tons_per_month'],
        ]
    ]
]

for i, out in enumerate(outs_drill):
    for j, text in enumerate(out[1]):
        globals().update({text[1]: StringVar()})
        ttk.Label(iFrames[i], text=f'{text[0]}: ').grid(row=j + 2, column=3, sticky='nw', padx=10)
        ttk.Label(iFrames[i], textvariable=globals().get(text[1]), justify=RIGHT).grid( row= j + 2, column=4, sticky='nw', padx=10)


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
        ttk.Label(sFrames[i], text=field[0] + ': ').grid(row=j + 2, column=0, padx=5, pady=3, sticky='nw')

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
        ttk.Label(tFrames[i], text=field[0] + ': ').grid(row=j + 2, column=0, padx=5, pady=3, sticky='nw')

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