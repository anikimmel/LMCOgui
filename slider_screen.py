import PySimpleGUI as sg

use_custom_titlebar = True if sg.running_trinket() else False


def make_window(theme=None):

    NAME_SIZE = 23


    def name(name):
        dots = NAME_SIZE-len(name)-2
        return sg.Text(name + ' ' + '•'*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')

    sg.theme(theme)

    # NOTE that we're using our own LOCAL Menu element
    if use_custom_titlebar:
        Menu = sg.MenubarCustom
    else:
        Menu = sg.Menu

    layout_l = [
                [sg.Text('Multi-Objective Parameters')],
                [sg.Text('You may specify weights on various performance objectives.')],
                [name('Manufacturing Costs'), sg.Slider((0.0, 1.0), orientation='h', resolution=0.1, enable_events=True, tick_interval=0.2)],
                [name('Design Mass'), sg.Slider((0.0, 1.0), orientation='h', resolution=0.1, enable_events=True, tick_interval=0.2)],
                [name('Design Volume'), sg.Slider((0.0, 1.0), orientation='h', resolution=0.1, enable_events=True, tick_interval=0.2)],
                [name('Production Time'), sg.Slider((0.0, 1.0), orientation='h', resolution=0.1, enable_events=True, tick_interval=0.2)],
                [name('Lead Time'), sg.Slider((0.0, 1.0), orientation='h', resolution=0.1, enable_events=True, tick_interval=0.2)]

    ]

    layout_r = [
                [sg.Text('Optimization Constraints')],
                [sg.Text('You may specify constraints which will be used for defining the optimization space.')],
                [name('Max Mfg. Costs ($)'), sg.Input(s=7)],
                [name('Max Mass (kg)'), sg.Input(s=7)],
                [name('Max Volume (m^3)'), sg.Input(s=7)],
                [name('Max Prod. Time (hrs)'), sg.Input(s=7)],
                [name('Max Lead Time (days)'), sg.Input(s=7)]
    ]

    # Note - LOCAL Menu element is used (see about for how that's defined)
    layout = [[Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
              [sg.T('Generative Manufacturing Optimizer Tool', font='_ 14', justification='c', expand_x=True)],
              [sg.Col(layout_l, p=30), sg.Col(layout_r, p=30)],
              [[sg.Push(), sg.Button('Generate Options >>', key='generateoptions')]]]

    window = sg.Window('The PySimpleGUI Element List', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True, use_custom_titlebar=use_custom_titlebar)

    # window['-PBAR-'].update(30)                                                     # Show 30% complete on ProgressBar
    # window['-GRAPH-'].draw_image(data=sg.EMOJI_BASE64_HAPPY_JOY, location=(0,50))   # Draw something in the Graph Element

    return window
#
#
# window = make_window()
#
# while True:
#     event, values = window.read()
#     # sg.Print(event, values)
#     if event == sg.WIN_CLOSED or event == 'Exit':
#         break
#     # if event == 'Edit Me':
#     #     sg.execute_editor(__file__)
#     # if values['-COMBO-'] != sg.theme():
#     #     sg.theme(values['-COMBO-'])
#     #     window.close()
#     #     window = make_window()
#     # if event == '-USE CUSTOM TITLEBAR-':
#     #     use_custom_titlebar = values['-USE CUSTOM TITLEBAR-']
#     #     sg.set_options(use_custom_titlebar=use_custom_titlebar)
#     #     window.close()
#     #     window = make_window()
#     # elif event == 'Version':
#     #     sg.popup_scrolled(sg.get_versions(), __file__, keep_on_top=True, non_blocking=True)
# window.close()
#
#
