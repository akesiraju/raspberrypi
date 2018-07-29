import socket
from flask import Flask, request, render_template
from flask import jsonify
#from flask_cors import CORS, cross_origin
import car

app = Flask(__name__, static_url_path='')
# CORS(app)
my_car = [None] * 1


@app.route("/<int:direction_id>")
def move(direction_id):
    signal = my_car[0].move(direction_id)
    return jsonify({'status': direction_id})


@app.route("/")
def control():
    my_car[0] = car.Car()
    return render_template('index.html', title='Car Control', ip=_get_ip())


@app.route("/beta/")
def control_beta():
    my_car[0] = car.Car()
    return render_template('beta.html', title='Car Control', ip=_get_ip())


def _get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
