#!/usr/bin/python
# -*- coding: utf-8 -*-

import json # import the module of json
import sys # this module is used to get the params from cmd

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer 
 
my_bot = ChatBot("Training demo")

#my_bot.set_trainer(ChatterBotCorpusTrainer)
#my_bot.train("chatterbot.corpus.chinese")

'''
my_bot.set_trainer(ListTrainer)
my_bot.train([
    "嗳，渡边君，真喜欢我?",
    "那还用说?",
    
    "那么，可依得我两件事?",
    "三件也依得",
    
    "你好",
    "你也好",

    "美女，女孩，二十岁",
    "年轻真好，你真美",

    "妇女，三十岁",
    "你看着像二十多岁的",

    "介绍，女人，认识",
    "真是荣幸，今天又认识个美女",
    
    "我不好",
    "怎么啦"
])
'''

aaa = [    
    "天气",
    "今天天气不错"
    ]
#my_bot.set_trainer(ListTrainer)
#my_bot.train(aaa)

# test
#print(my_bot.get_response("真喜欢我?"))
#print(my_bot.get_response("可依得我两件事?"))

#ret = my_bot.get_response("我不好")




# 开始对话
'''
while True:
    print(my_bot.get_response(input(">")))
'''
    



#for i in range(len(sys.argv)):
#    print('arg'+str(i),sys.argv[i])

params = sys.argv[1]
#obj = json.loads(params) #str to obj
#print(params)
ret = my_bot.get_response(params)

#jsonob = {'ret':'lijia'}
jsonob = {'ret':str(ret)}
#print(jsonob)
strjson = json.dumps(jsonob,sort_keys=True)
print(strjson)
#print("aaaaaaaaaaa")
#

#for i in range(len(sys.argv)):
#    print('arg'+str(i),sys.argv[i])



