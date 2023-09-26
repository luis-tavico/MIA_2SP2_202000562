import re

er = r'(\"(\/(\w|\s)+)+\.adsj\")|((\/\w+)+\.adsj)'
ruta = '"/home/user/Escritorio/mis rutas/prueba.adsj"'

match = re.search(er, ruta)
print(match)