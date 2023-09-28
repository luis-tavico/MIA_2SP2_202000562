class Mkgrp:
    def __init__(self, name = ""):
        self.name = name
        self.errors = 0

    #SET
    def setName(self, name):
        self.name = name 

    #GET
    def getName(self):
        return self.name