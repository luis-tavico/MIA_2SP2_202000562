import analizador.ply.lex as lex
import analizador.ply.yacc as yacc
from analizador.scripts import *

errors = []

reserved_words = {
    #Comandos
    'mkdisk': 'MKDISK',
    'rmdisk': 'RMDISK',
    'fdisk' : 'FDISK',
    'mount' : 'MOUNT',
    'unmount' : 'UNMOUNT',
    'mkfs' : 'MKFS',
    'login' : 'LOGIN',
    'logout' : 'LOGOUT',
    'mkgrp' : 'MKGRP',
    'rmgrp' : 'RMGRP',
    'mkusr' : 'MKUSR',
    'rmusr' : 'RMUSR',
    'mkfile' : 'MKFILE',
    'mkdir' : 'MKDIR',
    'pause' : 'PAUSE',
    'execute' : 'EXECUTE',
    'rep': 'REP',
    #Parametros
    'size': 'SIZE',
    'path': 'PATH',
    'fit': 'FIT',
    'unit': 'UNIT',
    'name' : 'NAME',
    'type' : 'TYPE',
    'id': 'ID',
    'user': 'USER',
    'pass': 'PASS',
    'grp' : 'GRP',
    'r' : 'R',
    'cont' : 'CONT',
    'ruta' : 'RUTA'
    #Valores
}

tokens = [
    'GUION',
    'IGUAL',
    'RUTA_ARCHIVO',
    'RUTA_CARPETA',
    'NOMBRE_ARCHIVO',
    'ENTERO',
    'CADENA',
    'COMENTARIO'
] + list(reserved_words.values())

t_ignore = ' \t'
t_GUION = r'-'
t_IGUAL = r'='

def t_RUTA_ARCHIVO(t):
    r'(\"(\/(\w|\s|-)+)+\.[a-zA-Z]+\")|((\/(\w|-)+)+\.[a-zA-Z]+)'
    return t

def t_RUTA_CARPETA(t):
    r'(\"(\/(\w|\s|-)+)+\")|((\/(\w|-)+)+)'
    return t

def t_NOMBRE_ARCHIVO(t):
    r'(\"(\w|\s|-)+\.txt\")|((\w|-)+\.txt)'
    return t

def t_CADENA(t):
    r'[a-zA-Z_0-9]+'
    t.type = reserved_words.get(t.value.lower(), 'CADENA')
    return t

def t_ENTERO(t):
    r'\d+|-\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print(f"Error al convertir {t.value} a entero")
        t.value = 0
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_COMENTARIO(t):
    r'\#.*'
    return t

def t_error(t):
    print(f"Caracter {t.value[0]} ilegal")
    t.lexer.skip(1)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

lexer = lex.lex()
lexer.ignore_case = True

global waiting_scripts
waiting_scripts = ""

precedence = ( )

def p_instrucciones(t):
    '''instrucciones : instruccion instrucciones
                     | instruccion'''
    global waiting_scripts
    t[0] = waiting_scripts

def p_instruccion(t):
    '''instruccion : comando parametros
                   | comando'''
    global waiting_scripts
    waiting_scripts = comando_ejecutar("ejecutar", None)

def p_comando(t):
    '''comando : MKDISK
               | RMDISK
               | FDISK
               | MOUNT
               | UNMOUNT
               | MKFS
               | LOGIN
               | LOGOUT
               | MKGRP
               | RMGRP
               | MKUSR
               | RMUSR
               | MKFILE
               | MKDIR
               | PAUSE
               | EXECUTE
               | REP
               | COMENTARIO'''
    comando_activar(str(t[1]))
    
def p_parametros (t):
    '''parametros : parametro parametros
                  | parametro'''
    
def p_parametro (t):
    '''parametro : argumento
                 | opcion'''

def p_argumento(t):
    'argumento : GUION param IGUAL valor'
    global waiting_scripts
    waiting_scripts = comando_ejecutar(str(t[2]), str(t[4]))

def p_param(t):
    '''param : SIZE
             | PATH
             | FIT
             | UNIT
             | NAME
             | TYPE
             | ID
             | USER
             | PASS
             | GRP
             | CONT
             | RUTA'''
    t[0] = t[1]

def p_valor(t):
    '''valor : ENTERO
             | RUTA_ARCHIVO
             | RUTA_CARPETA
             | NOMBRE_ARCHIVO
             | CADENA'''
    t[0] = t[1]

def p_opcion(t):
    'opcion : GUION R'
    global waiting_scripts
    waiting_scripts = comando_ejecutar(str(t[2]), None)

def p_error(t):
    print(f"Error sintáctico en {t}")

def analizador(input):
    global errors, parser
    parser = yacc.yacc()
    lexer.lineno = 1
    return parser.parse(input)