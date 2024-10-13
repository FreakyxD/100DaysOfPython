import pygame


class Starship:
    def __init__(self, screen):
        self.screen = screen
        self.pos = pygame.Vector2(self.screen.get_width() // 2, int(self.screen.get_height() * 0.9))

        self.body_width = 15
        self.body_height = 30
        self.side_width = 10
        self.side_height = 30

        self.starship_width = self.body_width + 2 * self.side_width

    def draw(self):
        # calculate half dimensions using integer division
        body_half_width = self.body_width // 2
        body_half_height = self.body_height // 2

        # main body position (centered)
        main_body_x = self.pos.x - body_half_width
        main_body_y = self.pos.y - body_half_height

        # left side position (to the left of main body)
        left_side_x = main_body_x - self.side_width
        left_side_y = main_body_y + 10

        # right side position (to the right of main body)
        right_side_x = main_body_x + self.body_width
        right_side_y = left_side_y

        # draw main central body
        pygame.draw.rect(
            self.screen, "white",
            pygame.Rect(main_body_x, main_body_y, self.body_width, self.body_height)
        )

        # draw left side
        pygame.draw.rect(
            self.screen, "white",
            pygame.Rect(left_side_x, left_side_y, self.side_width, self.side_height)
        )

        # draw right side
        pygame.draw.rect(
            self.screen, "white",
            pygame.Rect(right_side_x, right_side_y, self.side_width, self.side_height)
        )

    def handle_movement(self, dt):
        keys = pygame.key.get_pressed()
        move_distance = int(300 * dt)
        edge_offset = 4
        if keys[pygame.K_a] and (self.pos.x - self.starship_width // 2) > 0 + edge_offset:
            self.pos.x -= move_distance
        if keys[pygame.K_d] and (self.pos.x + self.starship_width // 2) < self.screen.get_width() - edge_offset:
            self.pos.x += move_distance