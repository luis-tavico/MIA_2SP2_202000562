from analizador.gramatica import *

#execute -path="/home/luis_tavico/Escritorio/ArchivosdeEntrada2S2023/Archivos de Prueba/prueba-1.adsj"
#sudo rm -r '/home/luis_tavico/Escritorio/mis discos'

if __name__ == '__main__':
    while True:
        clearMessages()
        entrada = input("App> ")
        if entrada == 'exit': break
        waiting_scripts = analizador(entrada)
        while (waiting_scripts != None):
            waiting_scripts = analizador(waiting_scripts)
        print(getMessages())