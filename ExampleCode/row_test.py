import PySimpleGUI as sg
import os.path

use_custom_titlebar = True if sg.running_trinket() else False


def make_window(theme=None):
    sg.theme('Default')

    NAME_SIZE = 20

    def name(name):
        dots = NAME_SIZE - len(name) - 2
        return sg.Text(name + ' ' + '•' * dots, size=(NAME_SIZE, 1), justification='r', pad=(0, 0), font='Courier 10')

    # NOTE that we're using our own LOCAL Menu element
    if use_custom_titlebar:
        Menu = sg.MenubarCustom
    else:
        Menu = sg.Menu

    layout_l = [sg.Image(sg.EMOJI_BASE64_HAPPY_THUMBS_UP)]

    layout_bars = [[name('Cost'), sg.ProgressBar(100, orientation='h', s=(10, 20), k='-CBAR-')],
                         [name('Time'), sg.ProgressBar(100, orientation='h', s=(10, 20), k='-TBAR-')],
                         [name('Material'), sg.ProgressBar(100, orientation='h', s=(10, 20), k='-MBAR-')]]
    layout_buttons = [
                [sg.Col([[sg.Button('Design File'), sg.Button('Supplier Info')]])],
                [sg.Col([[sg.Button('Process Plan'), sg.Button('Initiate Contract', button_color='green')]])]
    ]

    layout_c = [sg.Pane([sg.Col([[sg.T('Score' + '\n' + '78', justification='c', background_color='green')]], background_color='green')], background_color='green'),
                sg.Col(layout_bars), sg.Col(layout_buttons)]

    content = [[sg.Text("TruventorSolutions –Aluminium 6082 –3 axis CNC")],
              [sg.Col([layout_l], p=20, vertical_alignment='t'),
                sg.Col([layout_c], p=20, vertical_alignment='t')]]

    # Note - LOCAL Menu element is used (see about for how that's defined)
    layout = [[Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]], k='-CUST MENUBAR-', p=0)],
              [sg.T('Lockheed Martin Demo GUI', font='_ 14', justification='c', expand_x=True)],
              [sg.Frame('', content)],

              ]

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
