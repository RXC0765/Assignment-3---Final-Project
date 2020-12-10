import pygame


class ImageButton:
    __clickable = True
    __checked = False

    def __init__(self, screen, image_path, x, y, num, element, settings):
        self.screen = screen
        self.img = pygame.image.load(image_path)
        self.x = x
        self.y = y
        self.number = num
        self.element = element
        self.settings = settings
        # transform the scale size of original images
        self.img = pygame.transform.scale(self.img, settings.scale_size)

    def __del__(self):
        pass
    
    # display images
    def display(self):
        if self.__checked:
            pygame.draw.rect(self.img, (0, 205, 205, 255),
                             (0, 0, self.img.get_width() - 1, self.img.get_height() - 1), 2)
        else:
            pygame.draw.rect(self.img, (0, 205, 205, 0),
                             (0, 0, self.img.get_width() - 1, self.img.get_height() - 1), 2)
        self.screen.blit(self.img, (self.x, self.y))
    
    # clear the image (fill it with the background color)
    def delete(self):
        self.__checked = False
        self.__clickable = False
        self.img.fill((255, 255, 255))

    # check if one button is clickable
    def is_clickable(self):
        return self.__clickable
    
    # click the button: set it to checked
    def click(self):
        self.__checked = not self.__checked
        return self.__checked
    
    # reset the button to unchecked
    def reset(self):
        self.__checked = False

    # get geometry
    def geometry(self):
        return int(self.x), int(self.y), self.settings.scale_size[0], self.settings.scale_size[1]
