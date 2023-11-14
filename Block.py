from pygame import *

class Block(sprite.Sprite):
    def __init__(self, groups, x, y, hitboxStatus = False, type = "platform"):
        super().__init__(groups)
        if type == "platform":
            self.image = image.load("Platform.png").convert_alpha()
        elif type == "ground":
            self.image = image.load("Ground.png").convert_alpha()
        self.win = display.get_surface()
        self.hitboxStatus = hitboxStatus
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.hitbox = self.rect
    
    def draw(self,offset):
        if self.hitboxStatus == True:
            draw.rect(self.win, (255,0,0), self.rect, 2)
        else:
            self.win.blit(self.image, (self.rect.x, self.rect.y-offset))