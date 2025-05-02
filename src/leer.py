# app.py del visualizador (muestra los datos)
from flask import Flask, jsonify
import os
import json

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'sensor_w_rs_001.json')

@app.route('/ver', methods=['GET'])
def ver_radiacion():
    if not os.path.exists(DATA_FILE):
        return jsonify({"error": "Archivo de datos no encontrado"}), 404

    with open(DATA_FILE, 'r') as f:
        try:
            datos = json.load(f)
        except json.JSONDecodeError:
            return jsonify({"error": "Error al leer JSON"}), 500

    return jsonify(datos), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6452)
