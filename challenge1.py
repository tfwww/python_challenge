#!/usr/bin/python3
#-*- coding: utf-8 -*-

from urllib import request
import webbrowser
import re

url = 'http://www.pythonchallenge.com/pc/def/map.html'
content = request.urlopen(url).read()
decode_content = content.decode('utf8')

pattern = re.compile(r'g fmnc.*spj.')
string_found = re.findall(pattern, decode_content)
# print('before:\n' + string_found[0])

# a => c, c => e
def convert_two(letter):
	if letter == 'y':
		# print(' ')
		return 'a'

	elif letter == 'z':
		return 'b'

	else:
		# print(chr(ord(letter)+2))
		return chr(ord(letter)+2)

characters = [chr(i) for i in range(97, 123)] # 26 letters
cha_str = ''.join(characters) # convert list to str
print(cha_str)

r = map(convert_two, characters)
con_str = ''.join(list(r))  #convert list to str
print(con_str)

trantab = str.maketrans(cha_str, con_str)
print(string_found[0].translate(trantab))

# get the 'map' str in the url
pattern = re.compile(r'/def/(\w{3}).html')
url_found = re.findall(pattern, url)
print(url_found[0])

print(url_found[0].translate(trantab))
updated_url = url.replace(url_found[0], url_found[0].translate(trantab))
print(updated_url)
webbrowser.open(updated_url)
