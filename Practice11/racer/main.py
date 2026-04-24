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
N = 100 #threshold for increasing speed

#screen Setup
screen = py.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
py.display.set_caption("Racer")

#frame rate control
clock = py.time.Clock()

#font settings for UI and Game Over screen
font = py.font.SysFont("arial", 60)
small_font = py.font.SysFont("arial", 20)
game_over = font.render("Game Over", True, (0, 0, 0))

#load images and sound assets
background = py.image.load("Practice11/racer/road.png")
accident = py.image.load("Practice11/racer/boom.png")
fail_sound = py.mixer.Sound("Practice11/racer/spongebob-fail.wav")
main_titles = py.mixer.music.load("Practice11/racer/background.wav")

#start background music looping indefinitely
py.mixer.music.play(-1)

class Enemy(py.sprite.Sprite):
    """Class to represent the enemy car."""
    def __init__(self):
        super().__init__()
        self.image = py.image.load("Practice11/racer/green-car.png")
        self.rect = self.image.get_rect()
        #initial spawn at a random X position at the top of the screen
        self.rect.center = (random.randint(50, WIDTH - 50), 0)

    def move(self):
        global SCORE
        #move vertically by current global speed
        self.rect.move_ip(0, SPEED)
        #if the enemy passes the bottom, reset position and increase score
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(50, WIDTH - 50 ), 0)

class Player(py.sprite.Sprite):
    """Class to represent the player's car."""
    def __init__(self):
        super().__init__()
        self.image = py.image.load("Practice11/racer/pink-car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)

    def move(self):
        keys = py.key.get_pressed()
        #movement with boundary checks to keep car on screen
        if self.rect.left > 0:
            if keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:
            if keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def get_coordinates(self):
        return self.rect.top, self.rect.left
    
#initialize sprites and groups
player = Player()
enemy = Enemy()

enemies = py.sprite.Group()
enemies.add(enemy)

all_sprites = py.sprite.Group()
all_sprites.add(player, enemy)

#coin setup (handled outside a class in this version)
coin = py.image.load("Practice11/racer/thecoin.png")
COINX, COINY = random.randint(50, WIDTH - 50), 0

while True:
    #event handling
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    #draw background
    screen.blit(background, (0, 0))

    #draw UI header (Score and Coin counter)
    py.draw.rect(screen, (220, 220, 220), (0, 0, 450, 60))
    scores = small_font.render(f"Score: {str(SCORE)}", True, (0, 0, 0))
    screen.blit(scores, (10, 10))
    coins_text = small_font.render(f"Coins: {str(COINS)}", True, (0, 0, 0))
    screen.blit(coins_text, (10, 30))

    #coin logic: Drawing and Movement
    screen.blit(coin, (COINX, COINY))
    COINY += SPEED

    #respawn coin if it goes off screen
    if COINY > HEIGHT:
        COINX, COINY = random.randint(40, WIDTH - 40), 0

    #check for Player collecting the coin
    if player.rect.collidepoint(COINX, COINY):
        COINS += random.choice([1, 5, 10]) #random weight/value
        COINX, COINY = random.randint(50, WIDTH - 50), 0
        #speed up the game every N coins
        if COINS % N == 0 and COINS != 0:
            SPEED += 1

    #update and draw all car sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    #collision Logic: Player hitting an Enemy
    if py.sprite.spritecollideany(player, enemies):
        py.mixer.music.stop()
        fail_sound.play()
        
        #display accident image at the collision point
        screen.blit(background, (0, 0))
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
        accident_rect = accident.get_rect(center = player.rect.center)
        screen.blit(accident, accident_rect)
        py.display.update()
        time.sleep(1)

        #transition to Game Over screen
        screen.fill((255, 255, 255))
        screen.blit(game_over, (100, 200))
        py.display.update()
        time.sleep(2)
        py.quit()
        sys.exit()

    #refresh screen
    py.display.flip()
    #limit frame rate to 60 FPS
    clock.tick(60)