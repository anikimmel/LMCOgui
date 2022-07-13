def generate_score(values):
    max_cost = float(values["costs_max"])
    max_mass = float(values["mass_max"])
    max_disp = float(values["displacement_max"])
    max_time = float(values["time_max"])
    cost_coef = float(values["costs_coef"])
    mass_coef = float(values["mass_coef"])
    disp_coef = float(values["displacement_coef"])
    time_coef = float(values["time_coef"])
    return max_cost, max_mass, max_disp, max_time, cost_coef, mass_coef, disp_coef, time_coef