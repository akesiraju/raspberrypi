import socket
import json
from flask import Flask, request, render_template, Response
#from camera import VideoCamera
from flask import jsonify
#from flask_cors import CORS, cross_origin
import car
import car_beta

app = Flask(__name__, static_url_path='')
# CORS(app)
my_car = [None] * 1

#def gen(camera):
    #while True:
        #frame = camera.get_frame()
        #yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#@app.route('/video_feed')
#def video_feed():
    #return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/<int:signal>")
def move(signal):
    ret = my_car[0].move(signal)
    return jsonify({'status': ret})

@app.route("/")
def control():
    my_car[0] = car.Car()
    return render_template('charlie.html', title='Car Control', ip=_get_ip())

@app.route("/drive/forward")
def drive_forward():
    signal = my_car[0].forward()
    return jsonify({'status': signal})


@app.route("/turn/<float:angle>")
def turn(angle):
    signal = my_car[0].turn(angle)
    return jsonify({'status': signal})


@app.route("/drive/reverse")
def drive_reverse():
    signal = my_car[0].reverse()
    return jsonify({'status': signal})

@app.route("/brakes/apply")
def brakes():
    signal = my_car[0].apply_brakes()
    return jsonify({'status': signal})

@app.route("/engine/off")
def engine():
    signal = my_car[0].clear()
    return jsonify({'status': signal})

@app.route("/beta")
def control_beta():
    my_car[0] = car_beta.Car()
    return render_template('beta.html', title='Car Control', ip=_get_ip())


def _get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
