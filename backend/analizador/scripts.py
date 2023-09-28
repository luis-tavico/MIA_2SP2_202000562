import os
import math
import random
import re
from datetime import datetime
import subprocess
from analizador.comandos.ebr import Ebr
from analizador.comandos.execute import Execute
from analizador.comandos.fdisk import Fdisk
from analizador.comandos.inodo import Inodo
from analizador.comandos.login import Login
from analizador.comandos.mbr import Mbr
from analizador.comandos.mkdir import Mkdir
from analizador.comandos.mkdisk import Mkdisk
from analizador.comandos.mkfile import Mkfile
from analizador.comandos.mkfs import Mkfs
from analizador.comandos.mkgrp import Mkgrp
from analizador.comandos.mkusr import Mkusr
from analizador.comandos.mount import Mount
from analizador.comandos.partition import Partition
from analizador.comandos.rep import Rep
from analizador.comandos.rmdisk import Rmdisk
from analizador.comandos.rmgrp import Rmgrp
from analizador.comandos.rmusr import Rmusr
from analizador.comandos.superBloque import SuperBloque
from analizador.comandos.unmount import Unmount

global comando, script, particiones_montadas, usuario_actual, info, mensajes
particiones_montadas = {}
usuario_actual = ""
info = []
mensajes = ""

def comando_activar(valor):
    global comando, script, mensajes
    comando = valor

    #comandos de discos
    if (comando.lower() == "mkdisk"):
        script = Mkdisk()
        mensajes += '<span class="text-info">Ejecutando comando mkdisk...</span><br>\n'
    elif (comando.lower() == "rmdisk"):
        script = Rmdisk()
        mensajes += '<span class="text-info">Ejecutando comando rmdisk...</span><br>\n'
    elif (comando.lower() == "fdisk"):
        script = Fdisk()
        mensajes += '<span class="text-info">Ejecutando comando fdisk...</span><br>\n'
    elif (comando.lower() == "mount"):
        script = Mount()
        mensajes += '<span class="text-info">Ejecutando comando mount...</span><br>\n'
    elif (comando.lower() == "unmount"):
        script = Unmount()
        mensajes += '<span class="text-info">Ejecutando comando unmount...</span><br>\n'
    elif (comando.lower() == "mkfs"):
        script = Mkfs()
        mensajes += '<span class="text-info">Ejecutando comando mkfs...</span><br>\n'
    #comandos de usuarios y grupos
    elif (comando.lower() == "login"):
        script = Login()
        mensajes += '<span class="text-info">Ejecutando comando login...</span><br>\n'
    elif (comando.lower() == "logout"):
        mensajes += '<span class="text-info">Ejecutando comando logout...</span><br>\n'
    elif (comando.lower() == "mkgrp"):
        script = Mkgrp()
        mensajes += '<span class="text-info">Ejecutando comando mkgrp...</span><br>\n'
    elif (comando.lower() == "rmgrp"):
        script = Rmgrp()
        mensajes += '<span class="text-info">Ejecutando comando rmgrp...</span><br>\n'
    elif (comando.lower() == "mkusr"):
        script = Mkusr()
        mensajes += '<span class="text-info">Ejecutando comando mkusr...</span><br>\n'
    elif (comando.lower() == "rmusr"):
        script = Rmusr()
        mensajes += '<span class="text-info">Ejecutando comando rmusr...</span><br>\n'
    #comandos de archivos y permisos
    elif (comando.lower() == "mkfile"):
        script = Mkfile()
        mensajes += '<span class="text-info">Ejecutando comando mkfile...</span><br>\n'
    elif (comando.lower() == "mkdir"):
        script = Mkdir()
        mensajes += '<span class="text-info">Ejecutando comando mkdir...</span><br>\n'
    elif (comando.lower() == "execute"):
        script = Execute()
        mensajes += '<span class="text-info">Ejecutando comando execute...</span><br>\n'
    elif (comando.lower() == "rep"):
        script = Rep()
        mensajes += '<span class="text-info">Ejecutando comando rep...</span><br>\n'

def comando_ejecutar(parametro, valor):
    global comando, script, particiones_montadas, usuario_actual, info, mensajes
    #COMANDO MKDISK
    if (comando.lower() == "mkdisk"):
        if (parametro.lower() == 'size'):
            mensajes += '<span class="text-white">leyendo tamaño del disco...</span><br>\n'
            script.setSize(int(valor))
        elif (parametro.lower() == 'path'):
            mensajes += '<span class="text-white">leyendo ruta del disco...</span><br>\n'
            script.setPath(valor)
        elif (parametro.lower() == 'fit'):
            mensajes += '<span class="text-white">leyendo ajuste del disco...</span><br>\n'
            script.setFit(valor)
        elif (parametro.lower() == 'unit'):
            mensajes += '<span class="text-white">leyendo unidad del disco...</span><br>\n'
            script.setUnit(valor)
        elif (parametro.lower() == "ejecutar"):
            mensajes += script.mensajes
            if (script.errors == 0):
                #crear un arhivo vacio
                tamano_archivo = script.getSize()
                if (script.getUnit().lower() == "m"):
                    tamano_archivo = tamano_archivo * 1024
                with open(script.getPath(), 'wb') as archivo:
                    for i in range(0, tamano_archivo):
                        archivo.write(b'\x00' * 1024)
                #crear mbr
                mbr = Mbr()
                if (script.getUnit().lower() == "m"):
                    mbr.setTamano(script.getSize()*1024*1024)
                elif (script.getUnit().lower() == "k"):
                    mbr.setTamano(script.getSize()*1024)
                mbr.setFecha_creacion(datetime.now())
                mbr.setDsk_signature(generarCodigo())
                mbr.setFit(script.getFit()[0])
                #escribir mbr
                with open(script.getPath(), 'rb+') as archivo:
                    archivo.write(mbr.pack_data())
                #escribir particiones
                pos = mbr.getLength()
                for particion in mbr.getPartitions():
                    with open(script.getPath(), 'rb+') as archivo:
                        archivo.seek(pos)
                        archivo.write(particion.pack_data())
                    pos += particion.getLength()
                mensajes += '<span class="text-success"><i class="fa-solid fa-check"></i> Disco creado exitosamente.</span><br>\n'
                mensajes += '<span class="text-info">...Comando mkdisk ejecutado</span><br>\n'
            else: 
                mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> No se pudo crear el disco.</span><br>\n'
        else:
            script.errors += 1
            mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Parametro no valido.</span><br>\n'
        return None
    #COMANDO RMDISK
    elif (comando.lower() == "rmdisk"):
        if (parametro.lower() == 'path'):
            mensajes += '<span class="text-white">leyendo ruta del disco...</span><br>\n'
            script.setPath(valor)
        elif (parametro.lower() == 'ejecutar'):
            mensajes += script.mensajes
            if (script.errors == 0):
                os.remove(script.getPath())
                mensajes += '<span class="text-success"><i class="fa-solid fa-check"></i> Disco eliminado exitosamente.</span><br>\n'
                mensajes += '<span class="text-info">...Comando rmdisk ejecutado</span><br>\n'
            else:
                mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> No se pudo eliminar el disco.</span><br>\n'
        else:
            script.errors += 1
            mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Parametro no valido.</span><br>\n'
        return None
    #COMANDO FDISK
    elif (comando.lower() == 'fdisk'):
        if (parametro.lower() == 'size'):
            mensajes += '<span class="text-white">leyendo tamaño de la particion...</span><br>\n'
            script.setSize(int(valor))
        elif (parametro.lower() == 'path'):
            mensajes += '<span class="text-white">leyendo ruta del disco...</span><br>\n'
            script.setPath(valor)
        elif (parametro.lower() == 'name'):
            mensajes += '<span class="text-white">leyendo nombre de la particion...</span><br>\n'
            script.setName(valor)
        elif (parametro.lower() == 'unit'):
            mensajes += '<span class="text-white">leyendo unidad de la particion...</span><br>\n'
            script.setUnit(valor)
        elif(parametro.lower() == 'type'):
            mensajes += '<span class="text-white">leyendo tipo de la particion...</span><br>\n'
            script.setType(valor)
        elif(parametro.lower() == 'fit'):
            mensajes += '<span class="text-white">leyendo ajuste de la particion...</span><br>\n'
            script.setFit(valor)
        elif (parametro.lower() == 'ejecutar'):
            mensajes += script.mensajes
            if (script.errors == 0):
                #obtener mbr
                mbr = Mbr()
                with open(script.getPath(), 'rb+') as archivo:
                    archivo.seek(0)
                    contenido = archivo.read(mbr.getLength())
                mbr = mbr.unpack_data(contenido)
                #obtener particiones
                pos = mbr.getLength()
                for i in range(4):
                    particion = Partition()
                    with open(script.getPath(), 'rb+') as archivo:
                        archivo.seek(pos)
                        contenido = archivo.read(particion.getLength())
                    particion = particion.unpack_data(contenido)
                    mbr.getPartitions()[i] = particion
                    pos += particion.getLength()
                #verificar si nombre existe
                for partition in mbr.getPartitions():
                    if (partition.getPart_name().rstrip("\x00") == script.getName()):
                        mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> El valor del parametro "name" ya existe.</span><br>\n'
                        mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> No se pudo crear la particion.</span><br>\n'
                        return None
                #verificar tipo de particion
                if (script.getType().lower() == "e"):
                    for partition in mbr.getPartitions():
                        if (partition.getPart_type().lower() == "e"):
                            mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Ya existe una particion extendida.</span><br>\n'
                            mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> No se pudo crear la particion.</span><br>\n'
                            return None
                elif (script.getType().lower() == "l"):
                    extendida_existe = False
                    for partition in mbr.getPartitions():
                        if (partition.getPart_type().lower() == "e"):
                            extendida_existe = True
                            break
                    if not(extendida_existe):
                        mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> No existe una particion extendida.</span><br>\n'
                        mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> No se pudo crear la particion.</span><br>\n'
                        return None
                #convertir tamaño a bytes
                size = 0
                if (script.unit.lower() == "m"):
                    size = script.getSize()*1024*1024
                elif (script.unit.lower() == "k"):
                    size = script.getSize()*1024
                else:
                    size = script.getSize()
                #Buscar lugar para la particion
                pos_particion = None
                if (script.getType().lower() == "p" or script.getType().lower() == "e"):
                    temp = 0
                    pos_en_disco = 21 + 4 * 28
                    if (mbr.getFit().lower() == 'bf'):
                        diferencia_minima = float('inf')
                        for i, partition in enumerate(mbr.getPartitions()):
                            if (partition.getPart_status == "0"):
                                diferencia = partition.getPart_s() - size
                                if diferencia >= 0 and diferencia < diferencia_minima:
                                    pos_particion = i
                                    diferencia_minima = diferencia
                            else:
                                pos_en_disco += partition.getPart_s()
                    elif (mbr.getFit().lower() == 'ff'):
                        for i, partition in enumerate(mbr.getPartitions()):
                            if (partition.getPart_status() == "0"):
                                if partition.getPart_s() >= size:
                                    pos_particion = i
                            else:
                                pos_en_disco += partition.getPart_s()
                    elif (mbr.getFit().lower() == 'wf'):
                        for i, partition in enumerate(mbr.getPartitions()):
                            if (partition.getPart_status() == "0"):
                                if (partition.getPart_s() >= size and partition.getPart_s() >= temp):
                                    pos_particion = i
                                    temp = partition.getPart_s()
                            else:
                                pos_en_disco += partition.getPart_s()
                    #Si no se creo la particon, buscar de nuevo lugar
                    if (pos_particion == None):
                        for i, partition in enumerate(mbr.getPartitions()):
                            if (partition.getPart_status() == "0"):
                                if (partition.getPart_s() == 0):
                                    pos_particion = i
                                    break                           
                            else:
                                pos_en_disco += partition.getPart_s()
                elif (script.getType().lower() == "l"):
                    particion_extendida = None
                    for partition in mbr.getPartitions():
                        if (partition.getPart_type().lower() == "e"):
                            particion_extendida = partition
                            break
                    inicio = particion_extendida.getPart_start()
                    #obtener ebr
                    ebr = Ebr()
                    with open(script.getPath(), 'rb+') as archivo:
                        archivo.seek(inicio)
                        contenido = archivo.read(ebr.getLength())
                    ebr = ebr.unpack_data(contenido)
                    if (ebr.getPart_s() == 0):
                        if (particion_extendida.getPart_s() > (ebr.getLength() + size)):
                            ebr.setPart_status("1")
                            ebr.setPart_fit(script.getFit()[0])
                            ebr.setPart_start(inicio+ebr.getLength())
                            ebr.setPart_s(size)
                            ebr.setPart_next(-1)
                            ebr.setPart_name(script.getName())
                            #escribir ebr
                            with open(script.getPath(), 'rb+') as archivo:
                                archivo.seek(inicio)
                                archivo.write(ebr.pack_data())
                            mensajes += '<span class="text-success"><i class="fa-solid fa-check"></i> Particion creada exitosamente.</span><br>\n'
                            mensajes += '<span class="text-info">...Comando fdisk ejecutado</span><br>\n'
                            return None
                        else:
                            mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Espacio insuficiente en disco.</span><br>\n'
                            mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> No se pudo crear la particion.</span><br>\n'
                            return None
                    else:
                        puntero = inicio
                        tam_disp = particion_extendida.getPart_s() - (ebr.getLength() + ebr.getPart_s())
                        while True:
                            if (ebr.getPart_name().rstrip("\x00") == script.getName()):                              
                                mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> El valor del parametro "name" ya existe.</span><br>\n'
                                mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> No se pudo crear la particion.</span><br>\n'
                                return None
                            if (ebr.getPart_next() == -1):
                                if (tam_disp > (size + 32)):
                                    ebr.setPart_next(ebr.getPart_start() + ebr.getPart_s())
                                    #escribir ebr
                                    with open(script.getPath(), 'rb+') as archivo:
                                        archivo.seek(puntero)
                                        archivo.write(ebr.pack_data())
                                    puntero += ebr.getLength() + ebr.getPart_s()   
                                    ebr = Ebr()
                                    ebr.setPart_status("1")
                                    ebr.setPart_fit(script.getFit()[0])
                                    ebr.setPart_start(puntero+ebr.getLength())
                                    ebr.setPart_s(size)
                                    ebr.setPart_next(-1)
                                    ebr.setPart_name(script.getName())
                                    #escribir ebr
                                    with open(script.getPath(), 'rb+') as archivo:
                                        archivo.seek(puntero)
                                        archivo.write(ebr.pack_data())
                                    mensajes += '<span class="text-success"><i class="fa-solid fa-check"></i> Particion creada exitosamente.</span><br>\n'
                                    mensajes += '<span class="text-info">...Comando fdisk ejecutado</span><br>\n'
                                    return None
                                else:
                                    mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Espacio insuficiente en disco.</span><br>\n'
                                    mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> No se pudo crear la particion.</span><br>\n'
                                    return None
                            else:
                                puntero += ebr.getLength() + ebr.getPart_s() 
                                #obtener siguiente ebr
                                ebr = Ebr()
                                with open(script.getPath(), 'rb+') as archivo:
                                    archivo.seek(puntero)
                                    contenido = archivo.read(ebr.getLength())
                                ebr = ebr.unpack_data(contenido)
                                tam_disp -= (ebr.getLength() + ebr.getPart_s())
                #Crear particion primaria o extendida
                if (pos_particion != None):
                    tam_usado = 133
                    for particion in mbr.getPartitions():
                        tam_usado += particion.getPart_s()
                    tam_disp = mbr.getTamano() - tam_usado
                    mbr.getPartitions()[pos_particion].setPart_status("1")
                    mbr.getPartitions()[pos_particion].setPart_type(script.getType())
                    mbr.getPartitions()[pos_particion].setPart_fit(script.getFit()[0])
                    mbr.getPartitions()[pos_particion].setPart_start(pos_en_disco)
                    if (size > tam_disp):
                        mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Espacio insuficiente en disco.</span><br>\n'
                        mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> No se pudo crear la particion.</span><br>\n'
                        return None
                    mbr.getPartitions()[pos_particion].setPart_s(size)     
                    mbr.getPartitions()[pos_particion].setPart_name(script.getName())
                    #escribir mbr
                    with open(script.getPath(), 'rb+') as archivo:
                        archivo.write(mbr.pack_data())
                    #escribir particiones
                    pos = mbr.getLength()
                    for particion in mbr.getPartitions():
                        with open(script.getPath(), 'rb+') as archivo:
                            archivo.seek(pos)
                            archivo.write(particion.pack_data())
                        pos += particion.getLength()
                    if (script.getType().lower() == "e"):
                        ebr = Ebr()
                        #escribir ebr
                        with open(script.getPath(), 'rb+') as archivo:
                            archivo.seek(pos_en_disco)
                            archivo.write(ebr.pack_data())
                    mensajes += '<span class="text-success"><i class="fa-solid fa-check"></i> Particion creada exitosamente.</span><br>\n'
                    mensajes += '<span class="text-info">...Comando fdisk ejecutado</span><br>\n'
                    return None
                else:
                    script.errors += 1
                    mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Las 4 particiones permitidas, ya han sido usadas.</span><br>\n'
                    mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> No se pudo crear la particion.</span><br>\n'
                    return None
            if (script.errors != 0):
                mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> No se pudo crear la particion.</span><br>\n'
        else:
            mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Parametro no valido.</span><br>\n'
        return None
    #cOMANDO MOUNT
    elif (comando.lower() == 'mount'):
        if (parametro.lower() == 'path'):
            mensajes += '<span class="text-white">leyendo ruta del disco...</span><br>\n'
            script.setPath(valor)
        elif (parametro.lower() == 'name'):
            mensajes += '<span class="text-white">leyendo nombre de la particion...</span><br>\n'
            script.setName(valor)
        elif (parametro.lower() == 'ejecutar'):
            mensajes += script.mensajes
            if (script.errors == 0):
                #obtener mbr
                mbr = Mbr()
                with open(script.getPath(), 'rb+') as archivo:
                    archivo.seek(0)
                    contenido = archivo.read(mbr.getLength())
                mbr = mbr.unpack_data(contenido)
                #obtener particiones
                pos = mbr.getLength()
                for i in range(4):
                    particion = Partition()
                    with open(script.getPath(), 'rb+') as archivo:
                        archivo.seek(pos)
                        contenido = archivo.read(particion.getLength())
                    particion = particion.unpack_data(contenido)
                    mbr.getPartitions()[i] = particion
                    pos += particion.getLength()
                #buscar particion
                num_particion = ""
                for i, partition in enumerate(mbr.getPartitions()):
                    if (partition.getPart_type().lower() == "p" and partition.getPart_status() == "1"):
                        if (partition.getPart_name().rstrip("\x00") == script.getName()):
                            numeros = re.findall(r'\d+', script.getName())
                            for numero in numeros: 
                                num_particion += numero
                            break
                    elif (partition.getPart_type().lower() == "e" and partition.getPart_status() == "1"):
                        if (partition.getPart_name().rstrip("\x00") == script.getName()):
                            numeros = re.findall(r'\d+', script.getName())
                            for numero in numeros: 
                                num_particion += numero
                            break
                        else:
                            puntero = partition.getPart_start()
                            #obtener ebr
                            ebr = Ebr()
                            with open(script.getPath(), 'rb+') as archivo:
                                archivo.seek(puntero)
                                contenido = archivo.read(ebr.getLength())
                            ebr = ebr.unpack_data(contenido)
                            while True:
                                if (ebr.getPart_name().rstrip("\x00") == script.getName()):
                                    numeros = re.findall(r'\d+', script.getName())
                                    for numero in numeros: 
                                        num_particion += numero
                                    break
                                if (ebr.getPart_next() == -1):
                                    break
                                else:
                                    puntero = ebr.getPart_next()
                                    #obtener ebr
                                    ebr = Ebr()
                                    with open(script.getPath(), 'rb+') as archivo:
                                        archivo.seek(puntero)
                                        contenido = archivo.read(ebr.getLength())
                                    ebr = ebr.unpack_data(contenido)

                if (num_particion == ""):
                    script.errors += 1
                    mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> La particion no existe.</span><br>\n'
                else:
                    id = "62" + num_particion + os.path.splitext(os.path.basename(script.getPath()))[0]
                    if not(id in particiones_montadas):   
                        #particiones_montadas[id] = script.getPath()
                        particiones_montadas[id] = [script.getName(), script.getPath()]
                        mensajes += '<span class="text-white">Particiones montadas:</span><br>\n'
                        for clave, valor in particiones_montadas.items():
                            mensajes += '<span class="text-white">' + clave[1] + '</span><br>\n'
                        mensajes += '<span class="text-success"><i class="fa-solid fa-check"></i> Particion montada exitosamente.</span><br>\n'
                        mensajes += '<span class="text-info">...Comando mount ejecutado</span><br>\n'
                    else:
                        script.errors += 1
                        mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> La particion ya esta montada.</span><br>\n'
            if (script.errors != 0):
                mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> No se pudo montar la particion.</span><br>\n'
        else:
            mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Parametro no valido.</span><br>\n'
        return None
    #COMANDO UNMOUNT
    elif (comando.lower() == 'unmount'):
        if (parametro.lower() == 'id'):
            print("leyendo id de la particion...")
            script.setId(valor)
        elif (parametro.lower() == 'ejecutar'):
            if script.getId() in particiones_montadas:   
                particiones_montadas.pop(script.getId())
                print("\033[1;32m<<Success>> {}\033[00m" .format("Particion desmontada exitosamente."))
                mensajes += '<span class="text-info">...Comando unmount ejecutado</span><br>\n'
            else:
                print("\033[91m<<Error>> {}\033[00m" .format("La particion no esta montada."))
                print("\033[91m<<Error>> {}\033[00m" .format("No se pudo desmontar la particion."))
        else:
            print("\033[91m<<Error>> {}\033[00m" .format("Parametro no valido."))
        return None
    #COMANDO MKFS
    elif (comando.lower() == 'mkfs'):
        if (parametro.lower() == 'id'):
            print("leyendo id de la particion...")
            script.setId(valor)
        elif (parametro.lower() == 'type'):
            print("leyendo tipo de formateo...")
            script.setType(valor)
        elif (parametro.lower() == 'ejecutar'):
            #buscar particion o disco
            if script.getId() in particiones_montadas:
                name_part = particiones_montadas[script.getId()][0]
                path = particiones_montadas[script.getId()][1]
                if not(os.path.exists(path)):
                    return None
                #obtener mbr
                mbr = Mbr()
                with open(path, 'rb+') as archivo:
                    archivo.seek(0)
                    contenido = archivo.read(mbr.getLength())
                mbr = mbr.unpack_data(contenido)
                #obtener particiones
                pos = mbr.getLength()
                for i in range(4):
                    particion = Partition()
                    with open(path, 'rb+') as archivo:
                        archivo.seek(pos)
                        contenido = archivo.read(particion.getLength())
                    particion = particion.unpack_data(contenido)
                    mbr.getPartitions()[i] = particion
                    pos += particion.getLength()
                #buscar particion
                part_formatear = None
                for i, partition in enumerate(mbr.getPartitions()):
                    if (partition.getPart_type().lower() == "p" and partition.getPart_status() == "1"):
                        if (partition.getPart_name().rstrip("\x00") == name_part):
                            part_formatear = partition
                            break
                    elif (partition.getPart_type().lower() == "e" and partition.getPart_status() == "1"):
                        if (partition.getPart_name().rstrip("\x00") == name_part):
                            part_formatear = partition
                            break
                        else:
                            puntero = partition.getPart_start()
                            #obtener ebr
                            ebr = Ebr()
                            with open(script.getPath(), 'rb+') as archivo:
                                archivo.seek(puntero)
                                contenido = archivo.read(ebr.getLength())
                            ebr = ebr.unpack_data(contenido)
                            while True:
                                if (ebr.getPart_name().rstrip("\x00") == script.getName()):
                                    part_formatear = partition
                                    break
                                if (ebr.getPart_next() == -1):
                                    break
                                else:
                                    puntero = ebr.getPart_next()
                                    #obtener ebr
                                    ebr = Ebr()
                                    with open(script.getPath(), 'rb+') as archivo:
                                        archivo.seek(puntero)
                                        contenido = archivo.read(ebr.getLength())
                                    ebr = ebr.unpack_data(contenido)
                #calculos
                super_bloque = SuperBloque()
                #archivo_bloque = ArchivoBloque()
                inodo = Inodo()
                numerator = part_formatear.getPart_s() - super_bloque.getLength()
                denominator = 4 + inodo.getLength() + 3 * 64
                n = math.floor(numerator / denominator)
                print(n)
                #Escribir contenido en el archivo binario
                '''
                with open('users.txt', 'wb') as archivo:
                    archivo.write(b'1, G, root\n')
                    archivo.write(b'1, U, root, root, 123\n')
                '''
                #Escribir archivo users.txt en particion
                with open(path, 'rb+') as archivo:
                    archivo.seek(part_formatear.getPart_start())
                    contenido = ('1, G, root\n1, U, root, root, 123$').encode('utf-8')
                    archivo.write(contenido)
                print("Particion formateada exitosamente")
                return None
                #####
            else:
                print("\033[91m<<Error>> {}\033[00m" .format("La particion no existe."))
                print("\033[91m<<Error>> {}\033[00m" .format("No se pudo formatear la particion."))
        else:
            print("\033[91m<<Error>> {}\033[00m" .format("Parametro no valido."))
        return None
    #COMANDO LOGIN
    elif (comando.lower() == 'login'):
        if (parametro.lower() == 'user'):
            script.setUser(valor)
        elif (parametro.lower() == 'pass'):
            script.setPassword(valor)
        elif (parametro.lower() == 'id'):
            script.setId(valor)
        elif(parametro.lower() == 'ejecutar'):
            usuario_existe = False
            contraseña_correcta = False
            if (usuario_actual == ""):
                #buscar particion en particiones montadas
                if script.getId() in particiones_montadas:
                    name_part = particiones_montadas[script.getId()][0]
                    path = particiones_montadas[script.getId()][1]
                    if not(os.path.exists(path)):
                        print("¡el disco no existe!")
                        return None
                    #obtener mbr
                    mbr = Mbr()
                    with open(path, 'rb+') as archivo:
                        archivo.seek(0)
                        contenido = archivo.read(mbr.getLength())
                    mbr = mbr.unpack_data(contenido)
                    #obtener particiones
                    pos = mbr.getLength()
                    for i in range(4):
                        particion = Partition()
                        with open(path, 'rb+') as archivo:
                            archivo.seek(pos)
                            contenido = archivo.read(particion.getLength())
                        particion = particion.unpack_data(contenido)
                        mbr.getPartitions()[i] = particion
                        pos += particion.getLength()
                    #buscar particion
                    part_formateada = None
                    for i, partition in enumerate(mbr.getPartitions()):
                        if (partition.getPart_type().lower() == "p" and partition.getPart_status() == "1"):
                            if (partition.getPart_name().rstrip("\x00") == name_part):
                                part_formateada = partition
                                break
                        elif (partition.getPart_type().lower() == "e" and partition.getPart_status() == "1"):
                            if (partition.getPart_name().rstrip("\x00") == name_part):
                                part_formateada = partition
                                break
                            else:
                                puntero = partition.getPart_start()
                                #obtener ebr
                                ebr = Ebr()
                                with open(path, 'rb+') as archivo:
                                    archivo.seek(puntero)
                                    contenido = archivo.read(ebr.getLength())
                                ebr = ebr.unpack_data(contenido)
                                while True:
                                    if (ebr.getPart_name().rstrip("\x00") == script.getName()):
                                        part_formateada = partition
                                        break
                                    if (ebr.getPart_next() == -1):
                                        break
                                    else:
                                        puntero = ebr.getPart_next()
                                        #obtener ebr
                                        ebr = Ebr()
                                        with open(path, 'rb+') as archivo:
                                            archivo.seek(puntero)
                                            contenido = archivo.read(ebr.getLength())
                                        ebr = ebr.unpack_data(contenido)
                    #obtener inicio de archivos users.txt
                    if part_formateada == None:
                        print("No se encontro la particion")
                        return None
                    ini_archivo = part_formateada.getPart_start()
                    #verificar si esta formateada la particion
                    with open(path, 'rb+') as archivo:
                        archivo.seek(ini_archivo)
                        byte = archivo.read(1)
                        if byte == b'\x00':
                            print(f"La particion {part_formateada.getPart_name()} no esta formateada")
                            return None
                    #obtener longitud de archivo users.txt
                    pos = 0
                    with open(path, 'rb+') as archivo:
                        archivo.seek(ini_archivo)
                        while True:
                            byte = archivo.read(1)
                            if not byte:
                                break
                            if byte == b'$':
                                break
                            pos += 1
                    #obtener contenido de archivo users.txt
                    with open(path, 'rb+') as archivo:
                        archivo.seek(ini_archivo)
                        contenido = archivo.read(pos)
                    contenido = contenido.decode('utf-8')
                    lineas = contenido.splitlines()
                    #info = [ruta_disco, posicion_particion, contenido]
                    info.append(path)
                    info.append(ini_archivo)
                    info.append(contenido)
                    #verificar si existe usuario
                    for linea in lineas:
                        usuario_grupo = linea.strip().split(", ")
                        if (usuario_grupo[1] == "U"):
                            if (script.getUser() in usuario_grupo):
                                usuario_existe = True
                                if (script.getPassword() in usuario_grupo):
                                    contraseña_correcta = True
                                break
                    if (usuario_existe):
                        if (contraseña_correcta):
                            print(f"¡Bienvenido {script.getUser()}!")
                            usuario_actual = script.getUser()
                        else:
                            print("¡Contraseña incorrecta!")
                    else:
                        print("¡Usuario no existe!")
                else:
                    print("la particion no esta montada.")

            else:
                print("Ya hay una sesion activa")
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO LOGOUT
    elif (comando.lower() == 'logout'):
        if (parametro.lower() == 'ejecutar'):
            if (usuario_actual != ""):
                usuario_actual = ""
                info.clear()
                print("¡Sesion cerrada!")
            else:
                print("¡Error! no existe una sesion activa.")
        return None
    #COMANDO MKGRP
    elif (comando.lower() == 'mkgrp'):
        if (parametro.lower() == 'name'):
            script.setName(valor)
        elif (parametro.lower() == 'ejecutar'):
            if (usuario_actual == "root"):
                num = 1
                grupo_existe = False
                #leer archivo users.txt
                #info = [ruta_disco, posicion_particion, contenido]
                contenido = info[2]
                lineas = contenido.splitlines()
                for linea in lineas:
                    usuario_grupo = linea.strip().split(", ")
                    if (usuario_grupo[1] == "G"):
                        if (script.getName() in usuario_grupo):
                            grupo_existe = True
                            break
                        else:
                            num += 1
                if (not grupo_existe):
                    #editar archivo users.txt
                    info[2] = contenido + "\n" + str(num) + ", G, " + script.getName()
                    #Escribir en archivo users.txt
                    with open(info[0], 'rb+') as archivo:
                        archivo.seek(info[1])
                        archivo.write((info[2]+"$").encode('utf-8'))                   
                    print("¡Grupo creado exitosamente!")
                else:
                    print("¡Error! el grupo a crear ya existe.")
            elif (usuario_actual == ""):
                print("¡Error! ningun usuario ha iniciado sesion.")
            else:
                print("¡Error! solo el usuario 'root' tiene permiso de crear grupos.")
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO RMGRP
    elif (comando.lower() == 'rmgrp'):
        if (parametro.lower() == 'name'):
            script.setName(valor)
        elif (parametro.lower() == 'ejecutar'):
            if (usuario_actual == "root"):
                cont_editado = ""
                grupo_existe = False
                pos = None
                #leer archivo users.txt
                #info = [ruta_disco, posicion_particion, contenido]
                contenido = info[2]
                lineas = contenido.splitlines()
                for i, linea in enumerate(lineas):
                    usuario_grupo = linea.strip().split(", ")
                    if (usuario_grupo[1] == "G"):
                        if (script.getName() in usuario_grupo):
                            cont_editado = "0, " + usuario_grupo[1] + ", " + usuario_grupo[2]
                            grupo_existe = True
                            pos = i
                            break
                if (grupo_existe):
                    lineas[pos] = cont_editado
                    info[2] = "\n".join(lineas)
                    #Escribir en archivo users.txt
                    with open(info[0], 'rb+') as archivo:
                        archivo.seek(info[1])
                        archivo.write((info[2]+"$").encode('utf-8'))
                    print("¡Grupo eliminado exitosamente!")               
                else:
                    print("¡Error! el grupo a eliminar no existe")
            elif (usuario_actual == ""):
                print("¡Error! ningun usuario ha iniciado sesion.")
            else:
                print("¡Error! solo el usuario 'root' tiene permiso de eliminar grupos.")
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMAND MKUSR
    elif (comando.lower() == 'mkusr'):
        if (parametro.lower() == 'user'):
            script.setUser(valor)
        elif (parametro.lower() == 'pass'):
            script.setPassword(valor)
        elif (parametro.lower() == 'grp'):
            script.setGrp(valor)
        elif (parametro.lower() == 'ejecutar'):
            if (usuario_actual == 'root'):
                if (script.errors == 0):
                    usuario_existe = False
                    grupo_existe = False
                    pos = None
                    #leer archivo users.txt
                    #info = [ruta_disco, posicion_particion, contenido]
                    contenido = info[2]
                    lineas = contenido.splitlines()
                    for i, linea in enumerate(lineas):
                        usuario_grupo = linea.strip().split(", ")
                        if (usuario_grupo[1] == "U"):
                            if (script.getUser() in usuario_grupo):
                                usuario_existe = True
                        elif (usuario_grupo[1] == "G"):
                            if (script.getGrp() == usuario_grupo[2]):
                                grupo_existe = True
                                pos = usuario_grupo[0]
                    if (grupo_existe):
                        if not usuario_existe:
                            #editar archivo users.txt
                            info[2] = contenido + "\n" + pos + ", U, " + script.getGrp() + ", " + script.getUser() + ", " + script.getPassword()
                            #Escribir en archivo users.txt
                            with open(info[0], 'rb+') as archivo:
                                archivo.seek(info[1])
                                archivo.write((info[2]+"$").encode('utf-8'))                   
                            print("¡Usuario creado exitosamente!")
                        else:
                            print("¡Error! el usuario a crear ya existe.")
                    else:
                        print("¡Error! el grupo no existe.")
                else:
                    print('¡Error! no se pudo crear el usuario.')
            elif (usuario_actual == ""):
                print("¡Error! ningun usuario ha iniciado sesion.")
            else:
                print("¡Error! solo el usuario 'root' tiene permiso de crear usuarios.")
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO RMUSR
    elif (comando.lower() == 'rmusr'):
        if (parametro.lower() == 'user'):
            script.setUser(valor)
        elif (parametro.lower() == 'ejecutar'):
            if (usuario_actual == "root"):
                cont_editado = ""
                usuario_existe = False
                pos = None
                #leer archivo users.txt
                #info = [ruta_disco, posicion_particion, contenido]
                contenido = info[2]
                lineas = contenido.splitlines()
                for i, linea in enumerate(lineas):
                    usuario_grupo = linea.strip().split(", ")
                    if (usuario_grupo[1] == "U"):
                        if (script.getUser() in usuario_grupo):
                            cont_editado = "0, " + "U, " + usuario_grupo[2] + ", " + usuario_grupo[3] + ", " + usuario_grupo[4]
                            usuario_existe = True
                            pos = i
                            break
                if (usuario_existe):
                    lineas[pos] = cont_editado
                    info[2] = "\n".join(lineas)
                    #Escribir en archivo users.txt
                    with open(info[0], 'rb+') as archivo:
                        archivo.seek(info[1])
                        archivo.write((info[2]+"$").encode('utf-8'))
                    print("¡Usuario eliminado exitosamente!")
                else:
                    print("¡Error! el usuario a eliminar no existe")
            elif (usuario_actual == ""):
                print("¡Error! ningun usuario ha iniciado sesion.")
            else:
                print("¡Error! solo el usuario 'root' tiene permiso de eliminar usuarios.")
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO MKFILE
    elif (comando.lower() == 'mkfile'):
        if (parametro.lower() == 'path'):
            script.setPath(valor)
        elif (parametro.lower() == 'r'):
            script.setR(True)
        elif (parametro.lower() == 'size'):
            script.setSize(int(valor))
        elif (parametro.lower() == 'cont'):
            script.setCont(valor)
        elif ('ejecutar'):
            if script.errors == 0:
                if (usuario_actual != ""):
                    if (script.getR()):
                        carpetas = os.path.dirname(script.getPath())
                        if (not os.path.exists(script.getPath())):
                            if (not os.path.exists(carpetas)):
                                os.makedirs(carpetas)
                            contenido = ""
                            if (script.getSize() != 0):
                                num = 0
                                for i in range(script.getSize()):
                                    if (num == 10): num = 0
                                    contenido += str(num)
                                    num += 1
                            if (script.getCont() != ""):
                                with open(script.getCont(), "r") as archivo:
                                    contenido = archivo.read()
                            with open(script.getPath(), "w") as archivo:
                                archivo.write(contenido)
                            print("Archivo creado exitosamente")
                        else:
                            respuesta = input("El archivo ya existe, ¿Desea sobreescribirlo? (s/n)")
                            if (respuesta == "s"):
                                #pendiente                       
                                contenido = ""
                                if (script.getSize() != 0):
                                    num = 0
                                    for i in range(script.getSize()):
                                        if (num == 10): num = 0
                                        contenido += str(num)
                                        num += 1
                                if (script.getCont() != ""):
                                    with open(script.getCont(), "r") as archivo:
                                        contenido = archivo.read()
                                with open(script.getPath(), 'w') as archivo:
                                    archivo.write(contenido)
                    else:
                        carpetas = os.path.dirname(script.getPath())
                        if (not os.path.exists(script.getPath())):
                            if (os.path.exists(carpetas)):
                                contenido = ""
                                if (script.getSize() != 0):
                                    num = 0
                                    for i in range(script.getSize()):
                                        if (num == 10): num = 0
                                        contenido += str(num)
                                        num += 1
                                if (script.getCont() != ""):
                                    with open(script.getCont(), "r") as archivo:
                                        contenido = archivo.read()
                                with open(script.getPath(), 'w') as archivo:
                                    archivo.write(contenido)
                                print("Archivo creado exitosamente")
                            else:
                                print("¡Error! la ruta de carpetas no existe.")
                        else:
                            respuesta = input("El archivo ya existe, ¿Desea sobreescribirlo? (s/n)")
                            if (respuesta == "s"):
                                #pendiente                       
                                contenido = ""
                                if (script.getSize() != 0):
                                    num = 0
                                    for i in range(script.getSize()):
                                        if (num == 10): num = 0
                                        contenido += str(num)
                                        num += 1
                                if (script.getCont() != ""):
                                    with open(script.getCont(), "r") as archivo:
                                        contenido = archivo.read()
                                with open(script.getPath(), 'w') as archivo:
                                    archivo.write(contenido)
                else:
                    print("¡Error! ningun usuario ha iniciado sesion.")
            else:
                print('¡Error! no se pudo crear el archivo.')
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO MKDIR
    elif (comando.lower() == 'mkdir'):
        if (parametro.lower() == 'path'):
            script.setPath(valor)
        elif (parametro.lower() == 'r'):
            script.setR(True)
        elif (parametro.lower() == 'ejecutar'):
            if (script.getR()):
                try:
                    os.makedirs(script.getPath())
                except FileNotFoundError as ex:
                    print(ex)
            else:
                try:
                    os.mkdir(script.getPath())
                except FileNotFoundError as ex:
                    print(ex)
        else:
            print("¡Error! parametro no valido.")
        return None
    #COMANDO PAUSE
    elif (comando.lower() == 'pause'):
        while True: 
            tecla = input("\033[1;33m<<Confirm>> {}\033[00m\n" .format("Presione 'ENTER' para continuar "))
            if (tecla == ""):
                break
        return None
    #COMANDO EXECUTE
    elif (comando.lower() == 'execute'):
        if (parametro.lower() == "path"):
            mensajes += '<span class="text-white">leyendo ruta del archivo...</span><br>\n'
            script.setPath(valor)
        elif (parametro.lower() == 'ejecutar'):
            if script.errors == 0:
                with open(script.getPath(), 'r') as archivo:
                    contenido = archivo.read()
                mensajes += '<span class="text-info">...Comando execute ejecutado</span><br>\n'
                return contenido
                #return [contenido, mensajes]
            else:
                mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> No se pudo ejecutar el archivo.</span><br>\n'
        else:
            script.errors += 1
            mensajes += '<span class="text-danger"><i class="fa-solid fa-xmark"></i> Parametro no valido.</span><br>\n'
        return None
    #COMANDO REP
    elif (comando.lower() == "rep"):
        if (parametro.lower() == "name"):
            print("leyendo nombre del reporte...")
            script.setName(valor)
        elif (parametro.lower() == "path"):
            print("leyendo ruta del reporte...")
            script.setPath(valor)
        elif (parametro.lower() == "id"):
            print("leyendo id de la particion...")
            script.setId(valor)
        elif (parametro.lower() == "ruta"):
            print("leyendo ruta del reporte...")
            script.setRuta(valor)
        elif (parametro.lower() == "ejecutar"):
            if (script.errors == 0):
                #buscar particion en particiones montadas
                path = ""
                if script.getId() != "":
                    if script.getId() in particiones_montadas:   
                        name_part = particiones_montadas[script.getId()][0]
                        path = particiones_montadas[script.getId()][1]
                    else:
                        print("\033[91m<<Error>> {}\033[00m" .format("La particion no esta montada."))
                        print("\033[91m<<Error>> {}\033[00m" .format("No se pudo generar el reporte."))
                        return None
                if not(os.path.exists(path)):
                    print("¡el disco no existe!")
                    return None
                if (script.getName().lower() == "file"):
                    #obtener mbr
                    mbr = Mbr()
                    with open(path, 'rb+') as archivo:
                        archivo.seek(0)
                        contenido = archivo.read(mbr.getLength())
                    mbr = mbr.unpack_data(contenido)
                    #obtener particiones
                    pos = 21
                    for i in range(4):
                        particion = Partition()
                        with open(path, 'rb+') as archivo:
                            archivo.seek(pos)
                            contenido = archivo.read(28)
                        particion = particion.unpack_data(contenido)
                        mbr.getPartitions()[i] = particion
                        pos += particion.getLength()
                    #buscar particion
                    part_formateada = None
                    for i, partition in enumerate(mbr.getPartitions()):
                        if (partition.getPart_type().lower() == "p" and partition.getPart_status() == "1"):
                            if (partition.getPart_name().rstrip("\x00") == name_part):
                                part_formateada = partition
                                break
                        elif (partition.getPart_type().lower() == "e" and partition.getPart_status() == "1"):
                            if (partition.getPart_name().rstrip("\x00") == name_part):
                                part_formateada = partition
                                break
                            else:
                                puntero = partition.getPart_start()
                                #obtener ebr
                                ebr = Ebr()
                                with open(path, 'rb+') as archivo:
                                    archivo.seek(puntero)
                                    contenido = archivo.read(ebr.getLength())
                                ebr = ebr.unpack_data(contenido)
                                while True:
                                    if (ebr.getPart_name().rstrip("\x00") == script.getName()):
                                        part_formateada = partition
                                        break
                                    if (ebr.getPart_next() == -1):
                                        break
                                    else:
                                        puntero = ebr.getPart_next()
                                        #obtener ebr
                                        ebr = Ebr()
                                        with open(path, 'rb+') as archivo:
                                            archivo.seek(puntero)
                                            contenido = archivo.read(ebr.getLength())
                                        ebr = ebr.unpack_data(contenido)
                    #verificar si existe la particion
                    if part_formateada == None:
                        print("No se encontro la particion")
                        return None
                    #generar reporte
                    generarReporteArchivo(path, part_formateada, script.getRuta(), script.getPath())                    
                elif (script.getName().lower() == "mbr"):
                    generarReporteMBR(path, script.getPath())
                elif (script.getName().lower() == "disk"):
                    generarReporteDisco(path, script.getPath())
                print("\033[1;32m<<Success>> {}\033[00m" .format("Reporte generado exitosamente."))
                mensajes += '<span class="text-info">...Comando rep ejecutado</span><br>\n'
            if (script.errors != 0):
                print("\033[91m<<Error>> {}\033[00m" .format("No se pudo generar el reporte."))
        else:
            script.errors += 1
            print("\033[91m<<Error>> {}\033[00m" .format("Parametro no valido."))
        return None
    elif (comando[0] == "#"):
        print("\033[90m<<Comment>> {}\033[00m".format(comando[1:]))
        return None

#FUNCIONES
def generarCodigo():
    code = list(range(1001, 1030))
    random.shuffle(code)
    return code.pop()

def generarReporteMBR(path, pathReport):
    code = 'digraph G {\n'
    code += '  subgraph cluster { margin="0.0" penwidth="1.0"\n'
    code += '    tbl [shape=none fontname="Arial" label=<\n'
    code += '        <table border="1" cellborder="0" cellspacing="0">\n'
    #obtener mbr
    code += '        <tr>\n'
    code += '            <td bgcolor="springgreen4" align="left"><font color="white"> REPORTE DE MBR </font></td>\n'
    code += '            <td bgcolor="springgreen4" align="left"><font color="white"> </font></td>\n'
    code += '        </tr>\n'
    mbr = Mbr()
    with open(path, 'rb+') as archivo:
        archivo.seek(0)
        contenido = archivo.read(mbr.getLength())
    mbr = mbr.unpack_data(contenido)
    code += '        <tr>\n'
    code += '            <td bgcolor="white" align="center"> mbr_tamño </td>\n'
    code += '            <td bgcolor="white" align="left"> ' + str(mbr.getTamano()) + ' </td>\n'
    code += '        </tr>\n'
    code += '        <tr>\n'
    code += '            <td bgcolor="white" align="center"> mbr_fecha_creacion </td>\n'
    code += '            <td bgcolor="white" align="left"> ' + str(mbr.getFecha_creacion()) + ' </td>\n'
    code += '        </tr>\n'
    code += '        <tr>\n'
    code += '            <td bgcolor="white" align="center"> mbr_disk_signature </td>\n'
    code += '            <td bgcolor="white" align="left"> ' + str(mbr.getDsk_signature()) + ' </td>\n'
    code += '        </tr>\n'
    #obtener particiones
    pos = mbr.getLength()
    for i in range(4):
        particion = Partition()
        with open(path, 'rb+') as archivo:
            archivo.seek(pos)
            contenido = archivo.read(particion.getLength())
        particion = particion.unpack_data(contenido)
        mbr.getPartitions()[i] = particion
        code += '        <tr>\n'
        code += '            <td bgcolor="teal" align="left"><font color="white"> Particion </font></td>\n'
        code += '            <td bgcolor="teal" align="left"><font color="white"> </font></td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_status </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + mbr.getPartitions()[i].getPart_status() + ' </td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_type </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + mbr.getPartitions()[i].getPart_type() + ' </td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_fit </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + mbr.getPartitions()[i].getPart_fit() + ' </td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_start </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + str(mbr.getPartitions()[i].getPart_start()) + ' </td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_size </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + str(mbr.getPartitions()[i].getPart_s()) + ' </td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_name </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + mbr.getPartitions()[i].getPart_name().rstrip("\x00") + ' </td>\n'
        code += '        </tr>\n'
        if (mbr.getPartitions()[i].getPart_type().lower() == "e" and mbr.getPartitions()[i].getPart_status() == "1"):
            puntero = mbr.getPartitions()[i].getPart_start()
            #generar reporte de ebr
            generarReporteEBR(path, pathReport, puntero)
            #obtener ebr
            ebr = Ebr()
            with open(path, 'rb+') as archivo:
                archivo.seek(puntero)
                contenido = archivo.read(ebr.getLength())
            ebr = ebr.unpack_data(contenido)
            while True:
                code += '        <tr>\n'
                code += '            <td bgcolor="tomato" align="left"><font color="white"> Particion Logica </font></td>\n'
                code += '            <td bgcolor="tomato" align="left"><font color="white"> </font></td>\n'
                code += '        </tr>\n'
                code += '        <tr>\n'
                code += '            <td bgcolor="white" align="center"> part_status </td>\n'
                code += '            <td bgcolor="white" align="left"> ' + str(ebr.getPart_status()) + ' </td>\n'
                code += '        </tr>\n'
                code += '        <tr>\n'
                code += '            <td bgcolor="white" align="center"> part_next </td>\n'
                code += '            <td bgcolor="white" align="left"> ' + str(ebr.getPart_next()) + ' </td>\n'
                code += '        </tr>\n'
                code += '        <tr>\n'
                code += '            <td bgcolor="white" align="center"> part_fit </td>\n'
                code += '            <td bgcolor="white" align="left"> ' + ebr.getPart_fit() + ' </td>\n'
                code += '        </tr>\n'
                code += '        <tr>\n'
                code += '            <td bgcolor="white" align="center"> part_start </td>\n'
                code += '            <td bgcolor="white" align="left"> ' + str(ebr.getPart_start()) + ' </td>\n'
                code += '        </tr>\n'
                code += '        <tr>\n'
                code += '            <td bgcolor="white" align="center"> part_size </td>\n'
                code += '            <td bgcolor="white" align="left"> ' + str(ebr.getPart_s()) + ' </td>\n'
                code += '        </tr>\n'
                code += '        <tr>\n'
                code += '            <td bgcolor="white" align="center"> part_name </td>\n'
                code += '            <td bgcolor="white" align="left"> ' + ebr.getPart_name().rstrip("\x00") + ' </td>\n'
                code += '        </tr>\n'
                if (ebr.getPart_next() == -1):
                    break
                else:
                    puntero = ebr.getPart_next()
                    #obtener ebr
                    ebr = Ebr()
                    with open(path, 'rb+') as archivo:
                        archivo.seek(puntero)
                        contenido = archivo.read(ebr.getLength())
                    ebr = ebr.unpack_data(contenido)
        pos += particion.getLength()
    code += '        </table>\n'
    code += '    >];\n'
    code += '  }\n'
    code += '}'

    with open("reportes/reporte_mbr.dot", "w") as archivo:
        archivo.write(code)
    
    pathReport = verificarNombre(pathReport)

    if(os.path.splitext(os.path.basename(pathReport))[1] == ".jpg"):
        command = ["dot", "-Tjpg", "reportes/reporte_mbr.dot", "-o", pathReport]
    elif (os.path.splitext(os.path.basename(pathReport))[1] == ".png"):
        command = ["dot", "-Tpng", "reportes/reporte_mbr.dot", "-o", pathReport]
    
    subprocess.run(command, check=True)

def generarReporteEBR(path, pathReport, puntero):
    code =  'digraph G {\n'
    code += '  subgraph cluster { margin="0.0" penwidth="1.0"\n'
    code += '    tbl [shape=none fontname="Arial" label=<\n'
    code += '        <table border="1" cellborder="0" cellspacing="0">\n'
    #obtener ebr
    ebr = Ebr()
    with open(path, 'rb+') as archivo:
        archivo.seek(puntero)
        contenido = archivo.read(ebr.getLength())
    ebr = ebr.unpack_data(contenido)
    while True:
        code += '        <tr>\n'
        code += '            <td bgcolor="teal" align="left"><font color="white"> Particion </font></td>\n'
        code += '            <td bgcolor="teal" align="left"><font color="white"> </font></td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_status </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + str(ebr.getPart_status()) + ' </td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_type </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + 'l' + ' </td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_fit </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + str(ebr.getPart_fit()) + ' </td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_start </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + str(ebr.getPart_start()) + ' </td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_size </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + str(ebr.getPart_s()) + ' </td>\n'
        code += '        </tr>\n'
        code += '        <tr>\n'
        code += '            <td bgcolor="white" align="center"> part_name </td>\n'
        code += '            <td bgcolor="white" align="left"> ' + str(ebr.getPart_name()).rstrip("\x00") + ' </td>\n'
        code += '        </tr>\n'
        if (ebr.getPart_next() == -1):
            break
        else:
            puntero = ebr.getPart_next()
            #obtener ebr
            ebr = Ebr()
            with open(path, 'rb+') as archivo:
                archivo.seek(puntero)
                contenido = archivo.read(ebr.getLength())
            ebr = ebr.unpack_data(contenido)
    code += '        </table>\n'
    code += '    >];\n'
    code += '  }\n'
    code += '}'

    
    with open("reportes/reporte_ebr.dot", "w") as archivo:
        archivo.write(code)

    pathReport = verificarNombre(pathReport)

    if(os.path.splitext(os.path.basename(pathReport))[1] == ".jpg"):
        command = ["dot", "-Tjpg", "reportes/reporte_ebr.dot", "-o", pathReport]
    elif (os.path.splitext(os.path.basename(pathReport))[1] == ".png"):
        command = ["dot", "-Tpng", "reportes/reporte_ebr.dot", "-o", pathReport]
    
    subprocess.run(command, check=True)

def generarReporteDisco(path, pathReport):
    code =  'digraph G {\n'
    code += '    subgraph cluster { margin="5.0" penwidth="1.0" bgcolor="#68d9e2"\n'
    code += '        node [style="rounded" style=filled fontname="Arial" fontsize="16" margin=0.3];\n'
    label = ''
    #obtener mbr
    mbr = Mbr()
    with open(path, 'rb+') as archivo:
        archivo.seek(0)
        contenido = archivo.read(mbr.getLength())
    mbr = mbr.unpack_data(contenido)
    label += 'MBR'
    #obtener particiones
    pos = mbr.getLength()
    for i in range(4):
        particion = Partition()
        with open(path, 'rb+') as archivo:
            archivo.seek(pos)
            contenido = archivo.read(particion.getLength())
        particion = particion.unpack_data(contenido)
        mbr.getPartitions()[i] = particion
        if (mbr.getPartitions()[i].getPart_type().lower() == "p"):
            if (mbr.getPartitions()[i].getPart_status() == "0"):
                label += '|Libre'
            elif (mbr.getPartitions()[i].getPart_status() == "1"):
                label += '|Primaria'
        elif (mbr.getPartitions()[i].getPart_type().lower() == "e"):
            if (mbr.getPartitions()[i].getPart_status() == "0"):
                label += '|Libre'
            elif (mbr.getPartitions()[i].getPart_status() == "1"):
                puntero = mbr.getPartitions()[i].getPart_start()
                #obtener ebr
                ebr = Ebr()
                with open(path, 'rb+') as archivo:
                    archivo.seek(puntero)
                    contenido = archivo.read(ebr.getLength())
                ebr = ebr.unpack_data(contenido)
                label += '|{Extendida|{'
                while True:
                    if (ebr.getPart_status() == "1"):
                        label += 'EBR|Logica'
                    elif (ebr.getPart_status() == "0"):
                        label += 'EBR|Libre'
                    if (ebr.getPart_next() == -1):
                        break
                    else:
                        puntero = ebr.getPart_next()
                        #obtener ebr
                        ebr = Ebr()
                        with open(path, 'rb+') as archivo:
                            archivo.seek(puntero)
                            contenido = archivo.read(ebr.getLength())
                        ebr = ebr.unpack_data(contenido)
                        label += '|'
                label += '}}'
        pos += particion.getLength()
    code += '        node_disk [shape="record" label="' + label + '"];\n'
    code += '    }\n'
    code += '}'

    with open("reportes/reporte_disco.dot", "w") as archivo:
        archivo.write(code)

    pathReport = verificarNombre(pathReport)

    if(os.path.splitext(os.path.basename(pathReport))[1] == ".jpg"):
        command = ["dot", "-Tjpg", "reportes/reporte_disco.dot", "-o", pathReport]
    elif (os.path.splitext(os.path.basename(pathReport))[1] == ".png"):
        command = ["dot", "-Tpng", "reportes/reporte_disco.dot", "-o", pathReport]

    subprocess.run(command, check=True)

def generarReporteArchivo(path, part_formateada, ruta, pathReport):
    if ruta == '"/users.txt"':
        #obtener inicio de archivos users.txt
        ini_archivo = part_formateada.getPart_start()
        #verificar si esta formateada la particion
        with open(path, 'rb+') as archivo:
            archivo.seek(ini_archivo)
            byte = archivo.read(1)
            if byte == b'\x00':
                print(f"La particion {part_formateada.getPart_name()} no esta formateada")
                return None
        #obtener longitud de archivo users.txt
        pos = 0
        with open(path, 'rb+') as archivo:
            archivo.seek(ini_archivo)
            while True:
                byte = archivo.read(1)
                if not byte:
                    break
                if byte == b'$':
                    break
                pos += 1
        #obtener contenido de archivo users.txt
        with open(path, 'rb+') as archivo:
            archivo.seek(ini_archivo)
            contenido = archivo.read(pos)
        contenido = contenido.decode('utf-8')
        #crear reporte
        with open(pathReport, 'w') as archivo:
            archivo.write(contenido)
        print(pathReport)
        print(contenido)
    else:
        pass

def verificarNombre(pathReport):
    n = 1
    while True:
        if not(os.path.exists(pathReport)):
            break
        else:
            carpetas = os.path.dirname(pathReport)
            nombre, extension = os.path.splitext(os.path.basename(pathReport))
            if ("(" in nombre):
                nombre = nombre[:nombre.index("(")+1] + str(n) + nombre[nombre.index(")"):]
            else:
                nombre += "(" + str(n) + ")"
            pathReport = carpetas + "/" + nombre + extension
            n += 1
    return pathReport

def setM():
    global mensajes
    mensajes = ""

def getMessages():
    global mensajes
    return mensajes