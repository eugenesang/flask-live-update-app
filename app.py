from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')

# Initialize list of fruits
fruits = ['Apple', 'Banana', 'Cherry']

@app.route('/')
def index():
    return render_template('index.html', fruits=fruits)

@app.route('/media/<filename>')
def send_file(filename):
    return send_from_directory('media', filename)

@socketio.on('remove_fruit')
def remove_fruit(fruit):
    if fruit in fruits:
        fruits.remove(fruit)
        emit('update_fruits', fruits, broadcast=True)

@socketio.on('add_fruit')
def add_fruit(fruit):
    fruits.append(fruit)
    emit('update_fruits', fruits, broadcast=True)
    emit('new_fruit_notification', fruit, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)