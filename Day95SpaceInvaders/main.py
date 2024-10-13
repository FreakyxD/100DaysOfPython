import pygame
from starship import Starship

# pygame setup
pygame.init()
screen = pygame.display.set_mode((960, 720))
clock = pygame.time.Clock()
running = True

player = Starship(screen)

while running:
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    # poll for events
    # pygame.QUIT event means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    player.handle_movement(dt)
    player.draw()

    # flip() the display to put everything on screen
    pygame.display.flip()

pygame.quit()
