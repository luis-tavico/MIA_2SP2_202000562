import os

class Rmdisk:
    def __init__(self, path = ""):
        self.path = path
        self.username = os.getlogin()
        self.mensajes = ""
        self.errors = 0
    
    def setPath(self, path):
        self.path = path.replace("user", self.username).replace('"', "")
        if not(os.path.exists(self.path)):
            self.errors += 1
            self.mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> El disco no existe.</span><br>\n'
    
    def getPath(self):
        return self.path

    def deleteDisk(self):
        '''
        question = (f'¿Desea eliminar el disco {self.path} (s/n) ')
        r = input("\033[1;33m<<Confirm>> {}\033[00m\n" .format(question))
        if (r == 's'): 
            os.remove(self.path)
            print("\033[1;32m<<Success>> {}\033[00m" .format("Disco eliminado exitosamente."))
        '''

#'<span class="text-warning"><i class="fa-solid fa-triangle-exclamation"></i> ¿Desea eliminar el disco (s/n)?</span><br>'