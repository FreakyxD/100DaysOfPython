import pygame


class Starship:
    def __init__(self, screen):
        self.screen = screen
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() * 0.9)

        self.body_width = 15
        self.body_height = 30
        self.side_width = 10
        self.side_height = 30

        self.starship_width = self.body_width + 2 * self.side_width

    def draw(self):
        # main central body (slightly larger, centered)
        pygame.draw.rect(
            self.screen, "white",
            pygame.Rect(self.player_pos.x - self.body_width // 2, self.player_pos.y - self.body_height // 2,
                        self.body_width,
                        self.body_height)
        )

        # left side (shifted left and aligned vertically with bottom of main body)
        pygame.draw.rect(
            self.screen, "white",
            pygame.Rect(self.player_pos.x - self.body_width // 2 - self.side_width,
                        self.player_pos.y - self.body_height // 2 + 10,
                        self.side_width, self.side_height)
        )

        # right side (shifted right and aligned vertically with bottom of main body)
        pygame.draw.rect(
            self.screen, "white",
            pygame.Rect(self.player_pos.x + self.body_width // 2, self.player_pos.y - self.body_height // 2 + 10,
                        self.side_width,
                        self.side_height)
        )

    def handle_movement(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and (self.player_pos.x - self.starship_width // 2) > 0:
            self.player_pos.x -= 300 * dt
        if keys[pygame.K_d] and (self.player_pos.x + self.starship_width // 2) < self.screen.get_width():
            self.player_pos.x += 300 * dt
