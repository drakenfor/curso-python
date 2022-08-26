import math
# Physical development parameters
def physical_parameters(
            truck_capacity: float,
            fill_factor: float,
            tramming_speed_loaded: float,
            travel_loaded: float,
            dumping: float,
            tramming_speed_unloaded: float,
            travel_unloaded: float,
            efficiency_factor: float,
            days_per_year: float,
            days_worked_per_week: float,
            shift_per_day: float,
            fuel_up_safety_meeting: float,
            shift_change: float,
            inspect_job: float,
            breakdowns_unplanned_maintenance: float,
            job_or_efficiency_factor: float,
            shovel_average_pay_load: float,
        ):
    # Physical development parameters
    # Parameter
    average_pay_load = truck_capacity*(fill_factor/100)

    # Truck cycle time
    # Component
    shovel_cycle_time_per_pass = average_pay_load/shovel_average_pay_load
    number_of_passes = average_pay_load/shovel_average_pay_load
    loading = shovel_cycle_time_per_pass*number_of_passes
    travel_loaded_min = travel_loaded/tramming_speed_loaded*60
    travel_unloaded_min = travel_unloaded/tramming_speed_unloaded*60
    total_cycle_time = (loading+travel_loaded_min+dumping+travel_loaded_min)
    cycle_time = total_cycle_time/(efficiency_factor/100)

    # Truck performance
    # Roster
    days_worked_per_month = days_per_year/12
    shift_length = 24/shift_per_day

    # Delays
    planned_maintenance_8_per_week = 8/(days_worked_per_week*shift_per_day)
    total_delays = (fuel_up_safety_meeting+shift_change+inspect_job+planned_maintenance_8_per_week+breakdowns_unplanned_maintenance)

    # Productivity
    balance_of_shift_available = shift_length-total_delays
    effective_hours_per_shift = balance_of_shift_available*(job_or_efficiency_factor/100)
    effective_hours_per_year = effective_hours_per_shift*shift_per_day*days_per_year
    average_pay_load_effective = (60/cycle_time)*average_pay_load
    annual_truck_production = average_pay_load_effective*effective_hours_per_year
    day_truck_production = annual_truck_production/days_per_year

    return {
        'Physical development parameters':{
            'Parameter': {
                'Average pay load (t)': round(average_pay_load, 1),
                'Shovel average pay load (t)': round(shovel_average_pay_load, 1),
            }
        },

        'Truck cycle time': {
            'Component': {
                'Shovel cycle time per pass (min)': round(shovel_cycle_time_per_pass,2),
                'Number of passes': number_of_passes,
                'Loading (min)': round(loading, 1),
                'Travel loaded (min)': round(travel_loaded_min, 1),
                'Travel unloaded (min)': round(travel_unloaded_min, 1),
                'Total cycle time (min)': round(total_cycle_time, 1),
                'Cycle time (min)': round(cycle_time, 1),
            }
        },

        'Truck Performance': {
            'Roster': {
                'Days worked per month': days_worked_per_month,
                'Shift length (hr)': shift_length,
            },

            'Delays': {
                'Planned maintenance (8h/week)': round(planned_maintenance_8_per_week,1),
                'Total delays (hr)': round(total_delays, 1),
            },

            'Productivity': {
                'Balance of shift available (hr)': round(balance_of_shift_available, 1),
                'Effective hours per shift (hr)': round(effective_hours_per_shift, 1),
                'Effective hours per year (hr)': effective_hours_per_year,
                'Average pay load effective (t/hr)': round(average_pay_load_effective, 2),
                'Annual truck production (t)': round(annual_truck_production, 0),
                "Day truck production (t)": round(day_truck_production, 0),
            }
        }
      
    }
