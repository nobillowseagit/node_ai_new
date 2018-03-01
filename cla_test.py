import os
import shutil  

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import test1

image_base_dir = 'd:/tensorflow/mydata/cat_dog2/'
source_file_full_name = 'd:/node/node_ai_new/image1.jpg'

index = -1


print('init train_test server');
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('cla_test', namespace='/image')
def test_message(message):
    print('socketio cla_test enter')
    print(message)

    global index
    index = test1.evaluate_one_image(source_file_full_name)
    print(index)

    emit('res', 'ok');

@socketio.on('req_cla_test_res', namespace='/image')
def test_message(message):
    print('socketio req_cla_test_res enter');
    print(message);

    print(index);


    emit('cla_test_res', str(index));


if __name__ == '__main__':
    socketio.run(app, port=9001)