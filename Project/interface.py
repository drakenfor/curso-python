import re
from tkinter import *
from tkinter import ttk

# Eliminar letras
def validator(string: str):
    numbers = '1234567890'
    new_string = ''
    dot = False

    for char in string:
        if char in numbers:
            new_string += char 
        elif char == '.':
            if not dot:
                new_string += '.'
                dot = True

    new_string = '0'+ re.sub(r'^0+', '', new_string)
    if len(new_string) > 1:
        if new_string[1]!= '.':
            new_string = new_string[1:]
    return new_string

root = Tk()

# Calculos
def calc_volumen(*args):

    # height.set(validator(height.get()))
    # area.set(validator(area.get()))
    # rock.set(validator(rock.get()))
    # hole.set(validator(hole.get()))
    # burden.set(validator(burden.get()))
    # subdrilling.set(validator(subdrilling.get()))
    # space.set(validator(space.get()))
    
    volumen.set(float(height.get()) * float(area.get()))
    metric_tons.set(float(rock.get()) * float(volumen.get()))


# estilos

# TODO: Poner un titulo apropiado
root.title('Calculo de equipos')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

################## Creando las pestanas ################
nb = ttk.Notebook(root)
nb.pack(fill='both', expand='yes')

######################## Pestana 1 ####################
production = ttk.Frame(nb)
nb.add(production, text='Production Drill')

#img = PhotoImage(file='Project/assets/img/production-drill.png')
#prod_label = Label(production, image=img)
#prod_label.grid(column=0, row=0)

frame_prod = Frame(production)
frame_prod.grid(row=1, column=0)

# measures Area height
bench_label = ttk.Label(frame_prod, text='Bench: ').grid(column=0, row=2)

# Area
area = StringVar()
area.set(0)
area_label = ttk.Label(frame_prod, text='Area:').grid(column=1, row=1)
area_entry = ttk.Entry(frame_prod, textvariable=area, ).grid(column=1, row=2)

# Height
height = StringVar()
height.set(0)
height_label = ttk.Label(frame_prod, text='Height').grid(column=2, row=1)
height_entry = ttk.Entry(frame_prod, textvariable=height).grid(column=2, row=2)

# Volumen
volumen = StringVar()
volumen.set(0.0)
    

height.trace('w', calc_volumen)
area.trace('w', calc_volumen)

volumen_title = ttk.Label(frame_prod, text='Volumen').grid(column=3, row=1)
volumen_label = ttk.Label(frame_prod, textvariable=volumen).grid(column=3,row=2)
    
# Rock
rock = StringVar()
rock.set(0)
rock_label = ttk.Label(frame_prod, text='Rock Density: ').grid(column=0, row=4)
ttk.Entry(frame_prod, textvariable=rock).grid(column=1, row=4)

# mitric nots
ttk.Label(frame_prod, text='Metric tons, t').grid(column=0, row=5)
metric_tons = StringVar()
ttk.Label(frame_prod, textvariable=metric_tons).grid(column=3, row=5)


rock.trace('w', calc_volumen)

# Burden
burden = StringVar()
burden.set(0)
ttk.Label(frame_prod, text='Burden, m: ').grid(row=6, column=0)
ttk.Entry(frame_prod, textvariable=burden).grid(row=6, column=1)
burden.trace('w', calc_volumen)

# Space
space = StringVar()
space.set(0)
ttk.Label(frame_prod, text='Space, m: ').grid(row=7, column=0)
ttk.Entry(frame_prod, textvariable=space).grid(row=7, column=1)
space.trace('w', calc_volumen)

# Burden
hole = StringVar()
hole.set(0)
ttk.Label(frame_prod, text='Hole depth, m: ').grid(row=7, column=0)
ttk.Entry(frame_prod, textvariable=hole).grid(row=7, column=1)
hole.trace('w', calc_volumen)

# Subdrilling
subdrilling = StringVar()
subdrilling.set(0)
ttk.Label(frame_prod, text='Subdrilling, %: ').grid(row=8, column=0)
ttk.Entry(frame_prod, textvariable=subdrilling).grid(row=8, column=1)
subdrilling.trace('w', calc_volumen)



############################# pestana 2 ##############
shovel = ttk.Frame(nb)
nb.add(shovel, text='Shovel')

##################### pestana 3 ##########################
truck = ttk.Frame(nb)
nb.add(truck, text='Truck')

###########################################################

root.geometry('400x400')
root.mainloop()