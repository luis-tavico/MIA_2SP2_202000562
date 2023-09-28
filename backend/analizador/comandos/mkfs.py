
class Mkfs:
    def __init__(self, id = "", type = "full"):
        self.id = id
        self.type = type
        self.errors = 0

    #SET
    def setId(self, id):
        self.id = id

    def setType(self, type):
        self.type = type

    #GET
    def getId(self):
        return self.id

    def getType(self):
        return self.type