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
            ['Average distance between bench, (km)', 'average_distance_between_bench'],
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
        days_worked_per_month.set(round(float(days_per_year.get())/12),1)
    except:
        print('Error on days worked per month')
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
        print('Error on meters drilled per working day')
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
    try:
        units_of_production_drillers_2016.set(math.ceil(float(production_2016.get())/(float(metrics_tons_per_month.get())*12)))
    except:   
        print('Error on units of production drillers 2016')
    try:
        units_of_production_drillers_2017.set(math.ceil(float(production_2017.get())/(float(metrics_tons_per_month.get())*12)))
    except:   
        print('Error on units of production drillers 2017')


    

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
    ).grid(row=0, column=0, pady=[4, 4], sticky='nw', columnspan=4)

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
        ],
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
    ],
    [
        'Part 4', [
            ['Mining equipment - Units of Production drillers (2016)', 'units_of_production_drillers_2016'],
            ['Mining equipment - Units of production drillers (2017)', 'units_of_production_drillers_2017'],
        ],
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
            ['Bucket capacity (m3)', 'bucket_capacity_m'],
            ['In situ bulk density (t/m3)', 'in_situ_bulk_density'],
            ['Swell (%)', 'swell'],
            ['Fill factor (%)', 'fill_factor'],
        ]
    ],
    [
        'Shovel cycle time', [
            ['Loading (s)', 'loading'],
            ['Swing time (s)', 'swing_time'],
            ['dump in truck (s)', 'dump_in_truck'],
            ['Swing back (s)', 'swing_back'],
            ['delays (s)', 'delays'],
            ['Efficiency factor (%)', 'efficiency_factor'],
        ]
    ],
    [
        'Shovel Performance', [
            ['Days per year', 'days_per_year'],
            ['Days worked per week', 'days_worked_per_week'],
            ['Shift per day', 'shift_per_day'],
            ['Fuel up safety meeting (h)', 'fuel_up_safety_meeting'],
            ['Shift change (h)', 'shift_change'],
            ['Inspect job (h)', 'inspect_job'],
            ['Breakdowns/unplanned maintenance (h)', 'breakdowns_unplanned_maintenance'],
            ['Job or efficiency factor (%)', 'job_or_efficiency_factor'],
    
        ]
    ],
    [
        'PRODUCCIÓN MINA',[
            ['Production 2016', 'production_2016'],
            ['Production 2017', 'production_2017'],
        ]
    ],
]

# Function for calc
def shovel_calc(*args):
    # validator_sv(*args)
    print(*args)

    # Write code here
    # Volume
    try:
        swell_bulk_density.set(round(float(in_situ_bulk_density.get()) /(1+float(swell.get())/100), 2))
    except:
        print('Error on sweell bulk density')
    try:
        bucket_capacity.set(round(float(swell_bulk_density.get())*(float(bucket_capacity_m.get())),1))
    except:
        print('Error on Bucket capacity')
    try:
        average_pay_load.set(round(float(bucket_capacity.get())*(float(fill_factor.get())/100),1))
    except:
        print('Error on Average pay load')
    try:
        total_cycle_time.set(round((float(loading.get())+float(swing_time.get())+float(dump_in_truck.get())+float(swing_back.get())+float(delays.get()))/60,2))
    except:
        print('Error on total cycle time')  
    try:
       cycle_time.set(round(float(total_cycle_time.get())/(float(efficiency_factor.get())/100),2))
    except:
        print('Error on cycle time')
    try:
       days_worked_per_month.set(round(float(days_per_year.get())/12,2))
    except:
        print('Error on days worked per month')
    try:
       shift_length.set(24/float(shift_per_day.get()))
    except:
        print('Error on shift length')
    try:
       planned_maintenance.set(round(8/float(days_worked_per_week.get())/float(shift_per_day.get()),1))
    except:
        print('planned maintenance')
    try:
       total_delays.set(round(float(fuel_up_safety_meeting.get())+float(shift_change.get())+float(planned_maintenance.get())+float(inspect_job.get())+float(breakdowns_unplanned_maintenance.get()),1))
    except:
        print('total delays')
    try:
       balance_of_shift_available.set(round(float(shift_length.get())-float(total_delays.get()),1))
    except:
        print('total delays')
    try:
       effective_hours_per_shift.set(round(float(balance_of_shift_available.get())*(float(job_or_efficiency_factor.get())/100),2))
    except:
        print('effective hours per shift')
    try:
       effective_hours_per_year.set(round(float(effective_hours_per_shift.get())*float(shift_per_day.get())*float(days_per_year.get()),2))
    except:
        print('effective hours per shift')   
    try:
       average_pay_load_effective.set(round((60/float(cycle_time.get()))*float(average_pay_load.get()),2))
    except:
        print('average pay load effective') 
    try:
       annual_shovel_production.set(round(float(effective_hours_per_year.get())*float(average_pay_load_effective.get()),1))
    except:
        print('annual shovel production') 
    try:
       day_shovel_production.set(round(float(annual_shovel_production.get())/float(days_per_year.get()),1))
    except:
        print('day_shovel_production')
    try:
       units_of_shovels_2016.set(math.ceil(float(production_2016.get())/float(annual_shovel_production.get())))
    except:
        print('units of shovels 2016')
    try:
       units_of_shovels_2017.set(math.ceil(float(production_2017.get())/float(annual_shovel_production.get())))
    except:
        print('units_of_shovels_2017')

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
            ['Swell bulk density (t/m3)', 'swell_bulk_density'],
            ['Bucket capacity (t)', 'bucket_capacity'],
            ['Average pay load (t)', 'average_pay_load'],
        ]
    ],
    [
        'Part 2', [
            ['Total cycle time (min)', 'total_cycle_time'],
            ['Cycle time (min)', 'cycle_time'],
        ]
    ],
    [
        'Part 3', [
            ['Days worked per month ', 'days_worked_per_month'],
            ['Shift length (h)', 'shift_length'],
            ['Planned maintenance (8h/week) ', 'planned_maintenance'],
            ['Total delays (h)', 'total_delays'],
            ['Balance of shift available (h) ', 'balance_of_shift_available'],
            ['Effective hours per shift (h)', 'effective_hours_per_shift'],
            ['Effective hours per year (h) ', 'effective_hours_per_year'],
            ['Average pay load effective (t/h)', 'average_pay_load_effective'],
            ['Annual Shovel production (t)', 'annual_shovel_production'],
            ['Day shovel production (t)', 'day_shovel_production'],
            
        ]
    ],
    [
        'Part 4', [
            ['Mining equipment - Units of shovels 2016', 'units_of_shovels_2016'],
            ['Mining equipment - Units of shovels 2017', 'units_of_shovels_2017'],
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
        'a', [
            ['a', 'a'],
            ['a', 'fa'],

        ]
    ],
    [
        'a', [
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
        ]
    ],
    [
        'a', [
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
        ]
    ],
    [
        'PRODUCCIÓN MINA', [
            ['a', 'a'],
            ['a', 'a'],
        ]
    ],
]

# Function for calc
def truck_calc(*args):
    # validator_sv(*args)
    print(*args)

    # Write code here
    # Volume
    



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
        'a', [
            ['a','a'],
            ['a','a'],
        ],
    ],
    [
        'Part 2', [
            ['a','a'],
            ['a','a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            
        ]
    ],
    [
        'Part 3', [
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
            ['a', 'a'],
        ]
    ],
    [
        'Part 4', [
            ['a', 'a'],
            ['a', 'a'],
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