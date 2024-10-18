import pygame
from typing import Union

from scoreboard import Score, Lives
from separator import Separator
from starship import Starship
from projectile import Projectile

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


player_projectile = None
player_last_shot_time = 0
player_shooting_cooldown = 500  # in milliseconds
while running:
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    score.draw()
    lives.draw()

    separator.draw()

    starship.handle_movement(dt)
    starship.draw()

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

    if player_projectile:
        player_projectile.handle_projectile_movement(dt)
        player_projectile.draw()

        if is_collision_with_screen_top(player_projectile):
            player_projectile = None
            # todo for debugging purposes
            # lives.decrease_life()

    if lives.current_lives < 0:
        running = False

    # flip() the display to put everything on screen
    pygame.display.flip()

pygame.quit()
