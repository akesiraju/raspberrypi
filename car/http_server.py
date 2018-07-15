from flask import Flask
from flask import jsonify
import drive

app = Flask(__name__)

@app.route("/<int:direction_id>")
def move(direction_id):
    signal = drive.move(direction_id)
    return jsonify({'Moving':signal})

if __name__ == '__main__':
    app.run(port=5002)