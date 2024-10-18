import pygame

ALIEN_WIDTH = 40
ALIEN_HEIGHT = 40

global alien_direction
alien_direction = 1  # 1 for moving right, -1 for moving left


def create_alien_type1():
    # create Alien Type 1: body and eyes
    surface = pygame.Surface((ALIEN_WIDTH, ALIEN_HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(0, 10, ALIEN_WIDTH, 20))  # body
    pygame.draw.circle(surface, (255, 0, 0), (10, 17), 5)  # left eye
    pygame.draw.circle(surface, (255, 0, 0), (30, 17), 5)  # right eye
    return surface


def create_alien_type2():
    # create Alien Type 2: body and antennae
    surface = pygame.Surface((ALIEN_WIDTH, ALIEN_HEIGHT), pygame.SRCALPHA)
    pygame.draw.circle(surface, (255, 255, 255), (ALIEN_WIDTH // 2, ALIEN_HEIGHT // 2 + 5), 15)  # body
    pygame.draw.line(surface, (255, 255, 255), (15, 15), (10, 5), 2)  # left antenna
    pygame.draw.line(surface, (255, 255, 255), (25, 15), (30, 5), 2)  # right antenna
    return surface


def create_alien_type3():
    # create Alien Type 3: trapezoid body and pincers
    surface = pygame.Surface((ALIEN_WIDTH, ALIEN_HEIGHT), pygame.SRCALPHA)

    center_x, y_top, y_bottom = ALIEN_WIDTH / 2, 5, 20
    trapezoid = [
        (center_x - 10, y_top), (center_x + 10, y_top),
        (center_x + 15, y_bottom), (center_x - 15, y_bottom)
    ]
    pygame.draw.polygon(surface, (255, 255, 255), [(int(x), int(y)) for x, y in trapezoid])

    # define and draw pincers
    def draw_pincer(start, direction):
        mid = (start[0] + direction * 5, start[1] + 5)
        pygame.draw.line(surface, (255, 255, 255), start, mid, 2)
        pygame.draw.line(surface, (255, 255, 255), mid, (start[0], start[1] + 10), 2)

    draw_pincer((int(trapezoid[3][0] + 6), int(trapezoid[3][1])), -1)  # left pincer
    draw_pincer((int(trapezoid[2][0] - 6), int(trapezoid[2][1])), 1)  # right pincer

    return surface


class Alien:
    def __init__(self, screen, pos, alien_type):
        self.screen = screen
        self.pos = pygame.Vector2(pos)

        # assign alien shape based on type
        if alien_type == 1:
            self.shape = create_alien_type1()
        elif alien_type == 2:
            self.shape = create_alien_type2()
        elif alien_type == 3:
            self.shape = create_alien_type3()
        else:
            raise ValueError("Invalid alien type. Choose 1, 2, or 3.")

        self.mask = pygame.mask.from_surface(self.shape)  # mask for collisions
        self.speed = 100  # horizontal speed

    def draw(self):
        blit_pos = self.shape.get_rect(center=self.pos)
        self.screen.blit(self.shape, blit_pos)

    def handle_movement(self, dt):
        # todo fix movement
        global alien_direction
        if self.pos.x - ALIEN_WIDTH // 2 <= 0 or self.pos.x + ALIEN_WIDTH // 2 >= self.screen.get_width():
            # hit the wall
            alien_direction *= -1

        self.pos.x += alien_direction * int(self.speed * dt)

    def get_mask(self):
        return self.mask

    def get_surface(self):
        return self.shape

    def get_coords(self):
        return self.pos.x, self.pos.y
