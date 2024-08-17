import pygame

class SOUND:
    def __init__(self, game):
        self.game = game
        pygame.mixer.init()
        self.path = "recources/sounds/"
        self.pistol = pygame.mixer.Sound(self.path + 'pistol/pew.mp3')