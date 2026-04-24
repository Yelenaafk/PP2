import pygame as py
import sys
import random

py.init()
WIDTH = 800
HEIGHT = 800
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Paint")
BLUE = (30, 144, 255)
PINK = (255, 105, 180)
YELLOW = (255, 215, 0)
GREEN = (107, 142, 35)
BLACK = (0, 0, 0)
COLOR = BLACK
WHITE = (255, 255, 255)
clock = py.time.Clock()
screen.fill(WHITE)
LMBp = False
THICKNESS = 5
cX = 0
cY = 0
pX = 0
pY = 0

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            LMBp = True
            cX = event.pos[0]
            cY = event.pos[1]
            pX = event.pos[0]
            pY = event.pos[1]
        if event.type == py.MOUSEMOTION:
            if LMBp:
                cX = event.pos[0]
                cY = event.pos[1]
        if event.type == py.MOUSEBUTTONUP and event.button == 1:
            LMBp = False
        if event.type == py.KEYDOWN: 
            if event.key == py.K_9:
                THICKNESS += 1
            if event.key == py.K_0:
                THICKNESS -= 1
            if event.key == py.K_c:
                screen.fill(WHITE)
            if event.key == py.K_b: 
                COLOR = BLUE
            if event.key == py.K_p:
                COLOR = PINK
            if event.key == py.K_g:
                COLOR = GREEN
            if event.key == py.K_y:
                COLOR = YELLOW
            if event.key == py.K_r:
                py.draw.rect(screen, COLOR, (random.randint(5, 600), random.randint(5, 600), random.randint(5, 600), random.randint(5, 600)), THICKNESS)
            if event.key == py.K_o:
                py.draw.circle(screen, COLOR, (random.randint(5, 600), random.randint(5, 600)), random.randint(5, 600), THICKNESS)
    if LMBp:
        py.draw.line(screen, COLOR, (pX, pY), (cX, cY), THICKNESS)
    py.draw.rect(screen, (220, 220, 220), (0, 0, 450, 60))
    small_font = py.font.SysFont("arial", 20)
    text = small_font.render("B (blue) | P (pink) | Y (yellow) | G (green)", True, (0, 0, 0))
    screen.blit(text, (5, 5))
    text1 = small_font.render("C (eraser) | R (rectangle) | O (circle) | 0 (thicker) | 9 (thinner)", True, (0, 0, 0))
    screen.blit(text1, (5, 30))
    pX = cX
    pY = cY
    py.display.flip()
    clock.tick(60)