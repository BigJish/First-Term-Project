from settings import *
from Text import *
from TextFile import *

class EndScreen:
    def __init__(self, time, username):
        self.win = display.get_surface()
        self.f = TextFile()
        self.score = time

        self.text = Text(fontSize = 86)
        self.image = image.load("confetti.png").convert_alpha()
        self.text.render("Your time was: "+str(time))

        self.username = username

    def update(self):
        self.f.update(self.username, "highscore", self.score)
        self.f.update(self.username, "previous", self.score)

    def run(self):
        self.win.fill((0,200,200))
        self.text.draw(540 - self.text.get_w() // 2, 120 - self.text.get_h() // 2)
        self.win.blit(self.image, (100,420))
        self.win.blit(self.image, (390,420))
        self.win.blit(self.image, (680,420))