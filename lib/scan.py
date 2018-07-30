# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-30 13:18:58
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-30 13:49:48

import sys
import re
import threading
sys.path.append('../')

from config import *

import requests


def setting():
	# 获取请求方式
	if REQUEST_METHOD == 1:
		req = requests.head
	elif REQUEST_METHOD == 2:
		req = requests.get

	# 获取扫描列表
	with open('dict/default.txt') as f:
		files = f.readlines()
	files = (file.strip() for file in files)
	
	return req, files

req, files = setting()

class scan(threading.Thread):
	def __init__(self, url):
		threading.Thread.__init__(self)
		self.url = url

	def run(self):
		# global files
		for file in files:
			r = req(self.url+file)
			print(r.status_code, file,threading.current_thread())


