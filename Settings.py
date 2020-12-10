class Settings:

    def __init__(self):
        # game title
        self.caption = 'PokemonLink'
        # how many kinds of images we are using
        self.img_num = 10
        # background color
        self.background_color = (255, 255, 255)
        # screen size
        self.screen_size = (self.screen_width, self.screen_height) = (640, 480)
        # game size, the player will clear 6*8 = 48 images
        self.game_size = (self.game_row, self.game_col) = (6, 8)
        # map size
        self.map_size = self.game_row * self.game_col
        # show this image when the player win
        self.win = './images/win.png'
        # grid size
        self.grid_size = 80
        # scale size
        self.scale_size = (76, 76)
        # store temporary button
        self.temp_list = []
