import re

er = r'(\"(\/(\w|\s)+)+\.adsj\")|((\/\w+)+\.adsj)'
ruta = '"/home/user/Escritorio/mis rutas/prueba.adsj"'


def t_RUTA_ARCHIVO(t):
    r'(\"(\/(\w|\s|-)+)+\.[a-zA-Z]+\")|((\/(\w|-)+)+\.[a-zA-Z]+)'
    return t

match = re.search(er, ruta)
print(len(ruta))
print(match)