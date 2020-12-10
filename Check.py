import sys
import pygame
from pygame.locals import *

from Scan import v_scan, h_scan


# check if a pair of image can be cleared

def check_clear(points, settings, map_list):
    # if the two images are not identical, not clear
    if points[0].element != points[1].element:
        return False
    # find two identical images
    else:
        # the images can be cleared
        if v_scan(points, settings, map_list) is True or h_scan(points, settings, map_list) is True:
            return True
        # cannot be cleared
        else:
            return False


# check the click event

def click_event(button_list, settings, map_list):
    for i in pygame.event.get():
        if i.type == QUIT:
            sys.exit()
        # if click:
        if i.type == MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pos()
            for b in button_list:
                # get geometry
                g = b.geometry()
                g0 = g[0]
                g1 = g[1]
                g2 = g[2]
                g3 = g[3]
                # check if the click is on the image
                if g0 < click[0] < g0 + g2 and g1 < click[1] < g1 + g3:
                    # if the image is not cleared
                    if b.is_clickable():
                        if not b.click():
                            # if clicked itself
                            settings.temp_list.clear()
                            break
                        # if has already clicked one image
                        if settings.temp_list:
                            # add another image to the temp list
                            settings.temp_list.append(b)
                            # check if the two images are the same & can be cleared
                            if check_clear(settings.temp_list, settings, map_list):
                                # clear
                                for p in settings.temp_list:
                                    map_list[p.number] = 0
                                    p.number = 0
                                    p.delete()
                            else:
                                # can't be cleared, reset the images
                                for p in settings.temp_list:
                                    p.reset()
                            # clear images in temp list
                            settings.temp_list.clear()

                        # if hasn't clicked the first image
                        else:
                            # add first image to the temp list
                            settings.temp_list.append(b)

                    # stop checking
                    break


# check if all images are cleared
def all_cleared(map_list):
    for i in map_list:
        if i > 0:
            return False
    return True
