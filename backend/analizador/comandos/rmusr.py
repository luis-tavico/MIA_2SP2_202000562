class Rmusr:
    def __init__(self, user = ""):
        self.user = user
        self.errors = 0

    #SET
    def setUser(self, user):
        self.user = user 

    #GET
    def getUser(self):
        return self.user