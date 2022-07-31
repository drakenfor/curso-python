
import math
# Physical developemnt parameters
def physical_parameters(
            bench_width: float,
            bench_large: float,
            bench_heigth:float,
            rock_density: float,
            burden: float,
            space: float,
            hole_depth: float,
            subdrilling: float,
            tramming_speed: float, 
            average_distance: float, 
            setup_time: float,
            instantaneous_penetration_rate: float,
            setup_time_per_hole_drilled: float,
            days_per_year: float,
            days_worked_per_week: float,
            shifts_per_day: float,
            shift_length: float,
            shift_change: float,
            no_bench_available: float,
            no_power: float,
            meetings: float,
            pump_or_water_problems: float,
            maintenance_breakdown: float,

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
    setup_time_per_cut = total_setup_time/60

    # Drilling Cycle
    drilling_time = meters_drilled/instantaneous_penetration_rate
    total_drilling_time = drilling_time/60
    holes_drilled = number_production_holes
    total_set_up_time = holes_drilled * setup_time_per_hole_drilled
    total_set_up_drill_time = total_drilling_time + total_set_up_time / 60
    total_time_per_face = total_set_up_drill_time + setup_time_per_cut

    # Production drill performance

    # Roster
    days_worked_per_month = days_per_year/12

    # Delays
    total_delays = shift_change + no_bench_available + no_power + meetings + pump_or_water_problems + maintenance_breakdown

    # Productivity
    balance_of_shift_available = shift_length - total_delays
    rows_drilled_out = balance_of_shift_available/total_time_per_face
    meters_drilled_per_shift = meters_drilled * rows_drilled_out
    meters_drilled_per_working_day = meters_drilled_per_shift * 2
    meters_drilled_per_month = meters_drilled_per_working_day * 30
    metrics_tons_per_shift = metric_tons * rows_drilled_out
    metrics_tons_per_working_day = metrics_tons_per_shift * 2
    metrics_tons_per_month = metrics_tons_per_working_day * 30

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
                'Setup time per cut (h)': round(setup_time_per_cut, 1),
            },
            'Drilling Cycle': {
                'Meters drilled, 9 7/8" holes (m)': meters_drilled,
                'Drilling time, 9 7/8" holes, (min)': drilling_time,
                'Total drilling time (h)': total_drilling_time,
                'Holes drilled': holes_drilled,
                'Total set-up time (min)': total_set_up_time,
                'Total set-up time (h)': round(total_set_up_time/60,1),
                'Total set-up and drill time (h)': total_set_up_drill_time,
                'Total time per face (h)': total_time_per_face

            },
            'Production drill performance': {
                'Roster':{
                    'Days worked per month': days_worked_per_month,
                },
                'Delays':{
                    'Total delays, (h)': total_delays,
                },
                'Productivity':{
                    'Balance of shift available, (h)': balance_of_shift_available,
                    'Rows drilled out': rows_drilled_out,
                    'Meters drilled per shift, (m)': meters_drilled_per_shift,
                    'Meters drilled per working day, (m)': meters_drilled_per_working_day,
                    'Meters drilled per month, (m)': meters_drilled_per_month,
                    'Metrics tons per shift, (tn)': metrics_tons_per_shift,
                    'Metrics tons per working day, (tn)': metrics_tons_per_working_day,
                    'Metrics tons per month, (tn)': metrics_tons_per_month
                }
            }
        }
    }



def suma_cuadrado(a, b):
    return a**2 + b**2