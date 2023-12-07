from settings import *
from random import choice as rc
from random import randint as ri

from Player import * 
from Block import *
from Finish import *
from Display import *
from EndScreen import *
from DropDown import *
from TitleScreen import *


class MapGen:
    def __init__(self, level):
        self.lastY = 650
        self.level = level
        self.coords = []

    def generate(self):
        for i in range(0,self.level):
            x1 = ri(100, 880)

            x2 = ri(100,880)
            while x1-150 < x2 < x1+150:
                x2 = ri(100,880)

            x3 = ri(100,880)
            while x1-150 < x3 < x1+150 or x2-150 < x3 < x2+150:
                x3 = ri(100,880)

            y = self.lastY - rc([110, 120, 130])
            new_coord = [x1,y-120*i]
            self.coords.append(new_coord)
            y = self.lastY - rc([110, 120, 130])
            new_coord = [x2,y-120*i]
            self.coords.append(new_coord)
            y = self.lastY - rc([110, 120, 130])
            new_coord = [x3,y-120*i]
            self.coords.append(new_coord)

class Game:
    def __init__(self):
        self.win = display.get_surface()
        self.blocks = sprite.Group()
        self.display = Display()
        self.DropDown = DropDown()
        self.endScreen = EndScreen()
        self.t = t()
        self.offset = 0
        self.level = 20
        self.screen = 0
        self.pauseTime = 0
        self.keydown = False
        
        self.setup()
    
    def setup(self):
        self.title = TitleScreen()
        self.player = Player(self.blocks)
        Block(self.blocks, 80, 650, type = "ground")
        self.map = MapGen(self.level)
        self.map.generate()
        for i in self.map.coords:
            Block(self.blocks, i[0], i[1])
        self.finish = Finish(500-self.level*120)
    
    def run(self, username):

        k = key.get_pressed()
        if self.screen == 0:
            if self.title.run(username) == True:
                self.t = t()
                self.screen = 1

        if self.screen == 1:

            if k[K_ESCAPE]:
                if self.keydown == False:
                    self.screen = 3
                    self.pauseTime = t()
                    self.keydown = True
            
            else:
                self.keydown = False

            self.win.fill((0,200,200))
            for i in self.blocks:
                i.draw(self.offset)

            self.finish.draw(self.offset)

            self.player.update(self.offset)
            if self.player.rect.y-self.offset < 250:
                self.offset -= 3
            elif self.player.rect.y-self.offset > 450:
                self.offset += 6
            
            if self.player.hitbox.colliderect(self.finish.hitbox):
                self.screen = 2
            
            self.display.update(str(round(t() - self.t, 2)), self.player.get_JP())
        
        if self.screen == 2:
            self.endScreen.update(self.display.getTime(), username)
            self.endScreen.run()
            self.screen = 3
        
        if self.screen == 3:
            if self.DropDown.inputs() == "reset":
                self.end = False
                self.blocks = sprite.Group()
                self.offset = 0
                self.level = 20
                self.screen = 0
                self.display = Display()
                self.DropDown = DropDown()
                self.setup()

            if k[K_ESCAPE]:
                if self.keydown == False:
                    self.screen = 0
                    self.t += t() - self.pauseTime
                    self.keydown = True
            else:
                self.keydown = False