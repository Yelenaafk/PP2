import pygame
import random
from ui import WIDTH, HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        super().__init__()
        self.image = pygame.image.load("TSIS/TSIS3/assets/johny.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.speed = 5
        self.shielded = False

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 50 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.right < WIDTH - 50 and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        super().__init__()
        self.image = pygame.image.load("TSIS/TSIS3/assets/diego.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), -50)
        self.speed = speed + random.uniform(-1, 1)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("TSIS/TSIS3/assets/thecoin.png")
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), -50)

    def update(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > HEIGHT:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type 
        self.image = pygame.Surface((30, 30))
        colors = {'Nitro': (0, 0, 255), 'Shield': (0, 255, 255)}
        self.image.fill(colors.get(type, (255, 255, 255)))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), -50)

    def update(self):
        self.rect.move_ip(0, 4)
        if self.rect.top > HEIGHT:
            self.kill()

class Hazard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 20), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, (139, 69, 19), (0, 0, 50, 20))
        pygame.draw.ellipse(self.image, (100, 50, 15), (5, 5, 40, 10))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), -100)

    def update(self):
        self.rect.move_ip(0, 4)
        if self.rect.top > HEIGHT:
            self.kill()