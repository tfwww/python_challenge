#!/usr/bin/python3
#-*- coding: utf-8 -*-

from urllib import request
import re
import webbrowser

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
content = request.urlopen(url).read()
decode_content = content.decode('utf8')
string_found = re.findall(r'<!--\n(%.*)\n-->', decode_content, re.S)
mess = string_found[0]

str_list = []
for i in mess:
	if i.isalpha() == True:
		str_list.append(i)

final_str = ''.join(str_list)
print(final_str)

# open the url with correct answer
def open_url(url, var):
	pattern = re.compile(r'/def/(\w*).html')
	url_found = re.findall(pattern, url)
	updated_url = url.replace(url_found[0], var)
	webbrowser.open(updated_url)

if __name__ == '__main__':
	open_url(url, final_str)
