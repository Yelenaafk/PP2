import pygame as py
import sys
from pygame.locals import *
import random, time

#initialize all imported pygame modules
py.init()

#game constants and global variables
WIDTH = 400
HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0
N = 100 #speed increases every 5 coins (adjusted for testing)

#screen setup
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Racer")

#frame rate control
clock = py.time.Clock()

#font settings
font = py.font.SysFont("arial", 60)
small_font = py.font.SysFont("arial", 20)
game_over = font.render("Wasted", True, (0, 0, 0))

#load assets
background = py.image.load("Practice11/racer/road.png")
accident = py.image.load("Practice11/racer/boom.png")
fail_sound = py.mixer.Sound("Practice11/racer/boom.wav")
py.mixer.music.load("Practice11/racer/background.wav")
py.mixer.music.play(-1)

class Enemy(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("Practice11/racer/green-car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(50, WIDTH - 50 ), 0)

class Coin(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #load the base image
        self.base_image = py.image.load("Practice11/racer/thecoin.png")
        self.image = self.base_image
        self.rect = self.image.get_rect()
        self.weight = 1 #default value
        self.spawn()

    def spawn(self):
        #randomly assign a weight (value) between 1 and 3
        self.weight = random.randint(1, 3)
        
        #scale image based on weight (heavier coins are larger)
        size = 20 + (self.weight * 10) 
        self.image = py.transform.scale(self.base_image, (size, size))
        
        #update rect to match the new image size
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, WIDTH - 50), -50)

    def move(self):
        self.rect.move_ip(0, SPEED)
        #if coin goes off screen without being caught
        if self.rect.top > HEIGHT:
            self.spawn()

class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = py.image.load("Practice11/racer/johny.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)

    def move(self):
        keys = py.key.get_pressed()
        if self.rect.left > 50 and keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH - 50 and keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

#initialize sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

#setup groups
enemies = py.sprite.Group()
enemies.add(E1)

coin_group = py.sprite.Group()
coin_group.add(C1)

all_sprites = py.sprite.Group()
all_sprites.add(P1, E1, C1)

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    screen.blit(background, (0, 0))

    #UI rendering
    py.draw.rect(screen, (220, 220, 220), (0, 0, WIDTH, 60))
    scores = small_font.render(f"Score: {SCORE}", True, (0, 0, 0))
    coins_text = small_font.render(f"Coins: {COINS}", True, (0, 0, 0))
    speed_text = small_font.render(f"Speed: {SPEED}", True, (0, 0, 0))
    
    screen.blit(scores, (10, 10))
    screen.blit(coins_text, (10, 30))
    screen.blit(speed_text, (WIDTH - 80, 10))

    # draw and move all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    #check if Player collides with any sprite in coin_group
    collided_coin = py.sprite.spritecollideany(P1, coin_group)
    if collided_coin:
        #increase COINS by the specific weight of the coin collected
        COINS += C1.weight 
        
        #check if we hit the threshold N to increase global SPEED
        #we use // N to check if the "set" of coins has increased
        if COINS // N > (COINS - C1.weight) // N:
            SPEED += 1
            
        C1.spawn() #re-spawn the coin with new weight/position

    if py.sprite.spritecollideany(P1, enemies):
        py.mixer.music.stop()
        fail_sound.play()
        
        #show crash
        accident_rect = accident.get_rect(center=P1.rect.center)
        screen.blit(accident, accident_rect)
        py.display.update()
        time.sleep(1)

        #game over screen
        screen.fill((255, 255, 255))
        screen.blit(game_over, (100, 250))
        py.display.update()
        time.sleep(2)
        py.quit()
        sys.exit()

    py.display.update()
    clock.tick(60)