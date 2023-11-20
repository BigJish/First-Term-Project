from settings import *


class Text:
    def __init__(self, colour = (0,0,0), fontType = None, fontSize = 32):
        self.win = display.get_surface()
        self.colour = colour
        self.fontSize = fontSize
        self.font = font.Font(fontType, fontSize)
    
    def render(self,text):
        self.text = self.font.render(text, True, self.colour)
    
    def get_w(self):
        return self.text.get_width()
    
    def get_h(self):
        return self.text.get_height()
    
    def draw(self, x, y):
        self.win.blit(self.text, (x, y))