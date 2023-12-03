from settings import *

class TextFile:
    def __init__(self):
        pass
    
    def update(self, username, data, newdata):
        tempfile = self.read()
        for i in tempfile:
            if username == i["username"]:
                f = open("Database.txt","w")
                if data == "highscore": 
                    if i[data] == None:
                        i[data] = newdata
                        dump(tempfile,f)
                    elif i[data] > newdata:
                        i[data] = newdata
                        dump(tempfile,f)
                elif data == "previous":
                    i[data] = newdata
                    dump(tempfile,f)
                f.close()

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
            self.add(username, password)

    def newUser(self, username, password):
        check = self.check(username, password)
        if check == False:
            return False