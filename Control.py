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
            results = db_utils.construct_request(design, preferences,
                                                 values['quantity'], values['-CALStart-'], values['-CALEnd-'])
            window.close()
            window = slider_screen.make_window('DarkTeal12')

        if event == 'generateoptions':
            parameters = slider_utilities.generate_parameters(values)
            window.close()
            window = results_screen.make_window(parameters, results)
    window.close()
