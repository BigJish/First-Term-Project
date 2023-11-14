from pygame import *
from Text import *


class Button:
    def __init__(self, x ,y, txt):
        self.win = display.get_surface()
        self.text = Text(fontSize=40)
        self.text.render(text=txt)
        self.rect = Rect(x, y, 200, 80)
        self.x = x
        self.y = y

    def check(self):
        p = mouse.get_pos()
        if self.rect.collidepoint(p) and mouse.get_pressed()[0]:
            return True

    def draw(self):
        p = mouse.get_pos()
        if self.rect.collidepoint(p):
            draw.rect(self.win, (120,120,120), self.rect)
        else:
            draw.rect(self.win, (180,180,180), self.rect)
        
        self.text.draw((self.x + 100) - self.text.get_w() // 2, (self.y + 40) - self.text.get_h() // 2)
    
    def update(self):
        self.draw()