from pygame import *
from time import time as timer
w = 600
h = 500
window = display.set_mode((w, h))
display.set_caption('pingpong')
c = (121,34,76)
window.fill(c)
game = True
finish = False

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
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < w -80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < w -80:
            self.rect.y += self.speed


rocket = Player('ro.png', 30, 200, 50, 150, 4)
rocket2 = Player('ro.png', 520,200, 50, 150, 4)
ball = GameSprite('ba.png', 200, 200, 50, 50, 4)

font.init()
font = font.Font(None,35)
lose = font.render(' player 1 lose', True, (180,0,0))
lose2 = font.render(' player 2 lose', True, (180,0,0))

speed_x = 3
speed_y = 3
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(c)
        rocket.update_l()
        rocket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(rocket,ball) or sprite.collide_rect(rocket2,ball) :
            speed_x *= -1
        if ball.rect.y > h - 50 or ball.rect.y < 0 :
            speed_y *= -1
        if ball.rect.x < 0:
            window.blit(lose,(200,200))
            finish = True
        if ball.rect.x > w:
            window.blit(lose2,(200,200))
            finish = True
        rocket.reset()
        rocket2.reset()
        ball.reset()

    display.update()
    time.delay(20)   
