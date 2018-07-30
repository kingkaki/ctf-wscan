# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-30 13:18:58
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-30 16:25:33

import sys
import re
import threading

from config import *
from lib.generatedict import GenerateDcit

import requests


def setting():
	# 获取请求方式
	if REQUEST_METHOD == 1:
		req = requests.head
	elif REQUEST_METHOD == 2:
		req = requests.get

	# 获取默认扫描列表
	with open('dict/default.txt') as f:
		files = f.readlines()
	

	#生成关键字字典
	if KEY_WORDS:
		g = GenerateDcit()
		for i in g.generate():
			files.append(i)


	files = (file.strip() for file in files)

	return req, files

req, files = setting()

class Scan(threading.Thread):
	def __init__(self, url, log):
		threading.Thread.__init__(self)
		self.url = url
		self.log = log

	def run(self):
		for file in files:
			r = req(self.url+file, timeout=TIME_OUT)
			with threading.Lock():
				self.display(r, file)

				
	def display(self, r, file):
		if r.status_code != 403 and r.status_code != 404: 
			print('[{}] => {}{}'.format(r.status_code, file, '\t'*5))
			self.log[file] = r.status_code
		else:
			print('[{}] => {}{}'.format(r.status_code, file, '\t'*5), end='\r')





