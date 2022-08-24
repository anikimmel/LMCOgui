import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


# VARS CONSTS:
_VARS = {'window': False,
         'fig_agg': False,
         'pltFig': False}

# Theme for pyplot
plt.style.use('Solarize_Light2')


# Helper Functions
def update_annot(ind, annot, sc, names, im, ab, imgs):
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    ab.xy = pos
    annot.set_text(str(names[ind["ind"][0]]))
    im.set_data(plt.imread(str(imgs[(ind["ind"][0])])))
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event, annot, sc, fig, ax, names, img, ab, imgs):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind, annot, sc, names, img, ab, imgs)
            annot.set_visible(True)
            ab.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                ab.set_visible(False)
                fig.canvas.draw_idle()


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)
    return figure_canvas_agg


class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)


# \\  -------- PYSIMPLEGUI -------- //

AppFont = 'Any 16'
sg.theme('black')


def getData(bids, x_select, y_select):
    if x_select == 'Displacement':
        x_select = 'disp'
    if y_select == 'Displacement':
        y_select = 'disp'
    return [bid[x_select.lower()] for bid in bids], [bid[y_select.lower()] for bid in bids], \
           [bid["link"] for bid in bids], [bid["color"] for bid in bids], [bid["pic"] for bid in bids]


def drawChart(bids, x_select, y_select):
    layout = [[sg.T('Controls:'), sg.Canvas(key='controls_cv'), sg.Push(),
                     sg.Button('Back to Options List', enable_events=True, key='backtoresults')],
              [sg.Column(
                    layout=[
                        [sg.Canvas(key='fig_cv',
                                   # it's important that you set this size
                                   size=(400 * 2, 400)
                                   )]
                    ],
                    background_color='#DAE0E6',
                    pad=(0, 0))],
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
                                element_justification="center")
    _VARS['pltFig'] = plt.figure()
    dataXY = getData(bids, x_select, y_select)
    x = dataXY[0]
    y = dataXY[1]
    names = dataXY[2]
    colors = dataXY[3]
    imgs = dataXY[4]
    im = OffsetImage(plt.imread(str(imgs[0])))
    fig, ax = plt.subplots()
    sc = plt.scatter(x, y, c=colors, s=36, edgecolors='black')
    annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    xybox = (75., -75.)
    ab = AnnotationBbox(im, (0, 0), xybox=xybox, xycoords='data',
                        boxcoords="offset points", pad=0.3, arrowprops=dict(arrowstyle="->"))
    ax.add_artist(ab)
    ab.set_visible(False)
    annot.set_visible(False)
    fig.canvas.mpl_connect("motion_notify_event", lambda event: hover(event, annot, sc, fig, ax, names, im, ab, imgs))
    plt.xlabel(x_select)
    plt.ylabel(y_select)
    DPI = fig.get_dpi()
    fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
    _VARS['fig_agg'] = draw_figure_w_toolbar(_VARS['window']['fig_cv'].TKCanvas, fig, _VARS['window']['controls_cv'].TKCanvas)
    return _VARS['window']


def updateChart(bids, x_select, y_select):
    _VARS['fig_agg'].get_tk_widget().forget()
    plt.clf()
    dataXY = getData(bids, x_select, y_select)
    x = dataXY[0]
    y = dataXY[1]
    names = dataXY[2]
    colors = dataXY[3]
    imgs = dataXY[4]
    im = OffsetImage(plt.imread(str(imgs[0])))
    fig, ax = plt.subplots()
    sc = plt.scatter(x, y, c=colors, s=36, edgecolors='black')
    annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)
    xybox = (75., -75.)
    ab = AnnotationBbox(im, (0, 0), xybox=xybox, xycoords='data',
                        boxcoords="offset points", pad=0.3, arrowprops=dict(arrowstyle="->"))
    ax.add_artist(ab)
    ab.set_visible(False)
    fig.canvas.mpl_connect("motion_notify_event", lambda event: hover(event, annot, sc, fig, ax, names, im, ab, imgs))
    plt.xlabel(x_select)
    plt.ylabel(y_select)
    DPI = fig.get_dpi()
    fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
    _VARS['fig_agg'] = draw_figure_w_toolbar(_VARS['window']['fig_cv'].TKCanvas, fig, _VARS['window']['controls_cv'].TKCanvas)
