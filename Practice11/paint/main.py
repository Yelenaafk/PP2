import pygame as py
import sys
import random
import math

py.init()
WIDTH = 800
HEIGHT = 800
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Paint")

#colors
BLUE = (30, 144, 255)
PINK = (255, 105, 180)
YELLOW = (255, 215, 0)
GREEN = (107, 142, 35)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOR = BLACK

clock = py.time.Clock()
screen.fill(WHITE)

LMBp = False
THICKNESS = 5
cX, cY = 0, 0
pX, pY = 0, 0

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
            
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            LMBp = True
            cX, cY = event.pos
            pX, pY = event.pos
            
        if event.type == py.MOUSEMOTION:
            if LMBp:
                cX, cY = event.pos
                
        if event.type == py.MOUSEBUTTONUP and event.button == 1:
            LMBp = False
            
        if event.type == py.KEYDOWN: 
            #thickness and clear
            if event.key == py.K_9: THICKNESS += 1
            if event.key == py.K_0: THICKNESS = max(1, THICKNESS - 1)
            if event.key == py.K_c: screen.fill(WHITE)
            
            #color Selection
            if event.key == py.K_b: COLOR = BLUE
            if event.key == py.K_p: COLOR = PINK
            if event.key == py.K_g: COLOR = GREEN
            if event.key == py.K_y: COLOR = YELLOW

            #random coordinates for shape generation
            x, y = random.randint(100, 600), random.randint(100, 600)
            size = random.randint(50, 150)

            #draw SQUARE (Equal sides)
            if event.key == py.K_s:
                py.draw.rect(screen, COLOR, (x, y, size, size), THICKNESS)

            #draw RIGHT TRIANGLE
            if event.key == py.K_t:
                points = [(x, y), (x, y + size), (x + size, y + size)]
                py.draw.polygon(screen, COLOR, points, THICKNESS)

            #draw EQUILATERAL TRIANGLE (Using height = sqrt(3)/2 * side)
            if event.key == py.K_e:
                height = int((math.sqrt(3) / 2) * size)
                points = [(x, y), (x - size//2, y + height), (x + size//2, y + height)]
                py.draw.polygon(screen, COLOR, points, THICKNESS)

            #draw RHOMBUS (Diamond shape)
            if event.key == py.K_h:
                points = [(x, y), (x + size//2, y + size//2), (x, y + size), (x - size//2, y + size//2)]
                py.draw.polygon(screen, COLOR, points, THICKNESS)

            #original shapes
            if event.key == py.K_r:
                py.draw.rect(screen, COLOR, (x, y, size, random.randint(50, 150)), THICKNESS)
            if event.key == py.K_o:
                py.draw.circle(screen, COLOR, (x, y), size // 2, THICKNESS)

    # freehand drawing logic
    if LMBp:
        py.draw.line(screen, COLOR, (pX, pY), (cX, cY), THICKNESS)
    
    # UI banner
    py.draw.rect(screen, (220, 220, 220), (0, 0, WIDTH, 80))
    small_font = py.font.SysFont("arial", 18)
    
    line1 = "B (blue) | P (pink) | Y (yellow) | G (green) | C (clear)"
    line2 = "S (square) | T (right tri) | E (equilateral) | H (rhombus) | R (rect) | O (circle)"
    line3 = f"9/0 (Thickness: {THICKNESS})"
    
    screen.blit(small_font.render(line1, True, (0, 0, 0)), (10, 5))
    screen.blit(small_font.render(line2, True, (0, 0, 0)), (10, 30))
    screen.blit(small_font.render(line3, True, (0, 0, 0)), (10, 55))

    # update previous mouse position
    pX, pY = cX, cY
    
    py.display.flip()
    clock.tick(60)