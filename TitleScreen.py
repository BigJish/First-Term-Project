from settings import *
from Button import *
from Text import *
from TextFile import *

class TitleScreen:
    def __init__(self):
        self.win = display.get_surface()
        self.f = TextFile()
        self.start = Button(440, 550, "Start")
        self.text1 = Text(fontSize = 128)
        self.text2 = Text(fontSize = 64)

    def run(self, username):
        self.win.fill((0,50,200))
        self.text1.render("Welcome "+ username)
        self.text1.draw(540 - self.text1.get_w() // 2, 200 - self.text1.get_h() // 2)
        self.text2.render("Your Previous Score is "+str(self.f.search(username, "previous")))
        self.text2.draw(540 - self.text2.get_w() // 2, 350 - self.text2.get_h() // 2)
        self.text2.render("Your Highscore is "+str(self.f.search(username, "highscore")))
        self.text2.draw(540 - self.text2.get_w() // 2, 420 - self.text2.get_h() // 2)

        if self.start.check():
            return True
        self.start.update()