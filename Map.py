import math
import random


# build map of the game
def build_map(settings):
    tmp = []
    maplist = []

    # build a pair of data
    for i in range(0, settings.map_size, 2):
        # randomly generate 10 pairs of image element labels and store them in tmp
        e = math.ceil(random.random() * settings.img_num)
        # double append
        tmp.append(e)
        tmp.append(e)

    # shuffle
    for i in range(0, settings.map_size, 1):
        # store the image data in tmp randomly in map list
        index = int(random.random() * (settings.map_size - i))
        maplist.append(tmp[index])
        # delete image data in tmp
        tmp.pop(index)

    return maplist
