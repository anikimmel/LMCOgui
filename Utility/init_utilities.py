import PySimpleGUI as sg
from Utility import MachiningTypes
from Utility import MaterialTypes
from Utility import Suppliers


def save_preferences(values):
    materials = []
    manufacturing_methods = []
    businesses = []

    for material in MaterialTypes.materials:
        if values[material]:
            materials.append(material)

    for manufacturing in MachiningTypes.machiningTypes:
        if values[manufacturing]:
            manufacturing_methods.append(manufacturing)

    for business in Suppliers.suppliers:
        if values[business]:
            businesses.append(business)

    return materials, manufacturing_methods, businesses


def create_checkboxes(options, category):
    checkboxes = [[sg.Checkbox('Select All', key='SelectAll' + category, enable_events=True)]]
    for option in options:
        if option == "Supplier-A":
            checkboxes.append([sg.Checkbox(option + " (only subtractive)", key=option, enable_events=True)])
        elif option == "Supplier-B":
            checkboxes.append([sg.Checkbox(option + " (only additive)", key=option, enable_events=True)])
        else:
            checkboxes.append([sg.Checkbox(option, key=option, enable_events=True)])
    return checkboxes
