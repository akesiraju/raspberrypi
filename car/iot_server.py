import socket
import json
from flask import Flask, request, render_template, Response
from camera import VideoCamera
from flask import jsonify
# from flask_cors import CORS, cross_origin
import car
import logging
# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import os
from iot_connection import IotConnection

app = Flask(__name__, static_url_path='')

con = IotConnection()
# CORS(app)
my_car = [None] * 1

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/<int:signal>")
def move(signal):        
    ret = my_car[0].move(signal)
    con.publish({'signal': signal})
    return jsonify({'status': ret})


@app.route("/")
def control():
    my_car[0] = car.Car()
    return render_template('index.html', title='Car Control', ip=_get_ip())


def _get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
