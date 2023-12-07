from settings import *

from Textbox import *
from Button import *
from TextFile import *
from Text import *

class Login:
    def __init__(self):
        self.win = display.get_surface()
        self.f = TextFile()
        self.text = Text(fontSize = 58)
        self.errorText = Text(fontSize = 24, colour = (200,50,50))
        self.errorText.render("Username exists password is incorrect")
        self.userTextBox = TextBox(200,250)
        self.passTextBox = TextBox(200,400)
        self.b = Button(200, 500, "Enter")     
        self.errorTime = 0
    
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
        self.text.render("Username")
        self.text.draw(200, 200)
        self.text.render("Password")
        self.text.draw(200,350)


        if self.b.check() == True and self.userTextBox.txt != "" and self.passTextBox.txt != "":
            username = self.userTextBox.getText()
            password = self.passTextBox.getText()
            if self.f.newUser(username, password) == False:
                self.errorTime  = t()
            else:
                return True
        if t()-self.errorTime <= 2:
            self.errorText.draw(200, 450)

        self.b.update()
