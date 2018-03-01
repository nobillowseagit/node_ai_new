import os
import shutil  

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import pinyin
from pinyin._compat import u

import train1

image_base_dir = 'd:/tensorflow/mydata/cat_dog2/'
source_file_full_name = 'd:/node/node_ai_new/image1.jpg'





arrObj = [('wei4zhi1', '未知', 0), ('shou3ji1', '手机', 1), ('ming2pian4', '名片', 2)];



def get_file_index(file_dir, cla_name):
    print('get_file_file enter')

    max_index = 0
    for file in os.listdir(file_dir):  
        name = file.split(sep='.')  
        if name[0] == cla_name:
            index = int(name[1])
            if index > max_index:
                max_index = index
    return max_index 

def insert_pic(file_dir, cla_name, index):
    print('insert_pic enter')
    file_name = cla_name + '.' + str(index + 1) + '.' + 'jpg'
    print(file_name)
    file_full_name = file_dir + file_name
    shutil.copyfile(source_file_full_name, file_full_name)
    return file_full_name

def get_file_cla_name(file_name):
    return cla_name


def get_file_cla_id(file_name):
    return cla_id


'''
index = get_file_index(image_base_dir, 'cat')
print(index)

file_full_name = insert_pic(image_base_dir, 'cat', index)
print(file_full_name)
'''




print('init train_test server');
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('train_image', namespace='/train')
def test_message(message):
    print('socketio train_image enter')
    print(message)
    train1.run_training();
    emit('res', 'ok');

@socketio.on('train_test', namespace='/train')
def test_message(message):
    print('socketio train_test enter')
    print(message)
    index = test1.evaluate_one_image('D:/tensorflow/mydata/cat_dog2/cat.0.jpg')
    print(index)
    emit('res', 'ok');




@socketio.on('cla_train', namespace='/image')
def test_message(message):
    print('socketio cla_image enter')
    print(message)

    #cla_pinyin = pinyin.get(message, format="numerical")
    #print(cla_pinyin)

    #index = get_file_index(image_base_dir, cla_pinyin)
    #print(index)

    cla_pinyin = message;

    index = get_file_index(image_base_dir, message)
    print(index)

    file_full_name = insert_pic(image_base_dir, cla_pinyin, index)
    print(file_full_name)


    train1.run_training();

    #emit('cla_pinyin_res', cla_pinyin);



if __name__ == '__main__':
    socketio.run(app, port=9002)