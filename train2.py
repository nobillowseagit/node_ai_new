    #By @Kevin Xu  
#kevin28520@gmail.com  
#Youtube: https://www.youtube.com/channel/UCVCSn4qQXTDAtGWpWAe4Plw  
#  
#The aim of this project is to use TensorFlow to process our own data.  
#    - input_data.py:  read in data and generate batches  
#    - model: build the model architecture  
#    - training: train  
  
  
# I used Ubuntu with Python 3.5, TensorFlow 1.0*, other OS should also be good.  
# With current settings, 10000 traing steps needed 50 minutes on my laptop.  
  
  
# data: cats vs. dogs from Kaggle  
# Download link: https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/data  
# data size: ~540M  
  
  
# How to run?  
# 1. run the training.py once  
# 2. call the run_training() in the console to train the model.  
  
  
# Note:   
# it is suggested to restart your kenel to train the model multiple times   
#(in order to clear all the variables in the memory)  
# Otherwise errors may occur: conv1/weights/biases already exist......  
  
  
  
  
#%%  
  
  
import os  
import numpy as np  
import tensorflow as tf  
import input_data1 as input_data     
import model1 as model
  
  
#%%  
  
  
N_CLASSES = 2  
#N_CLASSES = 1
IMG_W = 208  # resize the image, if the input image is too large, training will be very slow.  
IMG_H = 208  
#BATCH_SIZE = 10  
BATCH_SIZE = 2  
#CAPACITY = 2000  
CAPACITY = 256  
MAX_STEP = 50 # with current parameters, it is suggested to use MAX_STEP>10k  
learning_rate = 0.0001 # with current parameters, it is suggested to use learning rate<0.0001

cnt_summary = 10
cnt_cache = 50
  
  
  
  
#%%  
def run_training():  
      
    # you need to change the directories to yours.  
    #train_dir = '/home/kevin/tensorflow/cats_vs_dogs/data/train/'  
    train_dir = 'D:/tensorflow/mydata/cat_dog2/'   #My dir--20170727-csq  
    #logs_train_dir = '/home/kevin/tensorflow/cats_vs_dogs/logs/train/'  
    logs_train_dir = 'D:/tensorflow/mylog/cat_dog2/'  
    train, train_label = input_data.get_files(train_dir)
    print(train)
    print(train_label)  
      
    train_batch, train_label_batch = input_data.get_batch(train,  
                                                          train_label,  
                                                          IMG_W,  
                                                          IMG_H,  
                                                          BATCH_SIZE,   
                                                          CAPACITY)
    print(train_batch)
    print(train_label_batch)

    train_logits = model.inference(train_batch, BATCH_SIZE, N_CLASSES)  
    train_loss = model.losses(train_logits, train_label_batch)          
    train_op = model.trainning(train_loss, learning_rate)  
    train__acc = model.evaluation(train_logits, train_label_batch)  
         
    summary_op = tf.summary.merge_all()
    print(summary_op)

    with tf.Session() as sess:
        train_writer = tf.summary.FileWriter(logs_train_dir, sess.graph)  
        saver = tf.train.Saver()  
          
        sess.run(tf.global_variables_initializer())  
        coord = tf.train.Coordinator()  
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)  
          
        try:  
            for step in np.arange(MAX_STEP):
                print(step)
                
                if coord.should_stop():  
                        break  
                _, tra_loss, tra_acc = sess.run([train_op, train_loss, train__acc])  
                     
                if step % cnt_summary == 0:  
                    print('Step %d, train loss = %.2f, train accuracy = %.2f%%' %(step, tra_loss, tra_acc*100.0))  
                    summary_str = sess.run(summary_op)  
                    train_writer.add_summary(summary_str, step)  
                  
                if step % cnt_cache == 0 or (step + 1) == MAX_STEP:  
                    checkpoint_path = os.path.join(logs_train_dir, 'model.ckpt')  
                    saver.save(sess, checkpoint_path, global_step=step)  
                      
        except tf.errors.OutOfRangeError:  
            print('Done training -- epoch limit reached')  
        finally:  
            coord.request_stop()  
              
        coord.join(threads)  
        sess.close()  
      
  
  
#%% Evaluate one image  
# when training, comment the following codes.  
  
  
  
  
from PIL import Image  
import matplotlib.pyplot as plt  
  
  
def get_one_image(train):  
    '''''Randomly pick one image from training data 
    Return: ndarray 
    '''  
    
    print('get_one_image enter')

    n = len(train)
    print(n)  
    ind = np.random.randint(0, n)  
    img_dir = train[ind]  
  
  
    image = Image.open(img_dir)  
    plt.imshow(image)  
    image = image.resize([208, 208])  
    image = np.array(image)  
    return image  
  
  

def get_one_image1(img_dir):  
    '''''Randomly pick one image from training data 
    Return: ndarray 
    '''  
    
    print('get_one_image1 enter')
  
    image = Image.open(img_dir)  
    plt.imshow(image)  
    image = image.resize([208, 208])  
    image = np.array(image)  
    return image 



def evaluate_one_image():  
    '''''Test one image against the saved models and parameters 
    '''  

    print('evaluate_one_image enter')
      
    # you need to change the directories to yours.  
    #train_dir = '/home/kevin/tensorflow/cats_vs_dogs/data/train/'  
    train_dir = 'D:/tensorflow/mypic/cat.2.jpg'  
    #train, train_label = input_data.get_files(train_dir)  
    #image_array = get_one_image(train)
    image_array = get_one_image1(train_dir)
    print(image_array)  
      
    with tf.Graph().as_default():  
        BATCH_SIZE = 2  
        N_CLASSES = 2  
          
        image = tf.cast(image_array, tf.float32)  
        image = tf.image.per_image_standardization(image)  
        image = tf.reshape(image, [1, 208, 208, 3])  
        logit = model.inference(image, BATCH_SIZE, N_CLASSES)  
          
        logit = tf.nn.softmax(logit)  
          
        x = tf.placeholder(tf.float32, shape=[208, 208, 3])  
          
        # you need to change the directories to yours.  
        #logs_train_dir = '/home/kevin/tensorflow/cats_vs_dogs/logs/train/'   
        logs_train_dir = 'D:/tensorflow/mylog/cat_dog2/'   
                         
        saver = tf.train.Saver()  
          
        with tf.Session() as sess:  
              
            print("Reading checkpoints...")  
            ckpt = tf.train.get_checkpoint_state(logs_train_dir)  
            if ckpt and ckpt.model_checkpoint_path:  
                global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]  
                saver.restore(sess, ckpt.model_checkpoint_path)  
                print('Loading success, global_step is %s' % global_step)  
            else:  
                print('No checkpoint file found')  
              
            prediction = sess.run(logit, feed_dict={x: image_array})  
            max_index = np.argmax(prediction)  
            if max_index==0:  
                print('This is a cat with possibility %.6f' %prediction[:, 0])  
            else:  
                print('This is a dog with possibility %.6f' %prediction[:, 1])  
  
#%%  

run_training()
#evaluate_one_image()