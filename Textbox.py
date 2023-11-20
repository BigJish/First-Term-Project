from settings import *
from Text import *

class TextBox:
    def __init__(self, x, y):
        self.win = display.get_surface()
        self.rect = Rect(x,y,320,40)
        self.active = False
        self.txt = ""
        self.text = Text()


    def draw(self):
        if self.active or self.rect.collidepoint(mouse.get_pos()):
            draw.rect(self.win, (220,220,220), self.rect)
        else:
            draw.rect(self.win, (255,255,255), self.rect)
        self.text.render(self.txt)
        self.text.draw(self.rect.x+10,self.rect.y-(self.text.get_h()//2)+20)
    
    def input(self, input):
         if self.active == True:
            if input.type == KEYDOWN:
                    if input.key == K_BACKSPACE:
                        self.txt = self.txt[:-1]
                    
                    else:
                        self.txt += input.unicode

    def checkActive(self):
        mp = mouse.get_pos()
        ms = mouse.get_pressed()

        if self.rect.collidepoint(mp) and ms[0]:
            self.active = True
        elif ms[0]:
            self.active = False

    def getText(self):
        return self.txt
    
    def update(self):
        self.draw()
        self.checkActive()
        