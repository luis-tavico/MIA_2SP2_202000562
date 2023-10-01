from flask import Flask, jsonify, request
from flask_cors import CORS
from analizador.gramatica import *

#execute -path="/home/luis_tavico/Escritorio/ArchivosdeEntrada2S2023/Archivos de Prueba/prueba-1.adsj"
#execute -path="/home/user/Escritorio/prueba.adsj"
#sudo rm -r '/home/luis_tavico/Escritorio/mis discos'

app = Flask(__name__)
CORS(app)

@app.route("/inicio")
def inicio():
    return jsonify({"mensaje":"hola"}), 200

@app.route("/login")
def login():
    return {"user": "admin"}

global waiting_lines
waiting_lines = []

@app.route("/", methods=["POST"])
def console():
    clearMessages()
    global waiting_lines
    #{"nombre":["contenido de textarea", "respuesta a pregunta"]}
    rqst = request.get_json()['request'] 
    content = rqst[0]
    reply = rqst[1]
    if (reply == "None"):
        clearValues()
        waiting_lines = []
        lines = content.splitlines()
        while len(lines) > 0:
            line = lines.pop(0)
            if not (line.isspace()):
                waiting_scripts = analizador(line)
                if waiting_scripts == None:
                    pass
                elif waiting_scripts == "pausa" or waiting_scripts == "confirmacion":
                    lines.insert(0, line)
                    waiting_lines = lines
                    break
                else:
                    new_lines = waiting_scripts.splitlines()
                    new_lines.extend(lines)
                    lines = new_lines
        return jsonify({"response": getMessages()}), 201
    else:
        setRespuesta(reply)
        while len(waiting_lines) > 0:
            line = waiting_lines.pop(0)
            if not (line.isspace()):
                waiting_scripts = analizador(line)
                if waiting_scripts == None:
                    pass
                elif waiting_scripts == "pausa" or waiting_scripts == "confirmacion":
                    waiting_lines.insert(0, line)
                    break
                else:
                    new_lines = waiting_scripts.splitlines()
                    new_lines.extend(waiting_lines)
                    waiting_lines = new_lines                
        return jsonify({"response": getMessages()}), 201

if __name__ == "__main__":
    app.run(debug=True)