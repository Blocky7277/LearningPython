import pygame

_ = False

mini_map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,1,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,1,1,1,_,_,_,1,1,1,_,_,1],
    [1,1,_,_,_,_,1,_,_,_,_,_,1,_,_,1],
    [1,_,_,_,_,_,1,_,_,_,_,_,1,_,_,1],
    [1,1,_,1,1,1,1,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,3,3,3,3,_,_,_,1],
    [1,_,_,3,_,_,_,3,_,_,_,_,_,_,_,1],
    [1,_,_,3,_,_,_,3,_,_,_,_,_,_,_,1],
    [1,_,_,3,_,_,_,3,_,_,_,_,_,_,_,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1],
    [1,_,_,3,_,_,_,3,_,_,_,_,_,_,_,1],
    [1,_,_,3,_,_,_,3,_,_,_,_,_,_,_,1],
    [1,_,_,3,_,_,_,3,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,4,4,4,1],
    [1,_,_,3,_,_,_,3,_,_,_,_,4,_,_,1],
    [1,_,_,3,_,_,_,3,_,_,_,_,4,_,_,1],
    [1,_,_,3,_,_,_,3,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

class MAP:
    def __init__(self, game):
        self.game = game
        self.mini_map =  mini_map
        self.world_map = {}
        self.get_map()
    
    def get_map(self):
        for i, row in enumerate(self.mini_map):
            for j, value in enumerate(row):
                if value:
                    self.world_map[(j,i)] = value
    
    def draw(self):
        [pygame.draw.rect(self.game.screen, 'gray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
        for pos in self.world_map]