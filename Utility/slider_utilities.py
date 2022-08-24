def generate_parameters(values):
    max_cost = float(values["costs_max"])
    max_mass = float(values["mass_max"]) * 1000  # Because part process returns grams
    max_disp = float(values["displacement_max"])
    max_time = float(values["time_max"]) * 24 * 60 * 60  # Because scheduler is in minutes
    cost_coef = float(values["costs_coef"])
    mass_coef = float(values["mass_coef"])
    disp_coef = float(values["displacement_coef"])
    time_coef = float(values["time_coef"])
    magnitude = float(cost_coef + mass_coef + disp_coef + time_coef)
    if magnitude == 0:  # if all coefficients are zero, set everything to be equal
        cost_coef = 0.25
        mass_coef = 0.25
        disp_coef = 0.25
        time_coef = 0.25
        magnitude = 1
    return max_cost, max_mass, max_disp, max_time, cost_coef / magnitude, mass_coef / magnitude, disp_coef / magnitude, time_coef / magnitude
