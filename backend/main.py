from flask import Flask, jsonify, request
from flask_cors import CORS
from analizador.gramatica import *

#execute -path="/home/luis_tavico/Escritorio/ArchivosdeEntrada2S2023/Archivos de Prueba/prueba-1.adsj"
#execute -path="/home/user/Escritorio/prueba.adsj"
#sudo rm -r '/home/luis_tavico/Escritorio/mis discos'

app = Flask(__name__)
CORS(app)

global waiting_lines, reports_list
waiting_lines = []
reports_list = []

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "MIA-2S-PY2-202000562"}), 200

@app.route("/", methods=["POST"])
def console():
    clearMessages()
    global waiting_lines, reports_list
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
            if (not line.isspace() and line != ""):
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
        reports_list = getReports()
        return jsonify({"response": getMessages()}), 201
    else:
        setRespuesta(reply)
        while len(waiting_lines) > 0:
            line = waiting_lines.pop(0)
            if (not line.isspace() and line != ""):
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

@app.route("/login", methods=["POST"])
def login():
    clearMessages()
    global waiting_lines
    #{"nombre":["contenido de textarea", "respuesta a pregunta"]}
    rqst = request.get_json()['request'] 
    content = rqst[0]
    limpiarValores()
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
    return jsonify({"message": getMessagesLogin(), "status": getStatus()}), 201

@app.route("/logout", methods=["POST"])
def logout():
    clearMessages()
    global waiting_lines
    #{"nombre":["contenido de textarea", "respuesta a pregunta"]}
    rqst = request.get_json()['request'] 
    content = rqst[0]
    limpiarValores()
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
    return jsonify({"message": "Sesion finalizada exitosamente.", "status": "Ok"}), 201
    
@app.route("/reports", methods=["GET"])
def reports():
    global reports_list
    return jsonify({"reports": reports_list}), 200

if __name__ == "__main__":
    app.run(debug=True)