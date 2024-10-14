import pygame
from enum import Enum, auto


class ProjectileState(Enum):
    READY = auto()
    FLYING = auto()
    DESTROYED = auto()


class Projectile:
    def __init__(self, screen, projectile_state=ProjectileState.READY):
        self.screen = screen
        self.pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() * 0.9 - 15)
        self.projectile_state = projectile_state

        self.shape = pygame.Surface((4, 10), pygame.SRCALPHA)
        pygame.draw.rect(
            self.shape, "white",
            pygame.Rect(0, 0, 4, 10)
        )

    def draw(self):
        blit_pos = self.shape.get_rect(center=(self.pos.x, self.pos.y))
        self.screen.blit(self.shape, blit_pos)

    def handle_projectile_movement(self, dt):
        # reach top of screen in ~1 second from the initial position
        self.pos.y -= self.screen.get_height() * dt
