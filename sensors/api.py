from flask import Flask, jsonify, render_template, Response
import Adafruit_DHT
from datetime import datetime
import socket
from flask_cors import CORS, cross_origin


app = Flask(__name__, static_url_path="")
CORS(app)


@app.route("/api/v1/climate", methods=["GET"])
@cross_origin()
def get_temperature():
    return jsonify(_get_climate())


def _get_climate():
    humidity, temperature = Adafruit_DHT.read_retry(11, 12)
    return {"temperature": temperature, "humidity": humidity, "time": datetime.now().strftime("%H:%M:%S")}


@app.route("/api/v1/status", methods=["GET"])
@cross_origin()
def get_status():
    return jsonify({"msg": "Sensors are working as expected."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
