from flask import Flask, jsonify, request
from analizador.gramatica import analizador

#execute -path="/home/luis_tavico/Escritorio/ArchivosdeEntrada2S2023/Archivos de Prueba/prueba-1.adsj"
#sudo rm -r '/home/luis_tavico/Escritorio/mis discos'

app = Flask(__name__)

@app.route("/members")
def members():
    return {"members": ["contenido"]}


@app.route("/", methods=["POST"])
def analyzer():
    content = request.get_json()
    c = content['contenido'] + "$"
    waiting_scripts = analizador(c)
    while (waiting_scripts != None):
        waiting_scripts = analizador(waiting_scripts + "$")
    return jsonify({"mensaje": "¡Analisis realizado exitosamente!"}), 201

    '''
    response = True
    if response:
        return jsonify({"mensaje": "¡Recurso creado exitosamente!"}), 201
    else:
        return jsonify({"mensaje": "¡Error! Recurso repetido"}), 400
    '''

if __name__ == "__main__":
    app.run(debug=True)