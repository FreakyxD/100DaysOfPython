import pygame


class Starship:
    def __init__(self, screen, y_starship):
        self.screen = screen
        self.pos = pygame.Vector2(self.screen.get_width() // 2, y_starship)

        self.body_width = 15
        self.body_height = 30
        self.side_width = 10
        self.side_height = 30

        self.starship_width = self.body_width + 2 * self.side_width
        self.starship_height = self.body_height + 10

        self.shape = pygame.Surface((self.starship_width, self.starship_height), pygame.SRCALPHA)

        # main body position
        main_body_x = self.side_width
        main_body_y = 0

        # left side position
        left_side_x = 0
        left_side_y = 10

        # right side position
        right_side_x = self.side_width + self.body_width
        right_side_y = left_side_y

        # draw main central body
        pygame.draw.rect(
            self.shape, (0, 255, 0),
            pygame.Rect(main_body_x, main_body_y, self.body_width, self.body_height)
        )

        # draw left side
        pygame.draw.rect(
            self.shape, (0, 255, 0),
            pygame.Rect(left_side_x, left_side_y, self.side_width, self.side_height)
        )

        # draw right side
        pygame.draw.rect(
            self.shape, (0, 255, 0),
            pygame.Rect(right_side_x, right_side_y, self.side_width, self.side_height)
        )

        self.mask = pygame.mask.from_surface(self.shape)

    def draw(self):
        blit_pos = self.shape.get_rect(center=(self.pos.x, self.pos.y))
        self.screen.blit(self.shape, blit_pos)

    def get_mask(self):
        return self.mask

    def handle_movement(self, dt):
        keys = pygame.key.get_pressed()
        move_distance = int(300 * dt)
        edge_offset = 4
        if keys[pygame.K_a] and (self.pos.x - self.starship_width // 2) > 0 + edge_offset:
            self.pos.x -= move_distance
        if keys[pygame.K_d] and (self.pos.x + self.starship_width // 2) < self.screen.get_width() - edge_offset:
            self.pos.x += move_distance

    def get_coords(self):
        return self.pos.x, self.pos.y

    def get_top_center(self):
        center_x = self.pos.x
        top_y = self.pos.y - (self.starship_height // 2)
        return center_x, top_y
