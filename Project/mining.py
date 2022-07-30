
import math
# Physical developemnt parameters
def physical_parameters(
            bench_width: float,
            bench_large: float,
            bench_heigth:float,
            rock_density: float,
            burden: float,
            space: float,
            hole_depth: float,subdrilling: float,
            tramming_speed: float, 
            average_distance: float, 
            setup_time: float,
            instantaneus_penetration_rate: float,
            setup_time_per_hole_drilled: float
        ):

    # Physical devopment parameters
    volumen = bench_heigth * bench_large * bench_width
    metric_tons = rock_density * volumen
    total_hole_depth = hole_depth * (1 + subdrilling/100)
    number_production_holes = math.ceil(volumen/(burden * space * hole_depth))
    meters_drilled = total_hole_depth * number_production_holes

    # Production drill cycle time

    # setup
    tramming_time = (average_distance/tramming_speed) * 60
    total_setup_time = tramming_time + setup_time
    total_time_percut = total_setup_time/60

    # Drilling Cycle
    drilling_time = meters_drilled/instantaneus_penetration_rate
    total_drilling_time = drilling_time/60
    holes_drilled = number_production_holes
    total_set_up_time = holes_drilled * setup_time_per_hole_drilled
    total_set_up_drill_time = total_drilling_time + total_set_up_time / 60
    total_time_perface = total_set_up_drill_time + total_time_percut

    return {
        'Physical development parameters': {
                'Volumen (m^3)': round(volumen, 1),
                'Metric tons (t)': round(metric_tons, 1),
                'Total hole depth (m)': round(total_hole_depth, 1),
                'Number of production holes': number_production_holes,
                '9 7/8" diameter holes, meters drilled (m)': round(meters_drilled, 1)
            },
        'Production drill cycle time': {
            'Setup': {
                'Tramming time (min)': round(tramming_time, 1),
                'Total setup time (min)': round(total_setup_time, 1),
                'Setup time per cut (h)': round(total_time_percut, 1),
            },
            'Drilling Cycle': {
                'Meters drilled, 9 7/8" holes (m)': meters_drilled,
                'Drilling time, 9 7/8" holes, min': drilling_time,
                'Total drilling time (h)': total_drilling_time,
                'Holes drilled': holes_drilled,
                'Total set-up time (min)': total_set_up_time,
                'Total set-up time (h)': round(total_set_up_time/60,1),
                'Total set-up and drill time (h)': total_set_up_drill_time,
                'Total time per face (h)': total_time_perface

            }
        }
    }

    print("Hola mundo")
    


