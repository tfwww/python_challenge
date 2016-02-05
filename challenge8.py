#!/usr/bin/python3
#-*- coding: utf-8 -*-

from urllib import request
import re
import bz2

url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
content = request.urlopen(url).read()
decoded_content = content.decode('utf-8')
# print(decoded_content)

keyword = r"<!--\nun: '(.*)'\npw: '(.*)'\n-->"
# keyword = re.compile(b"<!--\nun: '(.*)'\npw: '(.*)'\n-->")
codes = re.findall(keyword, decoded_content)
# print(codes)

name = codes[0][0]
password = codes[0][1]
print(name)
print(password)

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
print(bz2.decompress(un))
print(bz2.decompress(pw))