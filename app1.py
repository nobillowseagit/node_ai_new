import os
import shutil  

image_base_dir = 'd:/tensorflow/mydata/cat_dog2/'
source_file_full_name = 'd:/node/node_ai_new/image1.jpg'


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



index = get_file_index(image_base_dir, 'cat')
print(index)

file_full_name = insert_pic(image_base_dir, 'cat', index)
print(file_full_name)
