import pygame


# todo handle score
class Scoreboard:
    def __init__(self, screen, y_starship):
        self.screen = screen
        self.y_below_starship = y_starship + 40

        try:
            self.font = pygame.font.Font("FontPressStart2P/PressStart2P.ttf", 36)
            font_x = self.screen.get_width() // 2 + 50
            font_y = self.y_below_starship + 10
        except FileNotFoundError:
            self.font = pygame.font.Font(None, 55)
            font_x = self.screen.get_width() // 2 + 250
            font_y = self.y_below_starship + 10

        self.text_surface = self.font.render("Score: 9876", False, (0, 255, 0))
        self.text_pos = (font_x, font_y)

    def draw(self):
        self.screen.blit(self.text_surface, self.text_pos)
