import pygame

WIDTH = 400
HEIGHT = 600
FPS = 60
background = pygame.image.load("TSIS/TSIS3/assets/road.png")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (205, 92, 92)
GREEN = (50, 205, 50)
BLUE = (70, 130, 180)
YELLOW = (255, 215, 0)

class Button:
    def __init__(self, text, x, y, w, h, color, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.action = action
        self.hover_color = tuple(min(c + 50, 255) for c in color)
        self.current_color = color

    def draw(self, screen, font):
        mouse_pos = pygame.mouse.get_pos()
        self.current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(screen, self.current_color, self.rect)
        pygame.draw.rect(screen, WHITE, self.rect, 1) 
        txt_surf = font.render(self.text, True, WHITE)
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        screen.blit(txt_surf, txt_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def draw_text(screen, text, size, x, y, color=BLACK, center=False):
    font = pygame.font.SysFont("timesnewroman", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)