import os

class Mkdisk:
    def __init__(self, size = 0, path = "", fit = "FF", unit = "M"):
        self.size = size
        self.path = path
        self.fit = fit
        self.unit = unit
        self.username = os.getlogin()
        self.mensajes = ""
        self.errors = 0

    #SET
    def setSize(self, size):
        if (size > 0):
            self.size = size
        else:
            self.errors += 1
            self.mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> El valor del parametro "size" debe ser mayor a 0.</span><br>\n'

    def setPath(self, path):
        self.path = path.replace("user", self.username).replace('"', "")
        if not(os.path.exists(self.path)):
            carpetas = os.path.dirname(self.path)
            if not(os.path.exists(carpetas)):
                os.makedirs(carpetas)
        else:
            self.errors += 1
            self.mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> El disco ya existe.</span><br>\n'
    
    def setFit(self, fit):
        if (fit.lower() == "bf"):
            self.fit = fit
        elif (fit.lower() == "ff"):
            self.fit = fit
        elif (fit.lower() == "wf"):
            self.fit = fit
        else:
            self.errors += 1
            self.mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> El valor del parametro "fit" debe ser "BF", "FF" o "WF".</span><br>\n'

    def setUnit(self, unit):
        if (unit.lower() == 'k'):
            self.unit = unit
        elif (unit.lower() == 'm'):
            self.unit = unit
        else:
            self.errors += 1
            self.mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> El valor del parametro "unit" debe ser "K" o "M".</span><br>\n'
    
    #GET
    def getSize(self):
        return self.size
    
    def getPath(self):
        return self.path
    
    def getFit(self):
        return self.fit
    
    def getUnit(self):
        return self.unit