import socket
import json
from flask import Flask, request, render_template, Response

# from camera import VideoCamera
from flask import jsonify

# from flask_cors import CORS, cross_origin
import body

app = Flask(__name__, static_url_path="")
# CORS(app)


# def gen(camera):
# while True:
# frame = camera.get_frame()
# yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# @app.route('/video_feed')
# def video_feed():
# return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/<int:signal>")
def move(signal):
    if signal == 258:
        body.stop_walk()
        body.walk_forward()

    if signal == 260:
        body.stop_walk()
        body.turn_left()

    if signal == 261:
        body.stop_walk()
        body.turn_right()

    if signal == 259:
        body.stop_walk()
        body.walk_backward()

    if signal == 32 or signal == 27:
        body.stop_walk()

    return jsonify({"status": 200})


@app.route("/")
def control():
    return render_template("mike.html", title="Mike Controller", ip=_get_ip())


def _get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
