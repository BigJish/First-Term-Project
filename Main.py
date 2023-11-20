from settings import *
from login import *
from Game import *

class Main:
    def __init__(self):
        self.srcNo = 1
        self.win = display.set_mode((720,720))
        self.login = Login()
        self.game = Game()
    
    def run(self):
        if self.srcNo == 1:
            if self.login.run():
                self.srcNo = 2
                
        if self.srcNo == 2:
            self.game.run()


main = Main()
main.run()