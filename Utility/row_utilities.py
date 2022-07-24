import PySimpleGUI as sg

NAME_SIZE = 20


def name(name):
    dots = NAME_SIZE - len(name) - 2
    return sg.Text(name + ' ' + '•' * dots, size=(NAME_SIZE, 1), justification='r', pad=(0, 0), font='Courier 10')


def create_rows(max_cost, max_mass, max_disp, max_time, cost_coef, mass_coef, disp_coef, time_coef, response, dataMaxes):
    final_bids = []
    for bid in response:
        if (bid["cost"] > max_cost) or (bid["time"] > max_time) or (bid["mass"] > max_mass):
            continue
        score = generate_score(cost_coef, mass_coef, disp_coef, time_coef, bid["cost"],
                               bid["time"], bid["mass"], 0.05, dataMaxes)

        layout_bars = [[name('Cost'), sg.ProgressBar(dataMaxes["cost"], orientation='h', s=(10, 20),
                                                     k=('-CBAR-'+bid["link"]), bar_color=("blue", "grey"))],
                       [name('Time'), sg.ProgressBar(dataMaxes["time"], orientation='h', s=(10, 20),
                                                     k=('-TBAR-'+bid["link"]), bar_color=("blue", "grey"))],
                       [name('Mass'), sg.ProgressBar(dataMaxes["mass"], orientation='h', s=(10, 20),
                                                     k=('-MBAR-'+bid["link"]), bar_color=("blue", "grey"))],
                       [name('Displacement'), sg.ProgressBar(0.1, orientation='h', s=(10, 20),
                                                             k=('-DBAR-'+bid["link"]), bar_color=("blue", "grey"))]]

        layout_buttons = [
            [sg.Col([[sg.Button('Design File'), sg.Button('Supplier Info')]])],
            [sg.Col([[sg.Button('Process Plan'), sg.Button('Initiate Contract', button_color='green')]])]
        ]

        score_color = getScoreColor(float(score))
        layout_c = [sg.Image(sg.EMOJI_BASE64_HAPPY_THUMBS_UP),
                    sg.Pane([sg.Col([[sg.T('Score' + '\n' + str(round(score, 2)), justification='c',
                                           background_color=score_color)]], background_color=score_color)],
                            background_color=score_color),
                    sg.Col(layout_bars), sg.Col(layout_buttons)]

        content = [sg.Frame(bid["link"], [[sg.Col([layout_c], p=20, vertical_alignment='t')]], border_width=3)]
        bid["score"] = score
        bid["content"] = content
        final_bids.append(bid)
    return final_bids


def generate_score(cost_coef, mass_coef, disp_coef,
                   time_coef, cost, time, mass, displacement, dataMaxes):
    return 100*(cost_coef * (dataMaxes["cost"]-cost)/dataMaxes["cost"]
                + mass_coef * (dataMaxes["mass"]-mass)/dataMaxes["mass"]
                + time_coef * (dataMaxes["time"]-time)/dataMaxes["time"]
                + disp_coef * (0.1-displacement))


def sortRows(final_bids, value):
    reverse_val = False
    if value == "score":
        reverse_val = True
    rows = sorted(final_bids, key=lambda d: d[value], reverse=reverse_val)
    return [row["content"] for row in rows]


def getScoreColor(score):
    if score >= 90:
        return "dark green"
    if score >= 80:
        return "lime green"
    if score >= 70:
        return "OliveDrab1"
    if score >= 60:
        return"yellow"
    if score >= 50:
        return "tan1"
    if score >= 40:
        return "orange"
    if score >= 30:
        return "orange red"
    if score >= 20:
        return "red"
    if score >= 10:
        return "red4"
    return "maroon"
