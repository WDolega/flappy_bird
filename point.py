from random import randint

import pygame

pygame.init()
resolution = (1280, 720)
window = pygame.display.set_mode((1000, 720))
game_font = pygame.font.Font('font/04B_19.ttf', 40)
game_font2 = pygame.font.Font('font/04B_19.ttf', 42)


def draw_text(window, font, string, rgb, cords):
    text_img3 = pygame.font.Font.render(font, string, True, rgb)
    window.blit(text_img3, cords)


class Physic:
    def __init__(self, x, y, width, height):
        self.x_cord = x
        self.y_cord = y
        self.ver_velocity = 4
        self.hor_velocity = 4
        self.width = width
        self.height = height
        self.previous_x = x
        self.previous_y = y
        self.jumping = False
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def physic_tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)  # odświeżanie hitboxa


class Object(Physic):
    def __init__(self):
        self.rand = randint(0, 200)
        # self.x_cord = 830
        # self.y_cord = 220 + self.rand
        self.image = pygame.image.load("png/pipe-red.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        super().__init__(1280, 400 + self.rand, self.width, self.height)
        self.speed = 6

    def tick(self):
        self.x_cord -= self.hor_velocity
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


class Pip(Object):
    def __init__(self):
        super().__init__()
        self.y_cord = self.rand - 200
        self.image = pygame.transform.rotate(self.image, 180)


class Player(Object):
    def __init__(self):
        super().__init__()
        self.x_cord = 100
        self.y_cord = 350
        self.image = pygame.image.load("png/bird1.png")
        self.up_jump = pygame.image.load("png/yellowbird-upflap.png")
        self.down_jump = pygame.image.load("png/yellowbird-downflap.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.cooldown = 0
        self.hitbox = pygame.Rect(self.x_cord - 13, self.y_cord - 20, self.width - 18, self.height - 22)

    def collision(self):
        if self.y_cord + 20 < 0:
            self.y_cord = -20
        if self.x_cord + 13 < 0:
            self.x_cord = -13
        if self.y_cord + self.height - 18 > 720:
            self.y_cord = 720 - self.height + 18
        if self.x_cord + self.width - 22 > 1280:
            self.x_cord = 1280 - self.width + 22
            draw_text(window, game_font2, "DEFEAT", (255, 47, 0), (560, 100))

    def tick_bird(self, keys):
        self.physic_tick()
        self.collision()
        self.y_cord += self.ver_velocity
        self.hitbox = pygame.Rect(self.x_cord - 13, self.y_cord - 26, self.width - 18, self.height - 22)
        if keys[pygame.K_SPACE]:
            self.jumping = True
            cool1 = 0
            if self.cooldown == 0:
                self.y_cord -= self.speed * 2
                cool1 = pygame.time.get_ticks()
            self.cooldown = pygame.time.get_ticks() - cool1
            if self.cooldown > 1500:
                self.cooldown = 0
        self.previous_x = self.x_cord
        self.previous_y = self.y_cord


class Cash(Physic):
    def __init__(self):
        self.image = pygame.image.load("png/coin2.png")
        width = self.image.get_width()
        height = self.image.get_height()
        self.x_cord = 1520
        self.y_cord = randint(200, 500 - height)
        super().__init__(self.x_cord, self.y_cord, width, height)
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.x_cord -= self.hor_velocity
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


class Background:
    def __init__(self):
        self.bgimage = pygame.image.load('png/flapbgr.png')
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = 0
        self.bgX1 = 0

        self.bgY2 = 0
        self.bgX2 = self.rectBGimg.width

        self.moving_speed = 6

    def tick(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width

    def draw(self, window):
        window.blit(self.bgimage, (self.bgX1, self.bgY1))
        window.blit(self.bgimage, (self.bgX2, self.bgY2))
