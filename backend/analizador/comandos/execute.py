import os

class Execute:
    def __init__(self, path = ""):
        self.path = path
        self.username = os.getlogin()
        self.mensajes = ""
        self.errors = 0

    #SET
    def setPath(self, path):
        self.path = path.replace("user", self.username).replace('"', "")
        if not(os.path.exists(self.path)):
            self.errors += 1
            self.mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> El archivo no existe.</span><br>\n'

    #GET
    def getPath(self):
        return self.path