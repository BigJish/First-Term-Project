from settings import *

class TextFile:
    def __init__(self):
        pass
    
    def update(self, username, newdata):
        tempfile = self.read()
        highscore = False
        for i in tempfile:
            if i["username"] == username:
                if i["highscore"] == None:
                    i["highscore"] = newdata
                    highscore = True
                elif i["highscore"] > newdata:
                    i["highscore"] = newdata
                    highscore = True
                i["previous"] = newdata
                f = open("Database.txt","w")
                dump(tempfile,f)
                f.close()
                return highscore

    def search(self, username, data):
        tempfile = self.read()
        for i in tempfile:
            if i["username"] == username:
                return i[data]

    def read(self):
        f = open("Database.txt","r")
        tempfile = load(f)
        f.close()
        return tempfile

    def add(self, username, password):
        tempFile = self.read()
        f = open("Database.txt","w")
        tempFile.append({"username":username, "password": password, "highscore": None, "previous":None})
        dump(tempFile,f)
        f.close()
    
    def check(self, username, password):
        tempFile = self.read()
        found = False
        for i in tempFile:
            if username == i["username"]:
                found = True
                if password != i["password"]:
                    return False
                
        if found == False:
            try:
                self.add(username, password)
            except:
                print("There is an error with your username or password\n please try again")

    def newUser(self, username, password):
        check = self.check(username, password)
        if check == False:
            return False