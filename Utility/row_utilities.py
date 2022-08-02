import PySimpleGUI as sg

NAME_SIZE = 20


def name(name):
    dots = NAME_SIZE - len(name) - 2
    return sg.Text(name + ' ' + '•' * dots, size=(NAME_SIZE, 1), justification='r', pad=(0, 0), font='Courier 10')


def create_rows(max_cost, max_mass, max_disp, max_time, cost_coef, mass_coef, disp_coef, time_coef, response, dataMaxes):
    final_bids = []
    for bid in response:
        if (bid["cost"] > max_cost) or (bid["time"] > max_time) or (bid["mass"] > max_mass) or bid["disp"] > max_disp:
            continue
        score = generate_score(cost_coef, mass_coef, disp_coef, time_coef, bid["cost"],
                               bid["time"], bid["mass"], bid["disp"], dataMaxes)

        layout_bars = [[name('Cost'), sg.ProgressBar(dataMaxes["cost"], orientation='h', s=(10, 20),
                                                     k=('-CBAR-'+bid["link"]),
                                                     bar_color=(getParamBarColor(cost_coef), "grey"))],
                       [name('Lead Time'), sg.ProgressBar(dataMaxes["time"], orientation='h', s=(10, 20),
                                                     k=('-TBAR-'+bid["link"]),
                                                     bar_color=(getParamBarColor(time_coef), "grey"))],
                       [name('Mass'), sg.ProgressBar(dataMaxes["mass"], orientation='h', s=(10, 20),
                                                     k=('-MBAR-'+bid["link"]),
                                                     bar_color=(getParamBarColor(mass_coef), "grey"))],
                       [name('Max Displacement'), sg.ProgressBar(dataMaxes["disp"], orientation='h', s=(10, 20),
                                                             k=('-DBAR-'+bid["link"]),
                                                             bar_color=(getParamBarColor(disp_coef), "grey"))]]

        layout_buttons = [
            [sg.Col([[sg.Button('Design File'),
                      sg.Button('Supplier Info', key=("supplier"+bid["link"]), enable_events=True)]])],
            [sg.Col([[sg.Button('Process Plan', key=("pplan"+bid["link"]), enable_events=True),
                      sg.Button('Initiate Contract', button_color='green')]])]
        ]

        score_color, hex = getScoreColor(float(score))
        layout_c = [sg.Image(sg.EMOJI_BASE64_HAPPY_THUMBS_UP),
                    sg.Pane([sg.Col([[sg.T('Score' + '\n' + str(round(score, 2)), justification='c',
                                           background_color=score_color)]], background_color=score_color)],
                            background_color=score_color),
                    sg.Col(layout_bars), sg.Col(layout_buttons)]

        content = [sg.Frame(bid["link"], [[sg.Col([layout_c], p=20, vertical_alignment='t')]], border_width=3)]
        bid["score"] = score
        bid["content"] = content
        bid["color"] = hex
        final_bids.append(bid)
    return final_bids


def generate_score(cost_coef, mass_coef, disp_coef,
                   time_coef, cost, time, mass, displacement, dataMaxes):
    return 100*(cost_coef * (dataMaxes["cost"]-cost)/dataMaxes["cost"]
                + mass_coef * (dataMaxes["mass"]-mass)/dataMaxes["mass"]
                + time_coef * (dataMaxes["time"]-time)/dataMaxes["time"]
                + disp_coef * (dataMaxes["disp"]-displacement)/dataMaxes["disp"])


def sortRows(final_bids, value):
    reverse_val = False
    if value == "score":
        reverse_val = True
    rows = sorted(final_bids, key=lambda d: d[value], reverse=reverse_val)
    return [row["content"] for row in rows]


def getScoreColor(score):
    if score >= 90:
        return "dark green", '#006400'
    if score >= 80:
        return "lime green", '#32CD32'
    if score >= 70:
        return "OliveDrab1", '#C0FF3E'
    if score >= 60:
        return"yellow", '#FFFF00'
    if score >= 50:
        return "tan1", '#FFA54F'
    if score >= 40:
        return "orange",  '#FFA500'
    if score >= 30:
        return "orange red", '#FF4500'
    if score >= 20:
        return "red", '#FF0000'
    if score >= 10:
        return "red4", '#8B0000'
    return "maroon", '#B03060'


def getParamBarColor(coef):
    if coef >= 0.75:
        return 'navy'
    if coef >= 0.5:
        return 'blue2'
    if coef >= 0.25:
        return 'dodger blue'
    return 'SteelBlue2'
