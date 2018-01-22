from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app_port = 5001
print('server start, app_port = %d'%(app_port));

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

@socketio.on('image_set_path', namespace='/image')
def test_message(message):
    print('socketio image_set_path enter')
    print(message)
    function_new('image1.jpg');
    emit('res', 'ok');

@socketio.on('image_get_res', namespace='/image')
def test_message(message):
    print('socketio image_get_res enter')
    print(message)
    #function_new('image1.jpg');
    print(max_string);
    emit('image_res', max_string)

if __name__ == '__main__':
    socketio.run(app, port=app_port)
    