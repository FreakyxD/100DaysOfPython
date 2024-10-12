import pygame

class Player:
    def __init__(self, screen, dt, player_pos):
        self.dt = dt
        self.player_pos = player_pos
        pygame.draw.circle(screen, "red", self.player_pos, 40)


    def handle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player_pos.y -= 300 * self.dt
        if keys[pygame.K_s]:
            self.player_pos.y += 300 * self.dt
        if keys[pygame.K_a]:
            self.player_pos.x -= 300 * self.dt
        if keys[pygame.K_d]:
            self.player_pos.x += 300 * self.dt
