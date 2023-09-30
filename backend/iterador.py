'''
contenido = "sera un parrafo de texto\nextraido de un documento\nde texto."
#{"nombre":["contenido de textarea", "respuesta a pregunta"]}
request = {"request":[contenido, None]}
request = {"request":[contenido, ""]}
request = {"request":[contenido, "s"]}
'''

content = "sera un parrafo de texto\nextraido de un documento\nde texto."
waiting_scripts = 'texto agregado\ndesde otro archivo\nde texto'
lines = content.splitlines()
while len(lines) > 0:
    line = lines.pop(0)
    if not (line.isspace()):
        if waiting_scripts == None:
            pass
        elif waiting_scripts == "pausa":
            pass
        elif waiting_scripts == "confirmacion":
            pass
        else:
            new_lines = waiting_scripts.splitlines()
            new_lines.extend(lines)
            lines = new_lines
            break