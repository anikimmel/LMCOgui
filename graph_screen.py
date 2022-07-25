import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# VARS CONSTS:
_VARS = {'window': False,
         'fig_agg': False,
         'pltFig': False}

dataSize = 1000

# Theme for pyplot
plt.style.use('Solarize_Light2')

# Helper Functions
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


# \\  -------- PYSIMPLEGUI -------- //

AppFont = 'Any 16'
sg.theme('black')


def getData(bids, x_select, y_select):
    if x_select == 'Displacement':
        x_select = 'disp'
    if y_select == 'Displacement':
        y_select = 'disp'
    return [bid[x_select.lower()] for bid in bids], [bid[y_select.lower()] for bid in bids]


def drawChart(bids, x_select, y_select):
    layout = [[sg.Button('Back to Options List', font=AppFont, enable_events=True, key='backtoresults')],
              [sg.Canvas(key='figCanvas', background_color='#FDF6E3')],
              [sg.Text("Select X"),
               sg.OptionMenu(['Time', 'Cost', 'Mass', 'Displacement'], s=(15, 2), key='x_option', default_value='Time'),
               sg.Text("Select Y"),
               sg.OptionMenu(['Time', 'Cost', 'Mass', 'Displacement'], s=(15, 2), key='y_option', default_value='Cost'),
               sg.Button('View Graph', font=AppFont, enable_events=True, key="viewgraph")]]
    _VARS['window'] = sg.Window('Such Window',
                                layout,
                                finalize=True,
                                resizable=True,
                                location=(100, 100),
                                element_justification="center",
                                background_color='#FDF6E3')
    _VARS['pltFig'] = plt.figure()
    dataXY = getData(bids, x_select, y_select)
    plt.plot(dataXY[0], dataXY[1], '.k')
    plt.xlabel(x_select)
    plt.ylabel(y_select)
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])
    return _VARS['window']


def updateChart(bids, x_select, y_select):
    _VARS['fig_agg'].get_tk_widget().forget()
    dataXY = getData(bids, x_select, y_select)
    plt.clf()
    plt.plot(dataXY[0], dataXY[1], '.k')
    plt.xlabel(x_select)
    plt.ylabel(y_select)
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])
