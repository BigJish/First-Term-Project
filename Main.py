from settings import *
from login import *

class Main:
    def __init__(self):
        self.srcN0 = 1
        self.win = display.set_mode((720,720))
        self.login = Login()
    
    def run(self):
        self.login.run()

main = Main()
main.run()