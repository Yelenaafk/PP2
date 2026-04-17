import pygame as py
from ball import Ball

py.init()
w = 800
h = 600
screen = py.display.set_mode((w, h))
clock = py.time.Clock()
ball = Ball(x = w // 2, y = h // 2, radius = 25, step = 20, width = w, height = h)

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_UP:
                ball.move_up()
            elif event.key == py.K_DOWN:
                ball.move_down()
            elif event.key == py.K_LEFT:
                ball.move_left()
            elif event.key == py.K_RIGHT:
                ball.move_right()
    screen.fill((255, 255, 255))
    ball.draw(screen)
    py.display.flip()
    clock.tick(60)

py.quit()