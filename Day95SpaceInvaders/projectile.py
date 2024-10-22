import pygame
from enum import Enum, auto


class ProjectileState(Enum):
    READY = auto()
    FLYING = auto()
    DESTROYED = auto()


class Projectile:
    def __init__(self, screen, shooter_x, shooter_y, is_half_speed=False, wide_shots=False,
                 projectile_state=ProjectileState.READY):
        self.screen = screen
        self.pos = pygame.Vector2(shooter_x + 1, shooter_y)
        self.rect = None

        self.is_half_speed = is_half_speed
        if wide_shots:
            width = 7
        else:
            width = 4

        self.projectile_state = projectile_state

        self.shape = pygame.Surface((width, 10), pygame.SRCALPHA)
        pygame.draw.rect(
            self.shape, "white",
            pygame.Rect(0, 0, width, 10)
        )

        self.mask = pygame.mask.from_surface(self.shape)

    def draw(self):
        blit_pos = self.shape.get_rect(midtop=(self.pos.x, self.pos.y))
        self.screen.blit(self.shape, blit_pos)

    def update_rect(self):
        self.rect = self.shape.get_rect(midtop=(self.pos.x, self.pos.y))

    def handle_projectile_movement(self, dt, direction='up'):
        if self.is_half_speed:
            # reach top or bottom of screen in ~2 seconds from the initial position
            if direction == 'up':
                self.pos.y -= self.screen.get_height() * dt / 2
            elif direction == 'down':
                self.pos.y += self.screen.get_height() * dt / 2
        else:
            # reach top or bottom of screen in ~1 second from the initial position
            if direction == 'up':
                self.pos.y -= self.screen.get_height() * dt
            elif direction == 'down':
                self.pos.y += self.screen.get_height() * dt
