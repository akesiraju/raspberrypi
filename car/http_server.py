from flask import Flask, request, render_template
from flask import jsonify
#from flask_cors import CORS, cross_origin
from car import Car

app = Flask(__name__, static_url_path='')
#CORS(app)
my_car = Car()


@app.route("/<int:direction_id>")
def move(direction_id):
    signal = my_car.move(direction_id)
    return jsonify({'status':direction_id})

@app.route("/")
def control():
    my_car = Car()
    return render_template('index.html', title='Car Control')


if __name__ == '__main__':
    app.run(host='192.168.2.18',port=5002)
