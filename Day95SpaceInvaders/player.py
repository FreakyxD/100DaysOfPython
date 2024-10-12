import pygame

class Player:
    def __init__(self, screen, dt, player_pos):
        self.dt = dt
        self.player_pos = player_pos
        self.screen = screen
        self.draw()

    def draw(self):
        body_width = 15
        body_height = 30
        side_width = 10
        side_height = 30

        # main central body (slightly larger, centered)
        pygame.draw.rect(
            self.screen, "white",
            pygame.Rect(self.player_pos.x - body_width // 2, self.player_pos.y - body_height // 2, body_width,
                        body_height)
        )

        # left side (shifted left and aligned vertically with bottom of main body)
        pygame.draw.rect(
            self.screen, "white",
            pygame.Rect(self.player_pos.x - body_width // 2 - side_width, self.player_pos.y - body_height // 2 + 10,
                        side_width, side_height)
        )

        # right side (shifted right and aligned vertically with bottom of main body)
        pygame.draw.rect(
            self.screen, "white",
            pygame.Rect(self.player_pos.x + body_width // 2, self.player_pos.y - body_height // 2 + 10, side_width,
                        side_height)
        )

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
