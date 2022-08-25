import PIL
from PIL import Image
import os
from Utility import PathDefs


def resizeAndCrop(imgPath):

    im = Image.open(imgPath)

    # Get size
    x, y = im.size

    # New sizes
    yNew = 110
    xNew = 110 # should be equal


    # resize
    resizedImage = im.resize((int(xNew), int(yNew)), PIL.Image.ANTIALIAS)

    # save
    print("SAVE", imgPath)
    resizedImage.save(
        # "C:\\Users\\akimmel\\Downloads\\Generative_Design_Data\\Generative_Design_Data\\" + str(part) + "\\part110x110.png")
        PathDefs.design_path / str(part) / "part110x110.png")


for part in os.listdir(
        # "C:\\Users\\akimmel\\Downloads\\Generative_Design_Data\\Generative_Design_Data\\"
        PathDefs.design_path):
    resizeAndCrop(
        # "C:\\Users\\akimmel\\Downloads\\Generative_Design_Data\\Generative_Design_Data\\" + str(part) + "\\part.png"
        PathDefs.design_path / str(part) / "part.png")
