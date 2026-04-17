import pygame as py
from clock import TheClock

py.init()
size = 800
screen = py.display.set_mode((size, size))
clock = py.time.Clock()
clock_face = py.image.load("Practice9\mickeys_clock\images\clockface.jpg")
clock_face = py.transform.scale(clock_face, (size, size))
center = (size // 2, size // 2)
the_clock = TheClock(center, size)

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    screen.fill((255, 255, 255))
    screen.blit(clock_face, (0, 0))
    the_clock.draw(screen)
    py.display.flip()
    clock.tick(15)
py.quit()