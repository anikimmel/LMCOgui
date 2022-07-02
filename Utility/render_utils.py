import PySimpleGUI as sg
import os.path


def getDesigns():
    designs = []
    max_cost = 0
    max_time = 0
    max_weight = 0
    for design in designs:
        for process in design.processes:
            if process.weight > max_weight:
                max_weight = process.weight
            if process.cost > max_cost:
                max_cost = process.cost
            if process.time > max_time:
                max_time = process.time
    return designs, max_cost, max_time, max_weight



