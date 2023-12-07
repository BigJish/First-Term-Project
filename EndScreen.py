from settings import *
from Text import *
from TextFile import *

class EndScreen:
    def __init__(self ):
        self.win = display.get_surface()
        self.f = TextFile()
        self.text = Text(fontSize = 84)
        self.image = image.load("confetti.png").convert_alpha()
        

    def update(self, time, username):
        self.score = time
        self.newBest = self.f.update(username, self.score)
        self.text.render("Your time was: "+str(time))
        
        
        


    def run(self):
        self.win.fill((0,200,200))
        self.text.draw(540 - self.text.get_w() // 2, 120 - self.text.get_h() // 2)
        if self.newBest:
            self.text.render("New Highscore!!")
            self.text.draw(540 - self.text.get_w() // 2, 220 - self.text.get_h() // 2)
        self.win.blit(self.image, (100,420))
        self.win.blit(self.image, (390,420))
        self.win.blit(self.image, (680,420))