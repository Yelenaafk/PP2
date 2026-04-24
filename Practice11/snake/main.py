import pygame as py
import sys
import random

py.init()

#constants
SIZE = 800
CELL = 40
SCORE = 0
LEVEL = 1
screen = py.display.set_mode((SIZE, SIZE))
py.display.set_caption("Snake - Food Weight & Timer") 
clock = py.time.Clock()

#positioning helper
RANGE = (CELL // 2, SIZE - CELL // 2, CELL)
get_random_pos = lambda: [random.randrange(*RANGE), random.randrange(*RANGE)]

#snake setup
snake = py.rect.Rect([0, 0, CELL - 2, CELL - 2])
snake.center = get_random_pos()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)

#movement timing
time_prev, time_step = 0, 250

food = snake.copy()
food.center = get_random_pos()
food_weight = 1       #how many points/length units the food gives
food_timer = 5000     #food disappears after 5 seconds (5000 ms)
food_spawn_time = py.time.get_ticks() #timestamp of when food appeared

def spawn_food():
    """Generates new food with a random weight and resets the timer."""
    global food_weight, food_spawn_time
    food.center = get_random_pos()
    food_spawn_time = py.time.get_ticks()
    #randomly assign weight: 1 (common), 2 (rare), or 3 (epic)
    food_weight = random.choices([1, 2, 3], weights=[70, 20, 10])[0]

#initial spawn
spawn_food()

font = py.font.SysFont("arial", 20)

while True:
    current_time = py.time.get_ticks()

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

    #check if food has been sitting too long
    if current_time - food_spawn_time > food_timer:
        spawn_food()

    #collision with self or walls
    eating_itself = py.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > SIZE or snake.top < 0 or snake.bottom > SIZE or eating_itself:
        snake.center = get_random_pos()
        spawn_food()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]
        SCORE = 0
        LEVEL = 1
        FPS = 3 #reset speed

    #collision with food
    if snake.center == food.center:
        SCORE += food_weight
        length += food_weight #snake grows based on food weight
        if SCORE // 4 >= LEVEL: #level up every 4 points
            LEVEL += 1
        spawn_food()

    #draw background UI
    py.draw.rect(screen, (255, 255, 255), (0, 0, 120, 75))
    score_txt = font.render(f"Score: {SCORE}", True, (0, 0, 0))
    level_txt = font.render(f"Level: {LEVEL}", True, (0, 0, 0))
    #visual indicator of food timer
    timer_ratio = 1 - ((current_time - food_spawn_time) / food_timer)
    py.draw.rect(screen, (255, 0, 0), (5, 55, 100 * timer_ratio, 10))
    
    screen.blit(score_txt, (5, 5))
    screen.blit(level_txt, (5, 30))

    #draw food (Color changes based on weight)
    colors = {1: (255, 99, 71), 2: (0, 191, 255), 3: (255, 215, 0)}
    py.draw.rect(screen, colors.get(food_weight, (255, 255, 255)), food)

    #draw snake
    for segment in segments:
        py.draw.rect(screen, (127, 255, 0), segment)

    #movement logic
    if current_time - time_prev > time_step:
        time_prev = current_time
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

    py.display.flip()
    clock.tick(60) #keep a smooth 60 for the UI, movement is controlled by time_step