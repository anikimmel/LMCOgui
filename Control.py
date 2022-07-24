import init_screen
import results_screen
from Utility import init_utilities, MaterialTypes, MachiningTypes, Suppliers, db_utils, slider_utilities
import PySimpleGUI as sg
import slider_screen
import subprocess

subprocess.Popen(["C:\\Users\\Annie\\PycharmProjects\\LMCOgui\\Utility\\Data\\executable-win\\executable-win\\lmco.exe"])

if __name__ == '__main__':
    window = init_screen.make_window()
    preferences = []
    selectAllMat_cur = False
    selectAllMan_cur = False
    selectAllBus_cur = False
    results = []
    dataMaxes = {}
    parameters = []
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'SelectAllMaterials':
            selectAllMat_cur = not selectAllMat_cur
            for material in MaterialTypes.materials:
                window[material].update(selectAllMat_cur)

        if event == 'SelectAllManufacturing':
            selectAllMan_cur = not selectAllMan_cur
            for machineType in MachiningTypes.machiningTypes:
                window[machineType].update(selectAllMan_cur)

        if event == 'SelectAllBusinesses':
            selectAllBus_cur = not selectAllBus_cur
            for business in Suppliers.suppliers:
                window[business].update(selectAllBus_cur)

        if event == 'Edit Me':
            sg.execute_editor(__file__)

        if event == 'nextwindow':
            preferences = init_utilities.save_preferences(values)
            design = values['design_option']
            results, dataMaxes = db_utils.getBids(design, preferences,
                                       values['quantity'], values['-CALStart-'], values['-CALEnd-'])
            window.close()
            window = slider_screen.make_window('DarkTeal12')

        if event == 'generateoptions':
            parameters = slider_utilities.generate_parameters(values)
            window.close()
            window = results_screen.make_window(parameters, results, dataMaxes)

        if event == 're-sort':
            sort_on = ""
            if values['sort_design_options'] == 'Highest Score':
                sort_on = "score"
                default_val = 'Highest Score'
            if values['sort_design_options'] == 'Fastest':
                sort_on = "time"
                default_val = 'Fastest'
            if values['sort_design_options'] == 'Cheapest':
                sort_on = "cost"
                default_val = 'Cheapest'
            if values['sort_design_options'] == 'Lightest':
                sort_on = "mass"
                default_val = 'Lightest'
            window.close()
            window = results_screen.make_window(parameters, results, dataMaxes, sort_on, default_val)

    window.close()
