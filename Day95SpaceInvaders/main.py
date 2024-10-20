import pygame
from typing import Union

from scoreboard import Score, Lives
from separator import Separator
from starship import Starship
from projectile import Projectile
from alien import Alien, ALIEN_WIDTH, handle_alien_movement

# pygame setup
pygame.init()
screen = pygame.display.set_mode((960, 720))
STARSHIP_SPAWN_Y = screen.get_height() * 0.87
pygame.display.set_caption("Space Invaders")
clock = pygame.time.Clock()
running = True

score = Score(screen, STARSHIP_SPAWN_Y)
separator = Separator(screen, STARSHIP_SPAWN_Y)
starship = Starship(screen, STARSHIP_SPAWN_Y)
lives = Lives(screen, STARSHIP_SPAWN_Y, starship.get_surface())


def spawn_aliens(alien_list):
    number_of_columns = 11
    number_of_rows = 5
    row_alien_types = [1, 2, 2, 3, 3]

    x_spacing = 20  # column spacing
    y_spacing = 60  # row spacing

    total_row_width = number_of_columns * ALIEN_WIDTH + (number_of_columns - 1) * x_spacing
    start_x = (screen.get_width() - total_row_width) / 2
    start_y = int(screen.get_height() * 0.15)

    for row in range(number_of_rows):
        alien_type = row_alien_types[row]
        alien_y = start_y + row * y_spacing

        for column in range(number_of_columns):
            alien_x = start_x + column * (ALIEN_WIDTH + x_spacing) + ALIEN_WIDTH / 2

            # create and add the alien to the list
            new_alien = Alien(screen, (alien_x, alien_y), alien_type)
            alien_list.append(new_alien)


def is_collision_detected(object_1: Union[Starship, Projectile],
                          object_2: Union[Starship, Projectile, Separator]):
    if isinstance(object_2, Separator):
        # separator is horizontal line, no need for offset_x
        offset_x = 0
        offset_y = int(object_2.get_y() - object_1.pos.y)
    else:
        # offset between the objects
        offset_x = int(object_2.pos.x - object_1.pos.x)
        offset_y = int(object_2.pos.y - object_1.pos.y)

    # check if the masks overlap
    collision_point = object_2.mask.overlap(object_1.mask, (offset_x, offset_y))

    return collision_point is not None


def is_collision_with_screen_top(p_projectile: Projectile):
    return p_projectile.pos.y < 0


aliens = []
spawn_aliens(aliens)

player_projectile = None
player_last_shot_time = 0
player_shooting_cooldown = 500  # in milliseconds
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                center_x, top_y = starship.get_top_center()

                current_time = pygame.time.get_ticks()
                # allow only one projectile at a time and check if cooldown is over
                if not player_projectile and (current_time - player_last_shot_time) >= player_shooting_cooldown:
                    player_projectile = Projectile(screen, center_x, top_y)  # handle shooting
                    player_last_shot_time = current_time
        elif event.type == pygame.QUIT:
            running = False  # user clicked X to close the window

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # draw static elements
    score.draw()
    lives.draw()
    separator.draw()

    # move everything
    starship.handle_movement(dt)
    handle_alien_movement(aliens, dt, screen.get_width())
    if player_projectile:
        player_projectile.handle_projectile_movement(dt)

    # collision checks
    if player_projectile:
        if is_collision_with_screen_top(player_projectile):
            player_projectile = None

    for alien in aliens:
        if is_collision_detected(starship, alien):
            lives.decrease_life()
            aliens.remove(alien)
        if player_projectile:
            if is_collision_detected(player_projectile, alien):
                aliens.remove(alien)
                player_projectile = None

    # draw dynamic elements
    starship.draw()
    if player_projectile:
        player_projectile.draw()

    # check lives
    if lives.current_lives < 0:
        running = False

    # flip() the display to put everything on screen
    pygame.display.flip()

pygame.quit()
