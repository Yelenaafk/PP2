import pygame as py
import sys
from pygame.locals import *  
import random, time

py.init()
WIDTH = 400
HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

screen = py.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
py.display.set_caption("Racer")
clock = py.time.Clock()
clock.tick(60)
font = py.font.SysFont("arial", 60)
small_font = py.font.SysFont("arial", 20)
game_over = font.render("Game Over", True, (0, 0, 0))
background = py.image.load("Practice10/racer/road.png")
accident = py.image.load("Practice10/racer/boom.png")
fail_sound = py.mixer.Sound("Practice10/racer/spongebob-fail.wav")
main_titles = py.mixer.music.load("Practice10/racer/background.wav")
py.mixer.music.play(-1)

class Enemy(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("Practice10/racer/green-car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), 0)
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(50, WIDTH - 50 ), 0)

class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("Practice10/racer/pink-car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)
    def move(self):
        keys = py.key.get_pressed()
        if self.rect.left > 0:
            if keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:
            if keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    def get_coordinates(self):
        return self.rect.top, self.rect.left
    
player = Player()
enemy = Enemy()
enemies = py.sprite.Group()
enemies.add(enemy)
all_sprites = py.sprite.Group()
all_sprites.add(player, enemy)
INC_SPEED = py.USEREVENT + 1 
py.time.set_timer(INC_SPEED, 1000)
coin = py.image.load("Practice10/racer/thecoin.png")
COINX, COINY = random.randint(50, WIDTH - 50), 0

while True:
    for event in py.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    screen.blit(background, (0, 0))
    py.draw.rect(screen, (220, 220, 220), (0, 0, 450, 60))
    scores = small_font.render(f"Score: {str(SCORE)}", True, (0, 0, 0))
    screen.blit(scores, (10, 10))
    coins = small_font.render(f"Coins: {str(COINS)}", True, (0, 0, 0))
    screen.blit(coins, (10, 30))
    screen.blit(coin, (COINX, COINY))
    COINY += SPEED
    if COINY > HEIGHT:
        COINX, COINY = random.randint(40, WIDTH - 40), 0
    if player.rect.collidepoint(COINX, COINY):
        COINS += 1
        COINX, COINY = random.randint(50, WIDTH - 50), 0
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    if py.sprite.spritecollideany(player, enemies):
        py.mixer.music.stop()
        fail_sound.play()
        screen.blit(background, (0, 0))
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
        accident_rect = accident.get_rect(center = player.rect.center)
        screen.blit(accident, accident_rect)
        py.display.update()
        time.sleep(1)
        screen.fill((255, 255, 255))
        screen.blit(game_over, (100, 200))
        py.display.update()
        time.sleep(2)
        py.quit()
        sys.exit()
    py.display.flip()
    clock.tick(60)