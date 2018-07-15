from flask import Flask, request, render_template
from flask import jsonify
from flask_cors import CORS, cross_origin
import drive

app = Flask(__name__, static_url_path='')
CORS(app)


@app.route("/<int:direction_id>")
def move(direction_id):
    signal = drive.move(direction_id)
    return jsonify({'status':direction_id})

@app.route("/")
def control():
    return render_template('index.html', title='Car Control')


if __name__ == '__main__':
    app.run(port=5002)