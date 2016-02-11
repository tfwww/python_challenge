#!/usr/bin/python3
#-*- coding: utf-8 -*-

from PIL import Image

img = Image.open('./challenge7/oxygen.png')
print(img)

# get the grey area
x_begin = 0
x_end = 609
y_begin = 43
y_end = 54

box = img.crop((x_begin, y_begin, x_end, y_end))
pixels = box.getdata()

# convert mode RGBA to mode L
lBox = box.convert('L')
lPixels = lBox.getdata()

str = []
for i in range(0, 608, 7):
	str.append(chr(lPixels[i]))
	x = lPixels[i]

print(''.join(str))

result = [105, 110, 116, 101, 103, 114, 105, 116, 121]
new_str = []
for i in result:
	new_str.append(chr(i))

print(''.join(new_str))


