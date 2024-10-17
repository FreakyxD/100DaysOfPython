import pygame


class Separator:
    def __init__(self, screen, y_starship):
        self.screen = screen
        self.y_below_starship = y_starship + 40

        self.shape = pygame.Surface((self.screen.get_width(), 40), pygame.SRCALPHA)
        pygame.draw.line(
            self.shape,
            (0, 255, 0),
            (0, 0),
            (self.screen.get_width(), 0),
            2
        )

        self.mask = pygame.mask.from_surface(self.shape)

    def draw(self):
        self.screen.blit(self.shape, (0, self.y_below_starship))

    def get_mask(self):
        return self.mask

    def get_y(self):
        return self.y_below_starship