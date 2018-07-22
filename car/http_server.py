from flask import Flask, request, render_template
from flask import jsonify
#from flask_cors import CORS, cross_origin
import car

app = Flask(__name__, static_url_path='')
#CORS(app)
my_car = [None]*1


@app.route("/<int:direction_id>")
def move(direction_id):
    signal = my_car[0].move(direction_id)
    return jsonify({'status':direction_id})

@app.route("/beta")
def control():
    my_car[0] = car.Car()
    return render_template('index.html', title='Car Control')

if __name__ == '__main__':
    app.run(host='192.168.2.18',port=5002)
