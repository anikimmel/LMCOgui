import PySimpleGUI as sg
from Utility import row_utilities, db_utils

use_custom_titlebar = True if sg.running_trinket() else False


def make_window(max_cost, max_mass, max_disp, max_time, cost_coef, mass_coef, disp_coef, time_coef, response):
    sg.theme('Default')

    # NOTE that we're using our own LOCAL Menu element
    if use_custom_titlebar:
        Menu = sg.MenubarCustom
    else:
        Menu = sg.Menu

    rows, bids = row_utilities.create_rows(max_cost, max_mass, max_disp, max_time, cost_coef, mass_coef, disp_coef, time_coef, response)

    # Note - LOCAL Menu element is used (see about for how that's defined)
    layout = [[Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]], k='-CUST MENUBAR-', p=0)],
              [sg.T('Lockheed Martin Demo GUI', font='_ 14', justification='c', expand_x=True)],
              [sg.Frame('', rows)]]

    window = sg.Window('LMCO Demo', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
                       keep_on_top=True, use_custom_titlebar=use_custom_titlebar)  # Show 30% complete on ProgressBar

    for i, bid in enumerate(bids):
        plan = db_utils.getSpecificPlan(bid["ProcessPlan"])
        window['-CBAR-'+str(i)].update(bid["cost"])
        window['-MBAR-'+str(i)].update(plan["NetGrams"])
        window['-TBAR-'+str(i)].update(bid["leadTime"])
        window['-DBAR-'+str(i)].update(plan["Displacement"])
    return window
