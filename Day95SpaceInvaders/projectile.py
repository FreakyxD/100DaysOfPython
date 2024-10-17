import pygame
from enum import Enum, auto


class ProjectileState(Enum):
    READY = auto()
    FLYING = auto()
    DESTROYED = auto()


class Projectile:
    def __init__(self, screen, starship_x, y_starship, projectile_state=ProjectileState.READY):
        self.screen = screen

        self.pos = pygame.Vector2(starship_x + 1, y_starship - 10)
        self.projectile_state = projectile_state

        self.shape = pygame.Surface((4, 10), pygame.SRCALPHA)
        pygame.draw.rect(
            self.shape, "white",
            pygame.Rect(0, 0, 4, 10)
        )

        self.mask = pygame.mask.from_surface(self.shape)

    def draw(self):
        blit_pos = self.shape.get_rect(center=(self.pos.x, self.pos.y))
        self.screen.blit(self.shape, blit_pos)

    def get_mask(self):
        return self.mask

    def handle_projectile_movement(self, dt):
        # reach top of screen in ~1 second from the initial position
        self.pos.y -= self.screen.get_height() * dt
