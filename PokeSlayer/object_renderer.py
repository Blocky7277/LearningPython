import pygame
from settings import *

class OBJECT_RENDERER:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture("recources/textures/Cave4.png", (WIDTH, HALF_WIDTH))
        self.sky_offset = 0

    def draw(self):
        self.draw_bg()
        self.render_game_objects()

    def draw_bg(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        pygame.draw.rect(self.screen, (64,35,0), (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        objects = sorted(self.game.raycast.unrendered_objects, key=lambda t: t[0], reverse=True)
        for depth, image, pos in objects:
            self.screen.blit(image, pos)
    
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('recources/textures/Cave1.png'),
            2: self.get_texture('recources/textures/Cave2.png'),
            3: self.get_texture('recources/textures/Cave3.png'),
            4: self.get_texture('recources/textures/Cave4.png'),
        }