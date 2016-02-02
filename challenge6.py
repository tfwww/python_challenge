#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import zipfile

# find the numbers in the files
def findNo(filename):
	keyword = r'\d+'
	f = open('channel/'+filename, 'rb')
	content = f.read()
	decode_content = content.decode('utf8')
	code = re.findall(keyword, decode_content, re.S)
	f.close()
	# if no numbers in the file, return
	if code == []:
		print(content.decode('utf8'))
		return content
	else:
		updated_file = code[0] + '.txt'
		# print(code[0])
		return findNo(updated_file)


zfile = zipfile.ZipFile('channel.zip', 'r')
# print(zfile.namelist())
# print(zfile.getinfo('63643.txt').comment)

comments = []	# store the comment in comments
def collectComments(filename):
	content = zfile.read(filename)
	decode_content = content.decode('utf8')
	keyword = r'\d+'
	number = re.findall(keyword, decode_content, re.S)
	comment = zfile.getinfo(filename).comment.decode('utf8')
	comments.append(comment)
	print(comment)
	while number != []:
		return collectComments(number[0]+'.txt')


if __name__ == '__main__':
	findNo('90052.txt')
	collectComments('90052.txt')
	print(''.join(comments))



