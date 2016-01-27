#!/usr/bin/python3
#-*- coding: utf-8 -*-

from urllib import request
import re
import webbrowser

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=65520'


def changeurl(url):
	url_sample = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
	webcontent = request.urlopen(url).read()
	decode_web = webcontent.decode('utf8')
	pattern = r'and the next nothing is (\d+)'
	code = re.findall(pattern, decode_web, re.S)
	if code == []:
		print(url)
		return url
	url_updated = url_sample + code[0]
	# webbrowser.open(url_updated)
	print(url_updated)
	return changeurl(url_updated)

last_url = changeurl(url)
print(last_url)

# get the code number in the url
pattern = r'ht.*(\d{5})'
code = re.findall(pattern, last_url, re.S)
print(code)
print(code[0])

# divide the code number
new_code = int(int(code[0])/2)
print(new_code)

# get the new url
new_url = last_url.replace(code[0], str(new_code))
print(new_url)
webbrowser.open(new_url)

final_url = changeurl(new_url)
final_code = re.findall(pattern, final_url, re.S)
final_url_1 = final_url.replace(final_code[0], 'peak.html')
webbrowser.open(final_url_1)




