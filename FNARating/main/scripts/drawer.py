import random
import os


def get_background():
    PATH = os.getcwd()
    BG_PATH = os.path.join(PATH, 'main', 'static', 'img', 'backgrounds')

    bgs = os.listdir(BG_PATH)

    return random.choice(bgs)
