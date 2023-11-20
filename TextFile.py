from settings import *

class TextFile:
    def __init__(self):
        f = open("Database.txt","w")
        dump([], f)
        f.close()
    
    def newUser(self, name, password):
        tempFile = []
        f = open("Database.txt","r")
        tempFile = load(f)
        f.close()
        f = open("Database.txt","w")
        tempFile.append({"username":name, "password": password, "highscore": None, "previous":None})
        dump(tempFile,f)
        f.close()
        print(tempFile)
