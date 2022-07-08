import PySimpleGUI as sg
import os.path

import slider_screen

use_custom_titlebar = True if sg.running_trinket() else False


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

    layout_l = [sg.Frame('Materials Selection', [
                [sg.Checkbox('Select All', key='SelectAllMaterials', enable_events=True)],
                [sg.Text('')],
                [sg.Text('Plastics')],
                [sg.Checkbox('ABS Basic', key='matcheck0', enable_events=True)],
                [sg.Checkbox('ABS 9012 (Food Grade)', key='matcheck1', enable_events=True)],
                [sg.Checkbox('PLA Basic', key='matcheck2', enable_events=True)],
                [sg.Checkbox('Acrylic', key='matcheck3', enable_events=True)],
                [sg.Text('')],
                [sg.Text('Metals')],
                [sg.Checkbox('Aluminium 6082', key='matcheck4', enable_events=True)],
                [sg.Checkbox('Aluminium 6061-T6', key='matcheck5', enable_events=True)],
                [sg.Checkbox('Mild Steel', key='matcheck6', enable_events=True)],
                [sg.Checkbox('Stainless Steel', key='matcheck7', enable_events=True)],
                [sg.Checkbox('Titanium Grade 1', key='matcheck8', enable_events=True)]], border_width=3)]

    layout_c  = [sg.Frame('Manufacturing Method(s)', [
                [sg.Checkbox('Select All', key='SelectAllManufacturing', enable_events=True)],
                [sg.Text('')],
                [sg.Text('Subtractive')],
                [sg.Checkbox('3 axis CNC', key='mancheck0', enable_events=True)],
                [sg.Checkbox('5 axis CNC', key='mancheck1', enable_events=True)],
                [sg.Text('')],
                [sg.Text('Additive')],
                [sg.Checkbox('SLM additive', key='mancheck2', enable_events=True)],
                [sg.Checkbox('Binder jet metal additive', key='mancheck3', enable_events=True)],
                [sg.Checkbox('FDM additive', key='mancheck4', enable_events=True)],
                [sg.Checkbox('Injection moulding', key='mancheck5', enable_events=True)]], border_width=3)]

    layout_r  = [sg.Frame('Business Preferences', [
                [sg.Checkbox('Select All', key='SelectAllBusinesses', enable_events=True)],
                [sg.Text('')],
                [sg.Text('Supplier Groups')],
                [sg.Checkbox('Supplier A', key='buscheck0', enable_events=True)],
                [sg.Checkbox('Supplier B', key='buscheck1', enable_events=True)],
                [sg.Checkbox('Key Supplier: Kolwjaha Co.', key='buscheck2', enable_events=True)]], border_width=3)]

    # Note - LOCAL Menu element is used (see about for how that's defined)
    layout = [[Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
              [sg.T('Lockheed Martin Demo GUI', font='_ 14', justification='c', expand_x=True)],
              [sg.Col(file_list_column)],
              [sg.Col([layout_l], p=20, vertical_alignment='t'), sg.Col([layout_c], p=20, vertical_alignment='t'), sg.Col([layout_r], p=20, vertical_alignment='t')],
              [[sg.Push(), sg.Button('Next >>', key='nextwindow')]]]

    window = sg.Window('LMCO Demo', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True, use_custom_titlebar=use_custom_titlebar)                                                   # Show 30% complete on ProgressBar

    return window
