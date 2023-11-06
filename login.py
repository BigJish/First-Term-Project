from settings import *

class Login:
    def __init__(self):
        self.win = display.get_surface()
        self.quit = False
    
    def inputs(self):
        for i in event.get():
            if i.type == QUIT:
                self.quit = True
    
    def screen(self):
        self.win.fill((200,200,200))
        draw.rect(self.win, (100,100,100), (0,0,720,720),20)
        draw.rect(self.win, (255,255,255), (200,250,320,40))
        draw.rect(self.win, (255,255,255), (200,400,320,40))
    
    def run(self):
        while self.quit == False:
            inputs = self.inputs()
            self.screen()

            CLOCK.tick(60)
            display.flip()
        quit()