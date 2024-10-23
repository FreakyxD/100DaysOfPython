import pygame


class Separator:
    def __init__(self, screen, y_starship):
        self.y_below_starship = y_starship + 40

        self.screen = screen
        self.pos = pygame.Vector2(0, self.y_below_starship)
        self.rect = None

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
        blit_pos = self.shape.get_rect(topleft=(self.pos.x, self.pos.y))
        self.screen.blit(self.shape, blit_pos)

    def update_rect(self):
        self.rect = self.shape.get_rect(topleft=(self.pos.x, self.pos.y))

    def get_y(self):
        return self.y_below_starship
