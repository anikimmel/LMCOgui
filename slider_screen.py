import PySimpleGUI as sg

use_custom_titlebar = True if sg.running_trinket() else False


def make_window(dataMaxes, theme=None, prev_values=None):

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
                [sg.Text('Evaluation Factors', font='Any 12 underline bold')],
                [sg.Text('You may specify weights on various evaluation factors.')],
                [sg.Text('If all sliders are set to 0, the objective function will use equal weights for every parameter.')],
                [name('Manufacturing Costs'),
                 sg.Slider((0.0, 1.0), orientation='h', resolution=0.1, enable_events=True, tick_interval=0.2,
                           key="costs_coef")],
                [name('Design Mass'),
                 sg.Slider((0.0, 1.0), orientation='h', resolution=0.1, enable_events=True, tick_interval=0.2,
                           key="mass_coef")],
                [name('Max Displacement'),
                 sg.Slider((0.0, 1.0), orientation='h', resolution=0.1, enable_events=True, tick_interval=0.2,
                           key="displacement_coef")],
                [name('Lead Time'),
                 sg.Slider((0.0, 1.0), orientation='h', resolution=0.1, enable_events=True, tick_interval=0.2,
                           key="time_coef")]

    ]

    layout_r = [
                [sg.Text('Filtering Constraints', font='Any 12 underline bold')],
                [sg.Text('You may specify constraints which will be used for defining the optimization space.')],
                [sg.Text('If a maximum is unspecified then that parameter will be unconstrained.')],
                [name('Max Mfg. Costs ($)'), sg.Input(s=7, key="costs_max"),
                 sg.Text("Data Maximum: $" + str(dataMaxes["cost"]))],
                [name('Max Mass (kg)'), sg.Input(s=7, key="mass_max"),
                 sg.Text("Data Maximum: " + str(round(dataMaxes["mass"]/1000, 3)) + " (kg)")],
                [name('Max Displacement (mm)'), sg.Input(s=7, key="displacement_max"),
                 sg.Text("Data Maximum: " + str(round(dataMaxes["disp"], 3)) + " (mm)")],
                [name('Max Lead Time (days)'), sg.Input(s=7, key="time_max"),
                 sg.Text("Data Maximum: " + str(round(dataMaxes["time"]/(24*60*60), 2)) + " (days)")],
                [sg.Button("No Constraints", key='usealloptions', enable_events=True)]
    ]

    # Note - LOCAL Menu element is used (see about for how that's defined)
    layout = [[Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
              [sg.T('Generative Manufacturing Optimizer Tool', font='_ 14', justification='c', expand_x=True)],
              [sg.HSep()],
              [sg.Button('View Machine Graph', key='agents', enable_events=True),
               sg.Button('View Lots Graph', key='lots', enable_events=True)],
              [sg.Col(layout_l, p=30), sg.Col(layout_r, p=30)],
              [sg.Button('<< Go Back', key='backtoinit', enable_events=True), sg.Push(),
               sg.Button('Generate Options >>', key='generateoptions')]]

    window = sg.Window('The PySimpleGUI Element List', layout, finalize=True,
                       right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True,
                       use_custom_titlebar=use_custom_titlebar, element_justification='c')
    if prev_values:
        window.Element('costs_max').update(value=prev_values["costs_max"])
        window.Element('mass_max').update(value=prev_values["mass_max"])
        window.Element('displacement_max').update(value=prev_values["displacement_max"])
        window.Element('time_max').update(value=prev_values["time_max"])
        window.Element('costs_coef').update(value=prev_values["costs_coef"])
        window.Element('mass_coef').update(value=prev_values["mass_coef"])
        window.Element('displacement_coef').update(value=prev_values["displacement_coef"])
        window.Element('time_coef').update(value=prev_values["time_coef"])

    return window
