import pygame


class Score:
    def __init__(self, screen, y_starship):
        self.screen = screen
        self.y_below_starship = y_starship + 40
        self.current_score = 0

        try:
            self.font = pygame.font.Font("FontPressStart2P/PressStart2P.ttf", 36)
            font_x = self.screen.get_width() // 2 + 50
            font_y = self.y_below_starship + 10
        except FileNotFoundError:
            self.font = pygame.font.Font(None, 55)
            font_x = self.screen.get_width() // 2 + 250
            font_y = self.y_below_starship + 10

        self.text_pos = (font_x, font_y)

    def draw(self):
        text_surface = self.font.render(f"Score: {self.current_score}", False, (0, 255, 0))
        self.screen.blit(text_surface, self.text_pos)

    def increase_score(self, to_add):
        self.current_score += to_add


class Lives:
    def __init__(self, screen, y_starship, starship_surface):
        self.screen = screen
        self.y_below_starship = y_starship + 37
        self.starship_surface = starship_surface

        self.current_lives = 2

    def draw(self):
        for i in range(self.current_lives):
            x_pos = 10 + i * 50
            y_pos = self.y_below_starship + 10
            self.screen.blit(self.starship_surface, (x_pos, y_pos))

    def decrease_life(self):
        self.current_lives -= 1


class EndGameMessage:
    def __init__(self, screen, message, color):
        self.screen = screen
        self.message = message
        self.color = color

        try:
            self.font = pygame.font.Font("FontPressStart2P/PressStart2P.ttf", 70)
        except FileNotFoundError:
            self.font = pygame.font.Font(None, 120)

        self.text_pos = (self.screen.get_width() // 2 - self.font.size(self.message)[0] // 2,
                         self.screen.get_height() // 2 - self.font.size(self.message)[1] // 2)

    def draw(self):
        text_surface = self.font.render(self.message, False, self.color)
        self.screen.blit(text_surface, self.text_pos)
