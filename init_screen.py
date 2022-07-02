import PySimpleGUI as sg
import os.path


use_custom_titlebar = True if sg.running_trinket() else False


def generate_checkboxes(options, type):
    boxes = []
    i = 0
    for option in options:
        boxes.append([sg.Text(option)])
        boxes.append([sg.Text('')])
        for kind in option:
            boxes.append([sg.Checkbox(kind, type+str(i), enable_events=True)])


def load_options(info):
    layout_l = [sg.Frame('Materials Selection', generate_checkboxes(info['materials'], 'mat'), border_width=3)]
    layout_c = [sg.Frame('Manufacturing Methods', generate_checkboxes(info['manufacturing'], 'man'), border_width=3)]
    layout_r = [sg.Frame('Business Preferences', generate_checkboxes(info['businesses'], 'bus'), border_width=3)]
    return layout_l, layout_c, layout_r


def make_window(theme=None):
    sg.theme('DarkTeal12')

    # NOTE that we're using our own LOCAL Menu element
    if use_custom_titlebar:
        Menu = sg.MenubarCustom
    else:
        Menu = sg.Menu

    file_list_column = [
        [
            sg.Text("Design File(s)"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ]
    ]

    layout_l, layout_c, layout_r = load_options(info)

    # Note - LOCAL Menu element is used (see about for how that's defined)
    layout = [[Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]], k='-CUST MENUBAR-', p=0)],
              [sg.T('Lockheed Martin Demo GUI', font='_ 14', justification='c', expand_x=True)],
              [sg.Col(file_list_column)],
              [sg.Col([layout_l], p=20, vertical_alignment='t'), sg.Col([layout_c], p=20, vertical_alignment='t'),
               sg.Col([layout_r], p=20, vertical_alignment='t')],
              [[sg.Push(), sg.Button('Next >>')]]]

    window = sg.Window('LMCO Demo', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
                       keep_on_top=True, use_custom_titlebar=use_custom_titlebar)  # Show 30% complete on ProgressBar

    return window


window = make_window()

while True:
    event, values = window.read()
    prev_SelAllMat = False
    prev_SelAllMan = False
    prev_SelAllBus = False

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'SelectAllMaterials':
        for i in range(9):
            window['matcheck' + str(i)].update(not prev_SelAllMat)

    if event == 'SelectAllManufacturing':
        for i in range(6):
            window['mancheck' + str(i)].update(not prev_SelAllMan)

    if event == 'SelectAllBusinesses':
        for i in range(4):
            window['buscheck' + str(i)].update(not prev_SelAllBus)

    if event == 'Edit Me':
        sg.execute_editor(__file__)

    elif event == 'Version':
        sg.popup_scrolled(sg.get_versions(), __file__, keep_on_top=True, non_blocking=True)
        # Folder name was filled in, make a list of files in the folder
        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                # Get list of files in folder
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                   and f.lower().endswith((".png", ".gif"))
            ]
            window["-FILE LIST-"].update(fnames)
        elif event == "-FILE LIST-":  # A file was chosen from the listbox
            try:
                filename = os.path.join(
                    values["-FOLDER-"], values["-FILE LIST-"][0]
                )
                window["-TOUT-"].update(filename)
                window["-IMAGE-"].update(filename=filename)
            except:
                pass
window.close()