import math
# Physical development parameters
def physical_parameters(
            bucket_capacity: float,
            in_situ_bulk_density: float,
            swell: float,
            fill_factor: float,
            loading: float,
            swing_time: float,
            dump_in_truck: float,
            swing_back: float,
            delays: float,
            efficiency_factor: float,
            days_per_year: float,
            days_worked_per_week: float,
            shifts_per_day: float,
            fuel_up_safety_meeting: float,
            shift_change: float,
            inspect_job: float,
            breakdowns_unplanned_maintenance: float,
            job_or_efficiency_factor: float,

        ):

    # Physical development parameters
    swell_bulk_density = in_situ_bulk_density/(1+(swell)/100)
    bucket_capacity_t = swell_bulk_density*bucket_capacity
    average_pay_load = bucket_capacity_t*(fill_factor/100)
    
    # Shovel cycle time
    total_cycle_time = (loading+swing_time+dump_in_truck+swing_back+delays)/60
    cycle_time = total_cycle_time/(efficiency_factor/100)

    # Shovel performance
    # Roster
    days_worked_per_month = days_per_year/12
    shift_length = 24/shifts_per_day

    # Delays
    planned_maintenance_8_per_week = 8/(7*2)
    total_delays = (fuel_up_safety_meeting+shift_change+inspect_job+planned_maintenance_8_per_week+breakdowns_unplanned_maintenance)

    # Productivity
    balance_of_shift_available = shift_length-total_delays
    effective_hours_per_shift = balance_of_shift_available*(job_or_efficiency_factor/100)
    effective_hours_per_year = effective_hours_per_shift*shifts_per_day*days_per_year
    average_pay_load_effective = (60/cycle_time)*average_pay_load
    annual_shovel_production = effective_hours_per_year*average_pay_load_effective
    day_shovel_production = annual_shovel_production/days_per_year

    return {
        'Physical development parameters': {
                'swell bulk density (t/m^3)': round(swell_bulk_density, 1),
                'bucket capacity t (t)': round(bucket_capacity_t, 1),
                'average_pay_load (t)': round(average_pay_load, 1)  
            },
        
        'Shovel cycle time': {
                'total cycle time (min)': round(total_cycle_time, 1),
                'cycle time (min)': round(cycle_time, 1)
            },
        'Shovel performance':{
            'Roster': {
                'Days worked per month': days_worked_per_month,
                'Shift length (hr)': shift_length,
            },
            'Delays': {
                'Planned maintenance (8h/week)': round(planned_maintenance_8_per_week, 1),
                'Total delays (hr)': round(total_delays, 1),
            },
            'Productivity': {
                'Balance of shift availabe (hr)': round(balance_of_shift_available, 1),
                'Effective hours per shift (hr)': round(effective_hours_per_shift, 1),
                'Effective hours per year (hr)': round(effective_hours_per_year, 1),
                'Average pay load effective (t/hr)': round(average_pay_load_effective, 1),
                'Annual shovel production (t)': annual_shovel_production,
                'Day shovel production (t)': day_shovel_production,
            },

        }

    }