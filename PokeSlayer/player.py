from settings import *
import pygame
import math

class PLAYER:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle =  PLAYER_ANGLE
        self.shot = False

    def single_fire(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.game.sound.pistol.set_volume(.3)
                self.game.sound.pistol.play()
                self.shot = True
                self.game.weapon.reloading = True
    
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        delta_x , delta_y = 0,0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            delta_x += speed_cos
            delta_y += speed_sin
        if keys[pygame.K_s]:
            delta_x += -speed_cos
            delta_y += -speed_sin
        if keys[pygame.K_a]:
            delta_y += -speed_cos
            delta_x += speed_sin
        if keys[pygame.K_d]:
            delta_y += speed_cos
            delta_x += -speed_sin

        self.check_wall_collision(delta_x, delta_y)

        if keys[pygame.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def mouse_view(self):
        mx,my = pygame.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pygame.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pygame.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENS * self.game.delta_time


    def check_wall(self, x, y):
        return (x,y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SCALE_SIZE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y+dy * scale)):
            self.y += dy

    def update(self):
        self.movement()
        self.mouse_view()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

    def draw(self):
        pygame.draw.line(self.game.screen, 'red', (self.x*100, self.y*100),
            (self.x * 100 + WIDTH * math.cos(self.angle),
             self.y * 100 + HEIGHT * math.sin(self.angle)), 2)
        pygame.draw.circle(self.game.screen, 'green', (self.x*100, self.y*100), 15)