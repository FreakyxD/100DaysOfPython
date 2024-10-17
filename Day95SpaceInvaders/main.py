import pygame

from scoreboard import Scoreboard
from starship import Starship
from projectile import Projectile

# pygame setup
pygame.init()
screen = pygame.display.set_mode((960, 720))
Y_STARSHIP = screen.get_height() * 0.87
clock = pygame.time.Clock()
running = True

scoreboard = Scoreboard(screen, Y_STARSHIP)
starship = Starship(screen, Y_STARSHIP)

projectiles = []

while running:
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    scoreboard.draw()

    starship.handle_movement(dt)
    starship.draw()

    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                starship_x, _ = starship.get_coords()
                projectiles.append(Projectile(screen, starship_x, Y_STARSHIP))  # handle shooting
        elif event.type == pygame.QUIT:
            running = False  # user clicked X to close the window

    for projectile in projectiles:
        projectile.handle_projectile_movement(dt)
        projectile.draw()

    # todo destroy projectiles

    # flip() the display to put everything on screen
    pygame.display.flip()

pygame.quit()
