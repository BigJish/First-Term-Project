from pygame import *
from Text import *

class Display:
    def __init__(self):
        self.win = display.get_surface()
        self.text = Text(fontSize = 32)
        self.barHeight = 120
    def getTime(self):
        return self.time

    def timer(self, time):
        self.time = time
        self.text.render(time)
        self.text.draw(60, 60)
    
    def jumpMeter(self, jumpPower):
        jumpPower = round(jumpPower,1)
        draw.rect(self.win, (100,100,100), (1000, 460, 30, 180))     
        draw.rect(self.win, (255,255,0), (1000, 640-(jumpPower*10), 30, (jumpPower*10)))

    def update(self, time, jumpPower):
        self.timer(time)
        self.jumpMeter(jumpPower)