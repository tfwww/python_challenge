#!/usr/bin/python3
#-*- coding: utf-8 -*-

from urllib import request
import re
import webbrowser

# find the content we need on the page
def find_content(url, pattern):
	content = request.urlopen(url).read()
	decode_content = content.decode('utf8')
	content_found = re.findall(pattern, decode_content, re.S)
	return content_found[0]

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
pattern = r'<!--\n(kA.*)\n-->'
mess = find_content(url, pattern)
# print(mess)

key = r'[^A-Z][A-Z]{3}([a-z]{1})[A-Z]{3}[^A-Z]'
key_found = re.findall(key, mess)
# print(key_found)
answer = ''.join(key_found)
print(answer)

# open the url with correct answer
def open_url(url, var):
	pattern = re.compile(r'/def/(\w*).html')
	url_found = re.findall(pattern, url)
	updated_url = url.replace(url_found[0], var)
	webbrowser.open(updated_url)

open_url(url, answer)