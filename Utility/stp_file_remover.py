import os

dir_name = "C:\\Users\\akimmel\\PycharmProjects\\LMCOgui\\Utility\\Data\\executable-win\\executable-win\\data\\burak-initial-dataset-v4-zbr\\Generative_Design_Data\\"
test = os.listdir(dir_name)

for part in test:
    part_dir = dir_name + str(part)
    for file in os.listdir(part_dir):
        if file.endswith(".stp") or file.endswith(".step"):
            os.remove(os.path.join(part_dir, file))
