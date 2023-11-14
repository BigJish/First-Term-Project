from pygame import *
from Text import *

class EndScreen:
    def __init__(self, time):
        self.win = display.get_surface()
        self.text = Text(fontSize = 86)
        self.image = image.load("confettii.png").convert_alpha()
        self.text.render("Your time was: "+str(time))

    def run(self):
        self.text.draw(540 - self.text.get_w() // 2, 120 - self.text.get_h() // 2)
        self.win.blit(self.image, (100,420))
        self.win.blit(self.image, (390,420))
        self.win.blit(self.image, (680,420))