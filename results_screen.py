import PySimpleGUI as sg
from Utility import row_utilities

use_custom_titlebar = True if sg.running_trinket() else False


def make_window(max_cost, max_mass, max_disp, max_time, cost_coef, mass_coef, disp_coef, time_coef, response):
    sg.theme('Default')

    # NOTE that we're using our own LOCAL Menu element
    if use_custom_titlebar:
        Menu = sg.MenubarCustom
    else:
        Menu = sg.Menu

    rows = row_utilities.create_rows(max_cost, max_mass, max_disp, max_time, cost_coef, mass_coef, disp_coef, time_coef, response)

    # Note - LOCAL Menu element is used (see about for how that's defined)
    layout = [[Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]], k='-CUST MENUBAR-', p=0)],
              [sg.T('Lockheed Martin Demo GUI', font='_ 14', justification='c', expand_x=True)],
              [sg.Frame('', rows)]]

    window = sg.Window('LMCO Demo', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
                       keep_on_top=True, use_custom_titlebar=use_custom_titlebar)  # Show 30% complete on ProgressBar
    window['-CBAR-'].update(30)
    window['-MBAR-'].update(70)
    window['-TBAR-'].update(50)
    return window


# window = make_window()

# while True:
#     event, values = window.read()
#     # sg.Print(event, values)
#     if event == sg.WIN_CLOSED or event == 'Exit':
#         break
#
#     if event == 'SelectAllMaterials':
#         for i in range(9):
#             window['matcheck' + str(i)].update(True)
#
#     if event == 'SelectAllManufacturing':
#         for i in range(6):
#             window['mancheck' + str(i)].update(True)
#
#     if event == 'SelectAllBusinesses':
#         for i in range(4):
#             window['buscheck' + str(i)].update(True)
#
#     if event == 'Edit Me':
#         sg.execute_editor(__file__)
#
#     elif event == 'Version':
#         sg.popup_scrolled(sg.get_versions(), __file__, keep_on_top=True, non_blocking=True)
#         # Folder name was filled in, make a list of files in the folder
#         if event == "-FOLDER-":
#             folder = values["-FOLDER-"]
#             try:
#                 # Get list of files in folder
#                 file_list = os.listdir(folder)
#             except:
#                 file_list = []
#
#             fnames = [
#                 f
#                 for f in file_list
#                 if os.path.isfile(os.path.join(folder, f))
#                    and f.lower().endswith((".png", ".gif"))
#             ]
#             window["-FILE LIST-"].update(fnames)
#         elif event == "-FILE LIST-":  # A file was chosen from the listbox
#             try:
#                 filename = os.path.join(
#                     values["-FOLDER-"], values["-FILE LIST-"][0]
#                 )
#                 window["-TOUT-"].update(filename)
#                 window["-IMAGE-"].update(filename=filename)
#             except:
#                 pass
# window.close()
