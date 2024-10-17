import pygame

class Scoreboard:
    def __init__(self, screen, y_starship):
        self.screen = screen
        self.y_below_starship = y_starship + 40

    def draw(self):
        pygame.draw.line(
            self.screen,
            (0, 255, 0),
            (0, self.y_below_starship),
            (self.screen.get_width(), self.y_below_starship),
            2
        )
