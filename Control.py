import init_screen
import results_screen
from Utility import init_utilities, MaterialTypes, MachiningTypes, Suppliers, db_utils, slider_utilities
import PySimpleGUI as sg
import slider_screen
import subprocess
import graph_screen

subprocess.Popen(
    ["C:\\Users\\akimmel\\PycharmProjects\\LMCOgui\\Utility\\Data\\executable-win\\executable-win\\lmco.exe"])

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

        ##---INIT SCREEN CONTROLS---##
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
            output = db_utils.getBids(design, preferences, values['quantity'], values['-CALStart-'], values['-CALEnd-'])
            if len(output) != 2:
                sg.popup(str(output) + "Please select new options.", title="Select new options", keep_on_top=True)
            else:
                results = output[0]
                dataMaxes = output[1]
                window.close()
                window = slider_screen.make_window(dataMaxes, 'DarkTeal12')

        ##---SLIDER SCREEN CONTROLS---##
        if event == 'generateoptions':
            parameters = slider_utilities.generate_parameters(values)
            window.close()
            window = results_screen.make_window(parameters, results, dataMaxes)

        ##---RESULTS SCREEN CONTROLS---##
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
        if event == "graphs":
            window.close()
            window = graph_screen.drawChart(results, 'time', 'cost')
        if "supplier" in str(event):
            for bid in results:
                if bid["link"] == event[8:]:
                    sg.popup("Suppliers: " + str(bid["suppliers"]) + "\n"
                             + "Cost: " + str(bid["cost"]) + " ($)\n"
                             + "Mass: " + str(bid["mass"]) + " (g)\n"
                             + "Time: " + str(bid["time"]) + " (min)\n", title=bid["link"], keep_on_top=True)
                    break

        ##---GRAPH SCREEN CONTROLS---##
        if event == 'backtoresults':
            window.close()
            window = results_screen.make_window(parameters, results, dataMaxes)
        if event == 'viewgraph':
            x_sel = values["x_option"]
            y_sel = values["y_option"]
            graph_screen.updateChart(results, x_sel, y_sel)
    window.close()
