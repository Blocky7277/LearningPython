import pygame as pygame
from pygame.math import Vector2
from random import randrange
from sys import exit

offset = 6

class FRUIT:
    def __init__(self):
        self.x = randrange(0, 20)
        self.y = randrange(0, 20)
        self.colors = ["blue", "purple", "red", "orange", "yellow", "green"]
        self.eaten = 0;
        self.pos = Vector2(self.x, self.y)

    def draw(self):
        fruit_rect = pygame.Rect(self.pos.x*TILE_SIZE+offset/2, self.pos.y*TILE_SIZE+offset/2, TILE_SIZE-offset, TILE_SIZE-offset)
        color_index = self.eaten
        while color_index > len(self.colors)-1:
            color_index = color_index - len(self.colors)
        pygame.draw.rect(screen, self.colors[color_index], fruit_rect,)

    def randomize(self, snek):
        self.x = randrange(0, 20)
        self.y = randrange(0, 20)
        self.pos = Vector2(self.x, self.y)
        for segment in snek:
            if(self.pos == segment):
                self.randomize(snek)

class SNAKE:
    def __init__(self):
        # List of body segments as vectors
        x = randrange(2, 18)
        y = randrange(2, 18)
        self.body = [Vector2(x, y)]
        self.body_colors = ["green", "blue", "purple", "red", "orange", "yellow"]
        self.direction = Vector2(0, 0)
        self.old_dir = Vector2(0, 0)
        self.new_segment = False

    def draw(self):
        for i in range(len(self.body)):
            segment_rect = pygame.Rect(self.body[i].x*TILE_SIZE+offset/2, self.body[i].y*TILE_SIZE+offset/2 ,TILE_SIZE-offset,TILE_SIZE-offset)
            segment_color = i
            while segment_color > len(self.body_colors)-1:
                segment_color = segment_color - len(self.body_colors)
            pygame.draw.rect(screen, self.body_colors[segment_color], segment_rect)
    
    def move_snake(self):
        if self.old_dir + self.direction == Vector2(0,0):
            self.direction = self.old_dir

        if self.new_segment == True:
            self.new_segment = False
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
        elif(len(self.body) == 1):
            body_copy = self.body
            body_copy[0] = body_copy[0] + self.direction
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]
        self.old_dir = self.direction

    def add_segment(self):
        self.new_segment = True

class MAIN:
    def __init__(self):
        self.state = "TITLE_SCREEN"

        self.start_button = START_BUTTON()
        
        self.title_screen_button = TITLE_BUTTON()
        self.retry_button = PLAY_AGAIN_BUTTON()

        self.snek = SNAKE()
        self.fruit = FRUIT()
        self.score = "0"
        
        while self.snek.body[0] == self.fruit.pos:
            self.fruit.randomize()

    def update(self):
        # No need for a PLAY state here because the game_update occurs at a different interval than these updates
        if self.state == "PLAY":
            return
        elif(self.state == "TITLE_SCREEN"):
            self.update_title_screen()
        elif self.state == "GAME_OVER":
            self.update_game_over()
    
    def update_title_screen(self):
        self.start_button.check_click()

    def update_game_over(self):
        self.title_screen_button.check_click()
        self.retry_button.check_click()

    def update_game(self):
        self.snek.move_snake()
        self.check_food()
        self.check_fail()

    def draw(self):
        if(self.state == "TITLE_SCREEN"):
            self.draw_title_screen()
        elif self.state == "PLAY":
            self.draw_game()
        elif self.state == "GAME_OVER":
            self.draw_game_over()

    def draw_title_screen(self):
        title_surface = title_font.render("Welcome To Snek", True, 'white')
        title_x = TILE_SIZE*TILE_NUM/2
        title_y = 70
        title_rect = title_surface.get_rect(center = (title_x, title_y))
        screen.blit(title_surface, title_rect)

        author_surface = score_font.render("By Blocky7277", True, 'white')
        author_x = TILE_SIZE*TILE_NUM - 90
        author_y = TILE_SIZE*TILE_NUM - 20
        author_rect = author_surface.get_rect(center = (author_x, author_y))
        screen.blit(author_surface, author_rect)

        self.start_button.draw()

    def draw_game(self):
        self.fruit.draw()
        self.snek.draw()
        self.draw_score()
    
    def draw_game_over(self):
        title_surface = title_font.render("Game Over", True, 'red')
        title_x = TILE_SIZE*TILE_NUM/2
        title_y = 50
        title_rect = title_surface.get_rect(center = (title_x, title_y))
        screen.blit(title_surface, title_rect)

        title_surface = title_font.render("Score: " + self.score, True, 'white')
        title_x = TILE_SIZE*TILE_NUM/2
        title_y = TILE_SIZE*TILE_NUM/2-50
        title_rect = title_surface.get_rect(center = (title_x, title_y))
        screen.blit(title_surface, title_rect)

        self.retry_button.draw()
        self.title_screen_button.draw()

    def draw_score(self):
        self.score = str(len(self.snek.body) -1)
        score_surface = score_font.render(self.score, True, 'white')
        score_x = TILE_SIZE*TILE_NUM - 20
        score_y = 20
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        screen.blit(score_surface, score_rect)

    def check_food(self):
        if self.fruit.pos == self.snek.body[0]:
            self.fruit.randomize(self.snek.body)
            self.fruit.eaten += 1
            self.snek.add_segment()

    def check_fail(self):
        if 0 > self.snek.body[0].x or TILE_NUM <= self.snek.body[0].x or 0 > self.snek.body[0].y or TILE_NUM <= self.snek.body[0].y:
            self.state = "GAME_OVER"
            self.snek = SNAKE()
            self.fruit = FRUIT()
        for segment in self.snek.body[1:]:
            if segment == self.snek.body[0]:
                self.state = "GAME_OVER"
                self.snek = SNAKE()
                self.fruit = FRUIT()

class START_BUTTON:
    def __init__(self):
        self.button_surface = title_font.render("Start", True, 'green')
        self.button_rect = self.button_surface.get_rect(center=(TILE_NUM*TILE_SIZE/2, TILE_SIZE*TILE_NUM/2))

    def draw(self):
        screen.blit(self.button_surface, self.button_rect)

    def check_click(self):
        pos = pygame.mouse.get_pos()
        if(self.button_rect.collidepoint(pos)):
            if(pygame.mouse.get_pressed()[0]):
                main_game.state = "PLAY"

class TITLE_BUTTON:
    def __init__(self):
        self.button_surface = button_font.render("Title Screen", True, 'green')
        self.button_rect = self.button_surface.get_rect(center=(TILE_NUM*TILE_SIZE/2, TILE_SIZE*TILE_NUM/2 + 200))

    def draw(self):
        screen.blit(self.button_surface, self.button_rect)

    def check_click(self):
        pos = pygame.mouse.get_pos()
        if(self.button_rect.collidepoint(pos)):
            if(pygame.mouse.get_pressed()[0]):
                main_game.state = "TITLE_SCREEN"

class PLAY_AGAIN_BUTTON:
    def __init__(self):
        self.button_surface = button_font.render("Play Again", True, 'green')
        self.button_rect = self.button_surface.get_rect(center=(TILE_NUM*TILE_SIZE/2, TILE_SIZE*TILE_NUM/2 + 100))

    def draw(self):
        screen.blit(self.button_surface, self.button_rect)

    def check_click(self):
        pos = pygame.mouse.get_pos()
        if(self.button_rect.collidepoint(pos)):
            if(pygame.mouse.get_pressed()[0]):
                main_game.state = "PLAY"
        



pygame.init()
pygame.display.set_caption("SNEK")
TILE_SIZE, TILE_NUM = int(35), 20
screen = pygame.display.set_mode([TILE_SIZE*TILE_NUM]*2, pygame.SCALED | pygame.FULLSCREEN)
snake = pygame.rect.Rect([0,0,TILE_SIZE-2,TILE_SIZE-2,])
length = 1
snake_dir = Vector2(0, 0)
time, time_step = 0, 100
clock = pygame.time.Clock()
score_font = pygame.font.Font(None, 25)
title_font = pygame.font.Font(None, 75)
button_font = pygame.font.Font(None, 40)
mouse1 = Vector2(0,0)
mouse2 = Vector2(0,0)

def get_input():
    if event.key == pygame.K_w:
        main_game.snek.direction = Vector2(0, -1)
    elif event.key == pygame.K_s:
        main_game.snek.direction = Vector2(0, 1)
    elif event.key == pygame.K_a:
        main_game.snek.direction = Vector2(-1, 0)
    elif event.key == pygame.K_d :
        main_game.snek.direction = Vector2(1, 0)


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == SCREEN_UPDATE and main_game.state == "PLAY":
            main_game.update_game()
        # Run state updates
        main_game.update()

        # Collect Input
        if event.type == pygame.KEYDOWN:
            if main_game.state == "PLAY":
                get_input()
            if event.key == pygame.K_ESCAPE:
                    exit()
        if main_game.state == "PLAY":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(pygame.mouse.get_pressed()[0]):
                    mouse1 = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
            elif event.type == pygame.MOUSEBUTTONUP:
                if(not pygame.mouse.get_pressed()[0]):
                    mouse2 = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    delta_x = mouse2.x - mouse1.x
                    delta_y = mouse2.y - mouse1.y
                    if(abs(delta_x) > abs(delta_y)):
                        if delta_x < 0:
                            main_game.snek.direction = Vector2(-1, 0)
                        else:
                            main_game.snek.direction = Vector2(1, 0)
                    else:
                        if delta_y < 0:
                            main_game.snek.direction = Vector2(0, -1)
                        else:
                            main_game.snek.direction = Vector2(0, 1)
        screen.fill((20,20,20))
        main_game.draw()
        pygame.display.update()
        clock.tick(200)
