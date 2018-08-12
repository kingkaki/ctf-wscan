# -*- coding: utf-8 -*-
# @Author: kingkk
# @Date:   2018-08-11 19:32:38
# @Last Modified by:   kingkk
# @Last Modified time: 2018-08-12 10:27:39
import sys
from config import * 
from lib.log import Log
from lib.scan import Scan

class Init:
	def __init__(self, argv):
		if len(argv) != 2:
			print('Params Error!')
			self.help()
		self.url = str(argv[1])
		self.url = self.init_url(self.url)


	def help(self):
		help = 'Useage : python ctf-wscan.py [website url]\n'
		help+= 'Example: python ctf-wscan.py http://ctf.test.com'
		print(help)
		exit()

	# def args(self):

	def init_url(self, url):
		'''
		处理成标准的url格式
		'''
		if not url.startswith('http'):
			url = 'http://'+url

		if not url.endswith('/'):
			url = url + '/'

		return url

	def start(self):
		threadlist = []
		loglist = {}
		for i in range(NUMBER_OF_THREAD):
			threadlist.append(Scan(self.url, loglist))
		for t in threadlist:
			t.start()
		for t in threadlist:
			t.join()

		if CACHE_LOG:
			log = Log(self.url, loglist)
			log.save()
