import pygame
from sys import exit
from settings import *
from map import *
from player import *
from raycast import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *


class GAME:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(RES) #, pygame.SCALED | pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()
    
    def new_game(self):
        self.map = MAP(self)
        self.player = PLAYER(self)
        self.object_renderer = OBJECT_RENDERER(self)
        self.raycast = RAYCAST(self)
        self.object_handler = OBJECT_HANDLER(self)
        self.sound = SOUND(self)
        self.weapon = WEAPON(self)

    def update(self):
        self.player.update()
        self.raycast.update()
        self.object_handler.update()
        self.weapon.update()
        pygame.display.update()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(str(self.clock.get_fps()))
    
    def draw(self):
        # self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()
        # self.map.draw()
        # self.player.draw()
    
    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                exit()
            self.player.single_fire(event)

    def run(self):
        while True:
            self.event_handler()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = GAME()
    game.run()