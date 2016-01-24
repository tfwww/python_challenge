#!/usr/bin/python3
#-*- coding: utf-8 -*-

from urllib import request
import webbrowser

url = 'http://www.pythonchallenge.com/pc/def/0.html'

string = repr(2**38)
print(string)
updated_url = url.replace('0', string)
print(updated_url)
webbrowser.open(updated_url)