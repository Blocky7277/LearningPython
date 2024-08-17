from sprite_object import *

class WEAPON(ANIMATED_SPRITE):
    def __init__(self, game, path="recources/pewpew/pistol1.png", scale=4, frame_time=60):
        super().__init__(game=game, path=path, scale=scale, frame_time=frame_time)
        self.images = deque(
            [pygame.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale)) for img in self.images]
        )
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.image_num = len(self.images)
        self.frame_counter = 0
        self.hp = 50

    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.image_num:
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        self.check_animation()
        self.animate_shot()