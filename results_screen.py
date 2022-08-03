import PySimpleGUI as sg
from Utility import row_utilities

use_custom_titlebar = True if sg.running_trinket() else False


def make_window(parameters, response, dataMaxes, sort_on="score", default_sort_val="Highest Score"):
    max_cost = parameters[0]
    max_mass = parameters[1]
    max_disp = parameters[2]
    max_time = parameters[3]
    cost_coef = parameters[4]
    mass_coef = parameters[5]
    disp_coef = parameters[6]
    time_coef = parameters[7]
    sg.theme('Default')

    # NOTE that we're using our own LOCAL Menu element
    if use_custom_titlebar:
        Menu = sg.MenubarCustom
    else:
        Menu = sg.Menu

    bids = row_utilities.create_rows(max_cost, max_mass, max_disp, max_time, cost_coef, mass_coef,
                                           disp_coef, time_coef, response, dataMaxes)
    rows = row_utilities.sortRows(bids, sort_on)
    # Note - LOCAL Menu element is used (see about for how that's defined)
    layout = [[Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]], k='-CUST MENUBAR-', p=0)],
              [sg.T('Lockheed Martin Demo GUI', font='_ 14', justification='c', expand_x=True)],
              [sg.HSep()],
              [sg.Text("Sort: "),
               sg.OptionMenu(['Highest Score', 'Fastest', 'Cheapest', 'Lightest'], s=(15, 2),
                             key='sort_design_options', default_value=default_sort_val),
               sg.Button("Re-Sort!", key="re-sort", enable_events=True),
               sg.Button("Create New Request", key="backtoinit-results", enable_events=True),
               sg.Push(), sg.Button("View Graphs", key="graphs", enable_events=True)],
              [sg.Text("Parameter Weights -- Cost: " + str(round(cost_coef, 3))
                       + ", Mass: " + str(round(mass_coef, 3))
                       + ", Lead Time: " + str(round(time_coef, 3))
                       + ", Max Displacement: " + str(round(disp_coef, 3))), sg.Push(),
               sg.Button("Change Objective Parameters", key='backtosliders', enable_events=True)],
              [sg.Col(rows, scrollable=True)]]

    window = sg.Window('LMCO Demo', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
                       keep_on_top=True, use_custom_titlebar=use_custom_titlebar)

    for bid in bids:
        window['-CBAR-'+bid["link"]].update(bid["cost"])
        window['-MBAR-'+bid["link"]].update(bid["mass"])
        window['-TBAR-'+bid["link"]].update(bid["time"])
        window['-DBAR-'+bid["link"]].update(bid["disp"])
    return window, bids
