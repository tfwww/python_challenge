#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re

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
		print(content)
		return content
	else:
		updated_file = code[0] + '.txt'
		return findNo(updated_file)


if __name__ == '__main__':
	findNo('90052.txt')