#!/usr/bin/python
# -*- coding: utf-8 -*-

import json # import the module of json
import sys # this module is used to get the params from cmd


import pinyin as pinyin



params = sys.argv[1]
#obj = json.loads(params) #str to obj
#print(params)
#ret = my_bot.get_response(params)

ret = pinyin.get(params, format="numerical")
#ret = pinyin.delimiter.join(_pinyin_generator(u(params), format="numerical"))
#print(ret)



#jsonob = {'ret':'lijia'}
jsonob = {'ret':str(ret)}
#print(jsonob)
strjson = json.dumps(jsonob, sort_keys=True)
print(strjson)
#print("aaaaaaaaaaa")
#

#for i in range(len(sys.argv)):
#    print('arg'+str(i),sys.argv[i])



