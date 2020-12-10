import time
import pygame

from Check import click_event, all_cleared
from ImageButton import ImageButton
from Map import build_map
from Settings import Settings

# settings Object
s = Settings()

# set the map and images
maps = []
images = []


def main():
    # initialize pygame, set screen and title
    pygame.init()
    pygame.display.set_caption(s.caption)
    screen = pygame.display.set_mode(s.screen_size, 0, 0)

    # build map list
    global maps
    maps = build_map(s)
    num = 0
    for m in maps:
        num += 1

    # build image list
    for i in range(0, s.map_size):
        x = int(i % s.game_col) * s.grid_size + (s.grid_size - s.scale_size[0]) / 2
        y = int(i / s.game_col) * s.grid_size + (s.grid_size - s.scale_size[0]) / 2
        img = './images/img_' + str(maps[i]) + '.png'
        images.append(ImageButton(screen, img, x, y, i, maps[i], s))

    # start playing
    play = True

    while True:
        screen.fill(s.background_color)
        if play:
            # check if all the images are cleared, if so, end the game
            if all_cleared(maps):
                play = False
            # display images
            for i in images:
                i.display()

            pygame.display.update()

        else:
            win = pygame.image.load(s.win)
            screen.blit(win, (
                (s.screen_width - win.get_width()) / 2, (s.screen_height - win.get_height()) / 2))
            pygame.display.update()

        # check click event
        click_event(images, s, maps)

        time.sleep(0.03)


# main method
if __name__ == '__main__':
    main()
