import sys
sys.path.append('..')
import os
import time
import tensorflow as tf
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

from utils import label_map_util
from utils import visualization_utils as vis_util

import json
import socket
import time
import threading

from flask import Flask, render_template
from flask_socketio import SocketIO, emit


max_string = 0
max_val = 0

###timeout = 60 * 10;    
###socket.setdefaulttimeout(timeout);

###s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
###print("socket created");
###s.connect( ("127.0.0.1", 6000) );

###s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
###s.bind(('127.0.0.1', 6600));
###s.listen(1);
###print("tcp sever created");
###sock, addr = s.accept() 








#arr = ["人"， "自行车"，”汽车“， ”摩托车“， ”飞机“， ”巴士“， ”火车“， ”卡车“， ”船“， ”交通灯“
#]；

arr = ["人","自行车","汽车","摩托车","飞机","公共汽车","火车","卡车","船","交通灯",
        "消防栓","12","停车标","停车计时器","长凳","鸟","猫","狗","马","羊",
        "牛","象","熊","斑马","长颈鹿","26","背包","雨伞","29","30",
        "手提包","领带","手提箱","飞盘","滑雪板","单板滑雪","运动球","风筝","棒球棒","棒球手套",
        "滑板","冲浪板","网球拍","瓶子","45","红酒杯","杯子","叉子","刀","勺",
        "碗","香蕉","苹果","三明治","45","橙子","西兰花","胡萝卜","热狗","比萨","甜甜圈",
        "蛋糕","椅子","长椅","盆栽","床","66","餐桌","68","69","厕所",
        "71","电视","笔记本电脑","鼠标","遥控器","键盘","手机","微波炉","烤箱","面包机",
        "水槽","冰箱","83","书","时钟","花瓶","剪刀","泰迪熊","吹风机","牙刷"];



print('program start');

#PATH_TEST_IMAGE = sys.argv[1]
PATH_TO_CKPT = 'D:\\tensorflow\\ssd_mobilenet_v1_coco_11_06_2017\\frozen_inference_graph.pb'
PATH_TO_LABELS = 'D:\\tensorflow\\models\\research\\object_detection\\data\\mscoco_label_map.pbtxt'
NUM_CLASSES = 100
IMAGE_SIZE = (18, 12)

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(
    label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

config = tf.ConfigProto()
config.gpu_options.allow_growth = True

#print("lijia tensor start");





'''
with detection_graph.as_default():
    #with tf.Session(graph=detection_graph, config=config) as sess:
    with tf.Session(graph=detection_graph) as sess:

        ###while True:
            ###print("lijia while start");
            ###data = sock.recv(1024);
            ###print(data);
            ###time.sleep(1);
            ###if data=='exit' or not data:
                ###continue;

            ###start_time = time.time()

            print(time.ctime())
            
            print(PATH_TEST_IMAGE)

            ###if True != os.path.exists(PATH_TEST_IMAGE):
            ###    time.sleep(1);
            ###    continue;

            image = Image.open(PATH_TEST_IMAGE);
            ###image = Image.open("image2.jpg");
            ###print(image);

            image_np = np.array(image).astype(np.uint8)
            image_np_expanded = np.expand_dims(image_np, axis=0)
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
            (boxes, scores, classes, num_detections) = sess.run(
                [boxes, scores, classes, num_detections],
                feed_dict={image_tensor: image_np_expanded})
            #print('{} elapsed time: {:.3f}s'.format(time.ctime(), time.time() - start_time))
            #print(np.squeeze(scores))
            #print(np.squeeze(classes).astype(np.int32))
            a = np.squeeze(classes).astype(np.int32)
            print(a);
            b = np.bincount(a);
            print(b);
            b[1] = 0;
            max = np.argmax(b);
            #print(max);

            #os.remove(PATH_TEST_IMAGE);

            if max < 100:
                max = max.astype("str");
            #print(np.squeeze(boxes))
            #print(num_detections)
            #print(category_index)
            #print(category_index.1)
            #if max < '100':
                ###category_index_json = json.dumps(category_index);
            #print(category_index_json)
            #print('ret=' + category_index_json[max]['name'])
    		
                ###json_dict = json.loads(category_index_json);
                ###print('ret=' + json_dict[max]['name']);
                ###str1 = arr[max];
                ###print(str1);
                ###res = 'ret=' + str1
                ###print(res.encode('utf-8'));
                print('ret='+max);

                ###sock.send("kkkkkkk");
				###emit('res_image', 'aaa');

            else:
                print('ret=0');
                ###sock.send("bbbbbbbbbb");
    		
            #vis_util.visualize_boxes_and_labels_on_image_array(
            #    image_np, np.squeeze(boxes), np.squeeze(classes).astype(np.int32), np.squeeze(scores),
            #    category_index, use_normalized_coordinates=True, line_thickness=8)
            #plt.figure(figsize=IMAGE_SIZE)
            #plt.imshow(image_np)
        ###print("out of while");
'''		
		
def function_new(my_path):
	print("function_new enter");
	with detection_graph.as_default():
		#with tf.Session(graph=detection_graph, config=config) as sess:
		with tf.Session(graph=detection_graph) as sess:

			###while True:
				###print("lijia while start");
				###data = sock.recv(1024);
				###print(data);
				###time.sleep(1);
				###if data=='exit' or not data:
					###continue;

				###start_time = time.time()

				print(time.ctime())
				
				#print(PATH_TEST_IMAGE)

				###if True != os.path.exists(PATH_TEST_IMAGE):
				###    time.sleep(1);
				###    continue;

				#image = Image.open(PATH_TEST_IMAGE);
				#image = Image.open("image2.jpg");
				#print(image);
				print(my_path);
				image = Image.open(my_path);


				image_np = np.array(image).astype(np.uint8)
				image_np_expanded = np.expand_dims(image_np, axis=0)
				image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
				boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
				scores = detection_graph.get_tensor_by_name('detection_scores:0')
				classes = detection_graph.get_tensor_by_name('detection_classes:0')
				num_detections = detection_graph.get_tensor_by_name('num_detections:0')
				(boxes, scores, classes, num_detections) = sess.run(
					[boxes, scores, classes, num_detections],
					feed_dict={image_tensor: image_np_expanded})
				#print('{} elapsed time: {:.3f}s'.format(time.ctime(), time.time() - start_time))
				#print(np.squeeze(scores))
				#print(np.squeeze(classes).astype(np.int32))
				a = np.squeeze(classes).astype(np.int32)
				print(a);
				b = np.bincount(a);
				print(b);
				b[1] = 0;
				max = np.argmax(b);
				#print(max);

				#os.remove(PATH_TEST_IMAGE);

				if max < 100:
					max = max.astype("str");
					max_string = max;
				#print(np.squeeze(boxes))
				#print(num_detections)
				#print(category_index)
				#print(category_index.1)
				#if max < '100':
					###category_index_json = json.dumps(category_index);
				#print(category_index_json)
				#print('ret=' + category_index_json[max]['name'])
				
					###json_dict = json.loads(category_index_json);
					###print('ret=' + json_dict[max]['name']);
					###str1 = arr[max];
					###print(str1);
					###res = 'ret=' + str1
					###print(res.encode('utf-8'));
					print('ret='+max);

					###sock.send("kkkkkkk");
					###emit('res_image', 'aaa');
					emit('image_send_res', max);


				else:
					print('ret=0');
					###sock.send("bbbbbbbbbb");
				
				#vis_util.visualize_boxes_and_labels_on_image_array(
				#    image_np, np.squeeze(boxes), np.squeeze(classes).astype(np.int32), np.squeeze(scores),
				#    category_index, use_normalized_coordinates=True, line_thickness=8)
				#plt.figure(figsize=IMAGE_SIZE)
				#plt.imshow(image_np)
			###print("out of while");


#function_new('image1.jpg');



print('server start');
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
    socketio.run(app)
	
