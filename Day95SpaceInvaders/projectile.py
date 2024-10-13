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

    def draw(self):
        pygame.draw.rect(
            self.screen, "white",
            pygame.Rect(self.pos.x, self.pos.y, 4, 10)
        )

    def handle_projectile_movement(self, dt):
        # reach top of screen in ~1 second from the initial position
        self.pos.y -= self.screen.get_height() * dt
