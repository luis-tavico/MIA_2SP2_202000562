
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CADENA COMENTARIO CONT ENTERO EXECUTE FDISK FIT GRP GUION ID IGUAL LOGIN LOGOUT MKDIR MKDISK MKFILE MKFS MKGRP MKUSR MOUNT NAME NOMBRE_ARCHIVO PASS PATH PAUSE R REP RMDISK RMGRP RMUSR RUTA RUTA_ARCHIVO RUTA_CARPETA SIZE TYPE UNIT UNMOUNT USERinstrucciones : instruccion instrucciones\n                     | instruccioninstruccion : comando parametros\n                   | comandocomando : MKDISK\n               | RMDISK\n               | FDISK\n               | MOUNT\n               | UNMOUNT\n               | MKFS\n               | LOGIN\n               | LOGOUT\n               | MKGRP\n               | RMGRP\n               | MKUSR\n               | RMUSR\n               | MKFILE\n               | MKDIR\n               | PAUSE\n               | EXECUTE\n               | REP\n               | COMENTARIOparametros : parametro parametros\n                  | parametroparametro : argumento\n                 | opcionargumento : GUION param IGUAL valorparam : SIZE\n             | PATH\n             | FIT\n             | UNIT\n             | NAME\n             | TYPE\n             | ID\n             | USER\n             | PASS\n             | GRP\n             | CONT\n             | RUTAvalor : ENTERO\n             | RUTA_ARCHIVO\n             | RUTA_CARPETA\n             | NOMBRE_ARCHIVO\n             | CADENAopcion : GUION R'
    
_lr_action_items = {'MKDISK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[4,4,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'RMDISK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[5,5,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'FDISK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[6,6,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'MOUNT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[7,7,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'UNMOUNT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[8,8,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'MKFS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[9,9,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'LOGIN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[10,10,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'LOGOUT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[11,11,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'MKGRP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[12,12,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'RMGRP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[13,13,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'MKUSR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[14,14,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'RMUSR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[15,15,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'MKFILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[16,16,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'MKDIR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[17,17,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'PAUSE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[18,18,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'EXECUTE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[19,19,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'REP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[20,20,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'COMENTARIO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,28,30,44,45,46,47,48,49,],[21,21,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,30,44,45,46,47,48,49,],[0,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-1,-3,-24,-25,-26,-23,-45,-27,-40,-41,-42,-43,-44,]),'GUION':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,25,26,30,44,45,46,47,48,49,],[27,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,27,-25,-26,-45,-27,-40,-41,-42,-43,-44,]),'R':([27,],[30,]),'SIZE':([27,],[31,]),'PATH':([27,],[32,]),'FIT':([27,],[33,]),'UNIT':([27,],[34,]),'NAME':([27,],[35,]),'TYPE':([27,],[36,]),'ID':([27,],[37,]),'USER':([27,],[38,]),'PASS':([27,],[39,]),'GRP':([27,],[40,]),'CONT':([27,],[41,]),'RUTA':([27,],[42,]),'IGUAL':([29,31,32,33,34,35,36,37,38,39,40,41,42,],[43,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,]),'ENTERO':([43,],[45,]),'RUTA_ARCHIVO':([43,],[46,]),'RUTA_CARPETA':([43,],[47,]),'NOMBRE_ARCHIVO':([43,],[48,]),'CADENA':([43,],[49,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,2,],[1,22,]),'instruccion':([0,2,],[2,2,]),'comando':([0,2,],[3,3,]),'parametros':([3,24,],[23,28,]),'parametro':([3,24,],[24,24,]),'argumento':([3,24,],[25,25,]),'opcion':([3,24,],[26,26,]),'param':([27,],[29,]),'valor':([43,],[44,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> instruccion instrucciones','instrucciones',2,'p_instrucciones','gramatica.py',109),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','gramatica.py',110),
  ('instruccion -> comando parametros','instruccion',2,'p_instruccion','gramatica.py',115),
  ('instruccion -> comando','instruccion',1,'p_instruccion','gramatica.py',116),
  ('comando -> MKDISK','comando',1,'p_comando','gramatica.py',121),
  ('comando -> RMDISK','comando',1,'p_comando','gramatica.py',122),
  ('comando -> FDISK','comando',1,'p_comando','gramatica.py',123),
  ('comando -> MOUNT','comando',1,'p_comando','gramatica.py',124),
  ('comando -> UNMOUNT','comando',1,'p_comando','gramatica.py',125),
  ('comando -> MKFS','comando',1,'p_comando','gramatica.py',126),
  ('comando -> LOGIN','comando',1,'p_comando','gramatica.py',127),
  ('comando -> LOGOUT','comando',1,'p_comando','gramatica.py',128),
  ('comando -> MKGRP','comando',1,'p_comando','gramatica.py',129),
  ('comando -> RMGRP','comando',1,'p_comando','gramatica.py',130),
  ('comando -> MKUSR','comando',1,'p_comando','gramatica.py',131),
  ('comando -> RMUSR','comando',1,'p_comando','gramatica.py',132),
  ('comando -> MKFILE','comando',1,'p_comando','gramatica.py',133),
  ('comando -> MKDIR','comando',1,'p_comando','gramatica.py',134),
  ('comando -> PAUSE','comando',1,'p_comando','gramatica.py',135),
  ('comando -> EXECUTE','comando',1,'p_comando','gramatica.py',136),
  ('comando -> REP','comando',1,'p_comando','gramatica.py',137),
  ('comando -> COMENTARIO','comando',1,'p_comando','gramatica.py',138),
  ('parametros -> parametro parametros','parametros',2,'p_parametros','gramatica.py',142),
  ('parametros -> parametro','parametros',1,'p_parametros','gramatica.py',143),
  ('parametro -> argumento','parametro',1,'p_parametro','gramatica.py',146),
  ('parametro -> opcion','parametro',1,'p_parametro','gramatica.py',147),
  ('argumento -> GUION param IGUAL valor','argumento',4,'p_argumento','gramatica.py',150),
  ('param -> SIZE','param',1,'p_param','gramatica.py',155),
  ('param -> PATH','param',1,'p_param','gramatica.py',156),
  ('param -> FIT','param',1,'p_param','gramatica.py',157),
  ('param -> UNIT','param',1,'p_param','gramatica.py',158),
  ('param -> NAME','param',1,'p_param','gramatica.py',159),
  ('param -> TYPE','param',1,'p_param','gramatica.py',160),
  ('param -> ID','param',1,'p_param','gramatica.py',161),
  ('param -> USER','param',1,'p_param','gramatica.py',162),
  ('param -> PASS','param',1,'p_param','gramatica.py',163),
  ('param -> GRP','param',1,'p_param','gramatica.py',164),
  ('param -> CONT','param',1,'p_param','gramatica.py',165),
  ('param -> RUTA','param',1,'p_param','gramatica.py',166),
  ('valor -> ENTERO','valor',1,'p_valor','gramatica.py',170),
  ('valor -> RUTA_ARCHIVO','valor',1,'p_valor','gramatica.py',171),
  ('valor -> RUTA_CARPETA','valor',1,'p_valor','gramatica.py',172),
  ('valor -> NOMBRE_ARCHIVO','valor',1,'p_valor','gramatica.py',173),
  ('valor -> CADENA','valor',1,'p_valor','gramatica.py',174),
  ('opcion -> GUION R','opcion',2,'p_opcion','gramatica.py',178),
]
