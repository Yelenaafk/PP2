import pygame as py
import sys
import random

py.init()
SIZE = 800
CELL = 40
SCORE = 0
LEVEL = 1
screen = py.display.set_mode((SIZE, SIZE))
screen.fill((0, 0, 0))
py.display.set_caption("Snake") 
clock = py.time.Clock()
FPS = 3
RANGE = (CELL // 2, SIZE - CELL // 2, CELL)
get_random_pos = lambda: [random.randrange(*RANGE), random.randrange(*RANGE)]

snake = py.rect.Rect([0, 0, CELL - 2, CELL - 2])
snake.center = get_random_pos()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 110
food = snake.copy()
food.center = get_random_pos()
font = py.font.SysFont("arial", 20)

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_UP and snake_dir != (0, CELL):
                snake_dir = (0, - CELL)
            if event.key == py.K_DOWN and snake_dir != (0, -CELL):
                snake_dir = (0, CELL)
            if event.key == py.K_LEFT and snake_dir != (CELL, 0):
                snake_dir = (- CELL, 0)
            if event.key == py.K_RIGHT and snake_dir != (-CELL, 0):
                snake_dir = (CELL, 0)
    screen.fill((0, 0, 0))
    eating_itself = py.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > SIZE or snake.top < 0 or snake.bottom > SIZE or eating_itself:
        snake.center, food.center = get_random_pos(), get_random_pos()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]
        SCORE = 0
        LEVEL = 1
    if snake.center == food.center:
        food.center = get_random_pos()
        length += 1
        SCORE += 1
        if SCORE % 4 == 0:
            LEVEL += 1
            FPS += 1
    py.draw.rect(screen, (255, 255, 255), (0, 0, 100, 55))
    score = font.render(f"Score: {str(SCORE)}", True, (107, 255, 0))
    screen.blit(score, (5, 5))
    level = font.render(f"Level: {str(LEVEL)}", True, (255, 215, 0))
    screen.blit(level, (5, 25))
    py.draw.rect(screen, (255, 99, 71), food)
    for segment in segments:
        py.draw.rect(screen, (127, 255, 0), segment)
    time_now = py.time.get_ticks() 
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    py.display.flip()
    clock.tick(FPS)