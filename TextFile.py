from settings import *

class TextFile:
    def __init__(self):
        f = open("Database.txt", "w")
        f.close()
    
    def load(self, type):
        self.f = open("Database.txt",type)
    
    def newUser(self, name, password):
        self.load("w")
        tempFile = load(self.f)
        tempFile.append({"username":name, "password": password, "highscore": None, "previous":None})
        dump(tempFile,self.f)
        print(tempFile)
