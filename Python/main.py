import pygame as pg
from random import randrange
from time import sleep, perf_counter

WINDOW = 700
TILE_SIZE   = int(.05*WINDOW)
RANGE = (int(TILE_SIZE//2), int(WINDOW-TILE_SIZE//2), int(TILE_SIZE))

get_rand_pos = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.rect.Rect([0,0,TILE_SIZE-2,TILE_SIZE-2,])
snake.center = get_rand_pos()
length = 1
snake_dir = (0, 0)
segments = [snake.copy()]
time, time_step = 0, 200
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        # Collect Input
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                snake_dir = (0, -TILE_SIZE)
            elif event.key == pg.K_s:
                snake_dir = (0, TILE_SIZE)
            elif event.key == pg.K_a:
                snake_dir = (-TILE_SIZE, 0)
            elif event.key == pg.K_d:
                snake_dir = (TILE_SIZE, 0)
        screen.fill('black')
        # Draw snake
        [pg.draw.rect(screen, 'green', segment) for segment in segments]
        # Move snake
        currTime = pg.time.get_ticks()
        if currTime - time > time_step:
            time = currTime
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-length:]
        pg.display.flip()
        clock.tick(144)