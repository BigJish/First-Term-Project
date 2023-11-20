from settings import *

from Textbox import *
from Button import *
from TextFile import *

class Login:
    def __init__(self):
        self.win = display.get_surface()
        self.f = TextFile()
        self.userTextBox = TextBox(200,250)
        self.passTextBox = TextBox(200,400)
        self.b = Button(360, 550, "Eneter")       
    
    def screen(self):
        self.win.fill((200,200,200))
        draw.rect(self.win, (100,100,100), (0,0,720,720),20)
        
    def run(self, events):
        for i in events:
            self.userTextBox.input(i)
            self.passTextBox.input(i)

        self.screen()
        self.userTextBox.update()
        self.passTextBox.update()

        if self.b.check() == True and self.userTextBox.txt != "" and self.passTextBox.txt != "":
            username = self.userTextBox.getText()
            password = self.passTextBox.getText()
            self.f.newUser(username, password)
            return True
        self.b.update()