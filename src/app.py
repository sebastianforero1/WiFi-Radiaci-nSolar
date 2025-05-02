# app.py del receptor (recibe los datos)
from flask import Flask, jsonify, request
from datetime import datetime
import os
import json

app = Flask(__name__)
DATA_FOLDER = os.path.join(os.path.dirname(__file__), 'data')
DATA_FILE = os.path.join(DATA_FOLDER, 'sensor_w_rs_001.json')

@app.route('/recibir', methods=['POST'])
def recibir_radiacion():
    data = request.get_json()
    if not data or "RADIACION_SOLAR" not in data:
        return jsonify({"error": "JSON inválido o faltante"}), 400

    ultima_radiacion = {
        "RADIACION_SOLAR": data["RADIACION_SOLAR"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    os.makedirs(DATA_FOLDER, exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(ultima_radiacion, f, indent=2)

    return jsonify({"mensaje": "Datos recibidos correctamente"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6451)


# Comandos Docker para crear y construir imágenes
# docker volume create sensor-data
# cd proyecto/receptor
# docker build -t receptor-app .

# cd ../visualizador
# docker build -t visualizador-app .
# docker run -d --name receptor \
#  -v sensor-data:/app/data \
# -p 6451:6451 \
#  receptor-app

# docker run -d --name visualizador \
#  -v sensor-data:/app/data \
#  -p 6452:6452 \
#  visualizador-app
