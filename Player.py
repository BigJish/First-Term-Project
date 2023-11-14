from pygame import *
from time import time as t

class Player(sprite.Sprite):
    def __init__(self,blocks):
        self.win = display.get_surface()
        img1 = image.load("Player_Sprite_Image_1.png").convert_alpha()
        img2 = image.load("Player_Sprite_Image_2.png").convert_alpha()
        self.images = [img1, img2]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = 500,590 
        self.hitbox = self.rect
        self.jump = True
        self.grav = 0.6
        self.yMove = 0
        self.xMove = 0
        self.blocks = blocks
        self.charge = False
        self.chargeTime = 0
        self.jumpPower = 0
    
    def get_JP(self):
        return self.jumpPower

    def input(self):

        k = key.get_pressed()
        self.xMove = 0

        if k[K_SPACE] or k[K_w] or k[K_UP]:
            if self.jump != True:
                if self.charge == False:
                    self.chargeTime = t()
                self.charge = True
                self.image = self.images[1]

        if self.jump == True:
                self.charge = False
                self.image = self.images[0] 

        if self.charge:
            self.jumpPower = (t()-self.chargeTime)*20
            if self.jumpPower >= 18:
                self.jumpPower = 18
        
        else:
            self.jumpPower = 0

        if self.charge == True and k[K_SPACE] != True:
            self.yMove = -self.jumpPower
            self.jump = True
            self.charge = False
        if self.charge == False:
            if k[K_a] or k[K_LEFT]:
                self.xMove += -3
            
            if k[K_d] or k[K_RIGHT]:
                self.xMove += 3

    
    def move(self):
        self.jump = True
        self.yMove += self.grav
        self.hitbox.y += self.yMove
        self.collide("y")
        self.hitbox.x += self.xMove
        self.collide("x")
        self.rect = self.hitbox

    def collide(self, axis):
        for i in self.blocks:
            if axis == "x":
                if self.hitbox.colliderect(i.hitbox ):
                    if self.xMove < 0:
                        self.hitbox.left = i.hitbox.right
                    if self.xMove > 0:
                        self.hitbox.right = i.hitbox.left


            if axis == "y":
                if self.hitbox.colliderect(i.hitbox):
                    if self.yMove > 0:
                        self.hitbox.bottom = i.hitbox.top
                        self.yMove = 0
                        self.jump = False
                    if self.yMove < 0:
                        self.hitbox.top = i.hitbox.bottom
                        self.yMove = 0


    def draw(self,offset):
        if self.image == self.images[0]:
            self.win.blit(self.image, (self.rect.x,self.rect.y-offset))
            
        if self.image == self.images[1]:
            self.win.blit(self.image, (self.rect.x-10,self.rect.y-offset+20))
    
    def update(self, offset):
        self.input()
        self.move()
        self.draw(offset)