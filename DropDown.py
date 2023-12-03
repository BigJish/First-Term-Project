from pygame import *
from Button import *

class DropDown:
    def __init__(self):
        self.win = display.get_surface()
        self.b = Button(440, 330, "reset")

    def inputs(self):
        if self.b.check():
            return "reset"
        
        self.b.update()

        