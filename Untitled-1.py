from pygame import *
from time import *
w = 700
h = 500
window = display.set_mode((w, h))
display.set_caption('pingpong')
c = (121,34,76)
window.fill(c)
game = True


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.y += self.speed
        if keys[K_d] and self.rect.x < w -80:
            self.rect.y -= self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.y += self.speed
        if keys[K_RIGHT] and self.rect.x < w -80:
            self.rect.y -= self.speed


rocket = Player('ba.png', 80, -80, 20, 20, 1)
rocket2 = Player('ba.png', 480, -80, 20, 20, 1)

FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(c)
    display.update()
