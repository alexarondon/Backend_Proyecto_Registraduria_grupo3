from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi

app = Flask(__name__)
cors = CORS(app)

from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorCandidato import ControladorCandidato
miControladorPartido = ControladorPartido()
miControladorCandidato = ControladorCandidato()

@app.route("/", methods = ['GET'])
def test():
    json = {}
    json['mensaje'] = "Servidor ejecutandose ..."
    return jsonify(json)

@app.route("/", methods = ['POST'])
def testPost():
    json = {}
    json['mensaje'] = "Servidor corriendo POST..."
    return jsonify(json)

#INICIO Rutas del controlador Partido
@app.route("/partidos", methods=['GET'])
def indexPartidos():
    json = miControladorPartido.index()
    return jsonify(json)

@app.route("/partidos", methods=['POST'])
def createPartidos():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['PUT'])
def updatePartidos(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['DELETE'])
def deletePartidos(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=['GET'])
def showPartidos(id):
    json = miControladorPartido.show(id)
    return jsonify(json)


#FIN Rutas del controlador Partido

#INICIO Rutas del controlador Candidato
@app.route("/candidatos", methods=['GET'])
def indexCandidatos():
    json= miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidatos", methods=['POST'])
def createCandidatos():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['PUT'])
def updateCandidatos(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['DELETE'])
def deleteCandidatos(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)

@app.route("/candidatos/<string:id>", methods=['GET'])
def showCandidatos(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)

@app.route("/candidatos/<string:id_candidato>/partidos/<string:id_partido>", methods=['PUT'])
def setPartido(id_candidato, id_partido):
    json = miControladorCandidato.setPartido(id_candidato, id_partido)
    return jsonify(json)

#FIN Rutas del controlador Candidato

def loadConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    ca = certifi.where()
    client = pymongo.MongoClient(
        "mongodb+srv://admin:admin@cluster0.dolcbdp.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
    db = client.test
    print(db)

    baseDatos = client['BD-Registraduria'] #Conexion a la base de datos
    print(baseDatos.list_collection_names()) #Validacion que la conexion es a la BD correcta

    dataConfig = loadConfig()
    print("Server ejecutandose... " + "http://" + dataConfig['url-backend'] + ":" + str(dataConfig['port']))
    serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])