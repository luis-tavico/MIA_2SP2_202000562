from analizador.gramatica import analizador

#execute -path=/home/user/Escritorio/prueba.adsj
#sudo rm -r '/home/luis_tavico/Escritorio/mis discos'

if __name__ == '__main__':
    while True:
        entrada = input("App> ")
        if entrada == 'exit': break
        waiting_scripts = analizador(entrada)
        while (waiting_scripts != None):
            waiting_scripts = analizador(waiting_scripts)