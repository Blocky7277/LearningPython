import pygame
from settings import *
import os
from collections import deque

class SPRITE_OBJ:
    def __init__(self, game, path, pos, scale = 1, shift = 0):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pygame.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDTH = self.IMAGE_WIDTH // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_width = 0
        self.sprite_scale = scale
        self.sprite_shift = shift

    def get_sprite_projection(self):
        proj = SCREEN_DIST/self.norm_dist * self.sprite_scale
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        image = pygame.transform.scale(self.image, (proj_width, proj_height))

        self.sprite_half_width = proj_width // 2
        height_shift = proj_height * self.sprite_shift 
        pos = self.screen_x - self.sprite_half_width, HALF_HEIGHT - proj_height // 2 + height_shift

        self.game.raycast.unrendered_objects.append((self.norm_dist, image, pos))

    def get_sprite(self):
        delta_x = self.x - self.player.x
        delta_y = self.y - self.player.y
        self.dx, self.dy = delta_x, delta_y
        self.theta = math.atan2(delta_y, delta_x)
        
        delta = self.theta - self.player.angle
        if (delta_x > 0 and self.player.angle > math.pi) or (delta_x < 0 and delta_y < 0):
            delta += math.tau

        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_RAY_NUM + delta_rays) * SCALE

        self.dist = math.hypot(delta_x, delta_y)
        self.norm_dist = self.dist * math.cos(delta)

        if -self.IMAGE_HALF_WIDTH < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDTH) and self.norm_dist > 0.5:
            self.get_sprite_projection()

    def update(self):
        self.get_sprite()

class ANIMATED_SPRITE(SPRITE_OBJ):
    def __init__(self, game, path, pos = (1, 1), scale=1, shift=0, frame_time=60):
        super().__init__(game, path, pos, scale, shift)
        self.frame_time = frame_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.frame_time_prev = pygame.time.get_ticks()
        self.animation_trigger = False

    def update(self):
        super().update()
        self.check_animation()
        self.animate(self.images)

    def animate(self, images):
        if self.animation_trigger:
            images.rotate(-1)
            self.image = images[0]

    def check_animation(self):
         self.animation_trigger = False
         now = pygame.time.get_ticks()
         if(now - self.frame_time_prev > self.frame_time):
            self.frame_time_prev = now
            self.animation_trigger = True

    def get_images(self, path):
        images = deque()
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                img = pygame.image.load(path + "/" + file).convert_alpha()
                images.append(img)
        return images