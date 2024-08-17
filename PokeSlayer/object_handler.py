from sprite_object import *
from pkm import *

class OBJECT_HANDLER:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_path = 'recources/pkmn/'
        self.static_path = 'recources/static_sprites/'
        self.animated_path = "recources/animated_sprites/"
        sprite = self.add_sprite
        npc = self.add_npc

        sprite(SPRITE_OBJ(self.game, self.static_path + "pika.png", (3.5, 4.5), .8, .1))
        sprite(ANIMATED_SPRITE(self.game, self.animated_path + "pokeball/frame_0_delay-0.1s.png", (1.5, 4.5), .5, .5, 60))
        npc(PKM(self.game, ))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_npc(self, npc):
        self.npc_list.append(npc)