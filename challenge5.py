#!/usr/bin/python3
#-*- coding: utf-8 -*-

from urllib import request
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
txt = request.urlopen(url).read().decode('utf8')
# print(txt)

f = open('obj', 'w+')
f.write(txt)
f.close()

f = open('obj', 'rb')
obj = pickle.load(f)
f.close()
# print(obj)

# for item1 in obj:
# 	for item2 in item1:
# 		print(''.join(item2[0]*item2[1]))

for item1 in obj:
	print(''.join(item2[0]*item2[1] for item2 in item1))




