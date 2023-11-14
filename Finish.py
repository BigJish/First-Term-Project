from pygame import *

class Finish:
    def __init__(self, y):
        self.rect = Rect(0, y, 1080, 20)
        self.win = display.get_surface()
        self.hitbox = self.rect
    
    def draw(self, offset):
        draw.rect(self.win, (200,200,0), (self.rect.x, self.rect.y-offset, self.rect.w, self.rect.h))
