import PySimpleGUI as sg

from Utility import MachiningTypes
from Utility import MaterialTypes
from Utility import Suppliers
from Utility import init_utilities

use_custom_titlebar = True if sg.running_trinket() else False


def make_window(theme=None):
    sg.theme('DarkTeal12')

    # NOTE that we're using our own LOCAL Menu element
    if use_custom_titlebar:
        Menu = sg.MenubarCustom
    else:
        Menu = sg.Menu

    layout_l = [sg.Frame('Materials Selection',
                         init_utilities.create_checkboxes(MaterialTypes.materials, "Materials"),
                         border_width=3)]

    layout_c = [sg.Frame('Manufacturing Method(s)',
                         init_utilities.create_checkboxes(MachiningTypes.machiningTypes, "Manufacturing"),
                         border_width=3)]

    layout_r = [sg.Frame('Business Preferences',
                         init_utilities.create_checkboxes(Suppliers.suppliers, "Businesses"),
                         border_width=3)]

    # Note - LOCAL Menu element is used (see about for how that's defined)
    layout = [[Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]], k='-CUST MENUBAR-', p=0)],
              [sg.T('Lockheed Martin Demo GUI', font='_ 14', justification='c', expand_x=True)],
              [sg.HSep()],
              [sg.Text("Select Part: "), sg.OptionMenu(['Bracket'], s=(15, 2), key='design_option'),
               sg.Text("Quantity: "), sg.Input(s=15, key='quantity')],
              [sg.CalendarButton('Earliest Start Date', target='-CALStart-', pad=None,
                                 font=('MS Sans Serif', 10, 'bold'), key='_CALENDAR_S_'),
               sg.In(key='-CALStart-', enable_events=True, visible=True, s=(25, 3)),
               sg.CalendarButton('Due Date', target='-CALEnd-', pad=None,
                                 font=('MS Sans Serif', 10, 'bold'), key='_CALENDAR_E_'),
               sg.In(key='-CALEnd-', enable_events=True, visible=True, s=(25, 3))],
              [sg.HSep()],
              [sg.Col([layout_l], p=20, vertical_alignment='t'), sg.Col([layout_c], p=20, vertical_alignment='t'),
               sg.Col([layout_r], p=20, vertical_alignment='t')],
              [[sg.Push(), sg.Button('Next >>', key='nextwindow')]]]

    window = sg.Window('LMCO Demo', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT,
                       keep_on_top=True, use_custom_titlebar=use_custom_titlebar)  # Show 30% complete on ProgressBar

    return window
