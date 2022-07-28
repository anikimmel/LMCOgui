import PySimpleGUI as sg
import numpy as np

"""
    Embedding the Matplotlib toolbar into your application
"""

# ------------------------------- This is to include a matplotlib figure in a Tkinter canvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def update_annot(ind):
    pos = sc.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))),
                           " ".join([names[n] for n in ind["ind"]]))
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = sc.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()


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


class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)


# ------------------------------- PySimpleGUI CODE

layout = [
    [sg.B('Plot'), sg.B('Exit')],
    [sg.T('Controls:')],
    [sg.Canvas(key='controls_cv')],
    [sg.T('Figure:')],
    [sg.Column(
        layout=[
            [sg.Canvas(key='fig_cv',
                       # it's important that you set this size
                       size=(400 * 2, 400)
                       )]
        ],
        background_color='#DAE0E6',
        pad=(0, 0)
    )],
    [sg.B('Alive?')]

]

window = sg.Window('Graph with controls', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):  # always,  always give a way out!
        break
    elif event is 'Plot':
        x = np.random.rand(15)
        y = np.random.rand(15)
        names = np.array(list("ABCDEFGHIJKLMNO"))
        c = np.random.randint(1, 5, size=15)

        norm = plt.Normalize(1, 4)
        cmap = plt.cm.RdYlGn

        fig, ax = plt.subplots()
        sc = plt.scatter(x, y, c=c, s=100, norm=norm)

        annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="w"),
                            arrowprops=dict(arrowstyle="->"))
        annot.set_visible(False)
        fig.canvas.mpl_connect("motion_notify_event", hover)
        # ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE
        #plt.figure(1)
        #fig = plt.gcf()
        DPI = fig.get_dpi()
        # ------------------------------- you have to play with this size to reduce the movement error when the mouse hovers over the figure, it's close to canvas size
        fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
        # -------------------------------
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid()

        # ------------------------------- Instead of plt.show()
        draw_figure_w_toolbar(window['fig_cv'].TKCanvas, fig, window['controls_cv'].TKCanvas)

window.close()