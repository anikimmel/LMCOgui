import init_screen
from Utility import init_utilities
import PySimpleGUI as sg
import os
import slider_screen
import row_test

if __name__ == '__main__':
    window = init_screen.make_window()
    preferences = []
    while True:
        event, values = window.read()
        # sg.Print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'SelectAllMaterials':
            for i in range(9):
                window['matcheck' + str(i)].update(True)

        if event == 'SelectAllManufacturing':
            for i in range(6):
                window['mancheck' + str(i)].update(True)

        if event == 'SelectAllBusinesses':
            for i in range(2):
                window['buscheck' + str(i)].update(True)

        if event == 'Edit Me':
            sg.execute_editor(__file__)

        if event == 'nextwindow':
            preferences = init_utilities.save_preferences(values)
            window.close()
            window = slider_screen.make_window('DarkTeal12')

        if event == 'generateoptions':
            window.close()
            window = row_test.make_window()

        elif event == 'Version':
            sg.popup_scrolled(sg.get_versions(), __file__, keep_on_top=True, non_blocking=True)
            # Folder name was filled in, make a list of files in the folder
            if event == "-FOLDER-":
                folder = values["-FOLDER-"]
                try:
                    # Get list of files in folder
                    file_list = os.listdir(folder)
                except:
                    file_list = []

                fnames = [
                    f
                    for f in file_list
                    if os.path.isfile(os.path.join(folder, f))
                       and f.lower().endswith((".png", ".gif"))
                ]
                window["-FILE LIST-"].update(fnames)
            elif event == "-FILE LIST-":  # A file was chosen from the listbox
                try:
                    filename = os.path.join(
                        values["-FOLDER-"], values["-FILE LIST-"][0]
                    )
                    window["-TOUT-"].update(filename)
                    window["-IMAGE-"].update(filename=filename)
                except:
                    pass
    window.close()
