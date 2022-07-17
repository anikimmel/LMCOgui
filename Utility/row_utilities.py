import json
import PySimpleGUI as sg
from Utility import db_utils

NAME_SIZE = 20


def name(name):
    dots = NAME_SIZE - len(name) - 2
    return sg.Text(name + ' ' + '•' * dots, size=(NAME_SIZE, 1), justification='r', pad=(0, 0), font='Courier 10')


def create_rows(max_cost, max_mass, max_disp, max_time, cost_coef, mass_coef, disp_coef, time_coef, response):
    data = response["data"]
    rows = []
    i = 0
    final_bids = []
    max_score = float(max_cost*cost_coef + max_mass*mass_coef + max_time*time_coef + max_disp*disp_coef)
    for bid in data:
        plan = db_utils.getSpecificPlan(bid["processPlan"])
        if (bid["cost"] > max_cost) or (bid["leadTime"] > max_time) or (plan["NetGrams"] > max_mass):
            continue
        score = generate_score(max_cost, max_mass, max_disp, max_time, cost_coef, mass_coef, disp_coef, time_coef,
                               float(bid["cost"]), float(bid["leadTime"]), float(plan["NetGrams"]), 0.05, max_score)

        layout_bars = [[name('Cost'), sg.ProgressBar(max_cost, orientation='h', s=(10, 20), k=('-CBAR-'+str(i)))],
                       [name('Time'), sg.ProgressBar(max_time, orientation='h', s=(10, 20), k=('-TBAR-'+str(i)))],
                       [name('Mass'), sg.ProgressBar(max_mass, orientation='h', s=(10, 20), k=('-MBAR-'+str(i)))],
                       [name('Displacement'), sg.ProgressBar(max_disp, orientation='h', s=(10, 20), k=('-DBAR-'+str(i)))]]

        layout_buttons = [
            [sg.Col([[sg.Button('Design File'), sg.Button('Supplier Info')]])],
            [sg.Col([[sg.Button('Process Plan'), sg.Button('Initiate Contract', button_color='green')]])]
        ]

        layout_c = [sg.Image(sg.EMOJI_BASE64_HAPPY_THUMBS_UP), sg.Pane([sg.Col([[sg.T('Score' + '\n' + str(score), justification='c', background_color='green')]],
                                    background_color='green')], background_color='green'),
                    sg.Col(layout_bars), sg.Col(layout_buttons)]

        content = sg.Frame(plan["Link"], [[sg.Col([layout_c], p=20, vertical_alignment='t')]], border_width=3)
        i += 1
        rows.append([content])
        final_bids.append(bid)
    return rows, final_bids


def generate_score(max_cost, max_mass, max_disp, max_time, cost_coef, mass_coef, disp_coef,
                   time_coef, cost, time, mass, displacement, max_score):
    return 100*(cost_coef * (max_cost-cost) + mass_coef * (max_mass-mass) \
           + time_coef * (max_time-time) + disp_coef * (max_disp-displacement))/max_score
