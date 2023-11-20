from settings import *

from Textbox import *
from Button import *

class Login:
    def __init__(self):
        self.win = display.get_surface()
        self.userTextBox = TextBox(200,250)
        self.passTextBox = TextBox(200,400)
        self.b = Button(360, 550, "Eneter")
        self.quit = False        
    
    def screen(self):
        self.win.fill((200,200,200))
        draw.rect(self.win, (100,100,100), (0,0,720,720),20)
        
    def run(self):
        while self.quit == False:
            for i in event.get():
                if i.type == QUIT:
                    self.quit = True
                self.userTextBox.input(i)
                self.passTextBox.input(i)

            self.screen()
            self.userTextBox.update()
            self.passTextBox.update()

            if self.b.check() == True and self.userTextBox.txt != "" and self.passTextBox.txt != "":
                self.quit = True
            
            self.b.update()

            CLOCK.tick(60)
            display.flip()
        quit()
        return True