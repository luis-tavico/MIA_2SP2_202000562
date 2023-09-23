#crear un arhivo vacio
with open('archivo.bin', 'wb') as archivo:
    for i in range(0, 1):
        archivo.write(b'\x00' * 1024)

''' '''
#agregar cont a archivo
with open('archivo.bin', 'rb+') as archivo:
    archivo.seek(5)
    archivo.write(b'1, G, root\n1, U, root, root, 123\n$')

#buscar en archivo
pos = 0
encontrado = False
with open('archivo.bin', 'rb') as archivo:
    archivo.seek(5)
    while True:
        byte = archivo.read(1)
        if not byte:
            break
        if byte == b'$':
            encontrado = True
            break
        pos += 1

with open('archivo.bin', 'rb+') as archivo:
    archivo.seek(5)
    contenido = archivo.read(pos)
print(contenido)

if encontrado:
    print(f"El caracter $ se encontró en pos {str(pos)} del archivo.")
else:
    print(f"El caracter $ no se encontró en el archivo.")
