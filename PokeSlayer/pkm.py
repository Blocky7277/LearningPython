from sprite_object import *
from random import randint, random, choice

class PKM(ANIMATED_SPRITE):
    def __init__(self, game, path='recources/pkmn/charizard/frame_000_delay-0.05s.gif', pos = (7.5, 4.5), scale = .5, shift = .2, frame_time = 30):
        super().__init__(game, path, pos, scale, shift, frame_time)
        self.idle = self.get_images(self.path + '/idle')

        self.atk_dist = randint(3,6)
        self.speed = .03
        self.size = 10
        self.health = 100
        self.atk_dmg = 10
        self.acc = .2
        self.alive = True
        self.pain = False

    def update(self):
        self.check_animation()
        self.get_sprite()
        self.logic()

    def logic(self):
        if self.alive:
            self.animate(self.idle)