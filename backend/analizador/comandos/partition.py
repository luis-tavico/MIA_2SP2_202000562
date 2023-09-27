import struct

class Partition:
    def __init__(self, part_status = "0", part_type = "P", part_fit = "W", part_start = 0, part_s = 0, part_name = ""):
        self.part_status = part_status
        self.part_type = part_type
        self.part_fit = part_fit
        self.part_start = part_start
        self.part_s = part_s
        self.part_name = part_name

    #SET
    def setPart_status(self, part_status):
        self.part_status = part_status

    def setPart_type(self, part_type):
        self.part_type = part_type

    def setPart_fit(self, part_fit):
        self.part_fit = part_fit

    def setPart_start(self, part_start):
        self.part_start = part_start

    def setPart_s(self, part_s):
        self.part_s = part_s

    def setPart_name(self, part_name):
        self.part_name = part_name

    #GET
    def getPart_status(self):
        return self.part_status

    def getPart_type(self):
        return self.part_type

    def getPart_fit(self):
        return self.part_fit

    def getPart_start(self):
        return self.part_start

    def getPart_s(self):
        return self.part_s

    def getPart_name(self):
        return self.part_name
    
    #Empaquetar_Desempaquetar
    def pack_data(self):
        return struct.pack('cccii16s', self.part_status.encode(), self.part_type.encode(), self.part_fit.encode(), self.part_start, self.part_s, self.part_name.encode('utf-8'))

    @classmethod
    def unpack_data(cls, data_bytes):
        part_status, part_type, part_fit, part_start, part_s, part_name = struct.unpack('cccii16s', data_bytes)
        return cls(part_status.decode(), part_type.decode(), part_fit.decode(), part_start, part_s, part_name.decode('utf-8'))
    
    def getLength(self):
        return struct.calcsize('cccii16s')
        #devuelve 28

'''
part = Partition("I", "P", "W", 1500, 3000, "particion1")
pack = part.pack_data()
print(pack)
unpack = part.unpack_data(pack)
print(unpack)
print(unpack.getPart_name())
print(part.getLength())
'''