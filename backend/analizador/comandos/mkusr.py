class Mkusr:
    def __init__(self, user = "", password = "", grp = ""):
        self.user = user
        self.password = password
        self.grp = grp
        self.errors = 0
        self.mensajes = ""

    #SET
    def setUser(self, user):
        if (len(user)) > 10 :
            self.mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> El valor del parametro "user" no debe ser mayor a 10.</span><br>\n'
            self.errors += 1
        else:
            self.user = user

    def setPassword(self, password):
        if (len(password)) > 10 :
            self.mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> El valor del parametro "pass" no debe ser mayor a 10.</span><br>\n'
            self.errors += 1
        else:
            self.password = password

    def setGrp(self, grp):
        if (len(grp)) > 10 :
            self.mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> El valor del parametro "grp" no debe ser mayor a 10.</span><br>\n'
            self.errors += 1
        else:
            self.grp = grp
    #GET
    def getUser(self):
        return self.user

    def getPassword(self):
        return self.password

    def getGrp(self):
        return self.grp
    