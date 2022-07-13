import json
import PySimpleGUI as sg
from Utility import db_utils

NAME_SIZE = 20


def name(name):
    dots = NAME_SIZE - len(name) - 2
    return sg.Text(name + ' ' + '•' * dots, size=(NAME_SIZE, 1), justification='r', pad=(0, 0), font='Courier 10')


def create_rows(max_cost, max_mass, max_disp, max_time, cost_coef, mass_coef, disp_coef, time_coef, response):
    r = json.load(open('C:\\Users\\Annie\\PycharmProjects\\LMCOgui\\Utility\\Data\\bids-example.json'))
    data = r["data"]
    rows = []
    i = 0
    for bid in data:
        plan = db_utils.getSpecificPlan(bid["ProcessPlan"])
        score = generate_score(max_cost, max_mass, max_disp, max_time, cost_coef, mass_coef, disp_coef, time_coef,
                               float(bid["cost"]), float(bid["leadTime"]), plan(["NetGrams"]), 2)
        layout_l = [sg.Image(sg.EMOJI_BASE64_HAPPY_THUMBS_UP)]

        layout_bars = [[name('Cost'), sg.ProgressBar(max_cost, orientation='h', s=(10, 20), k=('-CBAR-'+str(i)))],
                       [name('Time'), sg.ProgressBar(max_time, orientation='h', s=(10, 20), k=('-TBAR-'+str(i)))],
                       [name('Mass'), sg.ProgressBar(max_mass, orientation='h', s=(10, 20), k=('-MBAR-'+str(i)))],
                       [name('Displacement'), sg.ProgressBar(max_mass, orientation='h', s=(10, 20), k='-DBAR-')]]

        layout_buttons = [
            [sg.Col([[sg.Button('Design File'), sg.Button('Supplier Info')]])],
            [sg.Col([[sg.Button('Process Plan'), sg.Button('Initiate Contract', button_color='green')]])]
        ]

        layout_c = [sg.Pane([sg.Col([[sg.T('Score' + '\n' + str(score), justification='c', background_color='green')]],
                                    background_color='green')], background_color='green'),
                    sg.Col(layout_bars), sg.Col(layout_buttons)]

        content = [[sg.Text(plan["Link"])],
                   [sg.Col([layout_l], p=20, vertical_alignment='t'),
                    sg.Col([layout_c], p=20, vertical_alignment='t')]]
        i += 1
        rows.append(content)
    return rows, data


def generate_score(max_cost, max_mass, max_disp, max_time, cost_coef, mass_coef, disp_coef,
                   time_coef, cost, time, mass, displacement):
    return cost_coef * (max_cost-cost) + mass_coef * (max_mass-mass) \
           + time_coef * (max_time-time) + disp_coef * (max_disp-displacement)
