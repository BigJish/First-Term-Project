from settings import *
from login import *
from Game import *

class Main:
    def __init__(self):
        self.srcNo = 1
        self.win = display.set_mode((720,720))
        self.login = Login()
        self.game = Game()
        self.quit = False
    
    def run(self):
        while self.quit == False:
            events= event.get()
            for i in events:
                if i.type == QUIT:self.quit = True

            if self.srcNo == 1:
                if self.login.run(events):
                    self.srcNo = 2
                    self.win = display.set_mode((1080,720))

                    
            if self.srcNo == 2:
                self.game.run()

            display.flip()
            CLOCK.tick(60)
        quit()

main = Main()
main.run()