# -*- coding: utf-8 -*-
# @Author: kingkk
# @Date:   2018-08-11 19:32:38
# @Last Modified by:   kingkk
# @Last Modified time: 2018-08-18 15:58:15
import sys
from config import * 
from lib.log import Log
from lib.scan import Scan
from lib.generatedict import GenerateDcit


class Init:
	def __init__(self, args):	
		self.url = self.init_url(str(args.url))
		self.keywords = args.key_words


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

	def get_files(self):
		# 获取默认扫描列表
		with open('dict/default.txt') as f:
			files = f.readlines()
		

		#生成关键字字典
		if KEY_WORDS or args.KEY_WORDS:
			g = GenerateDcit(self.keywords)
			for i in g.generate():
				files.append(i)


		files = (file.strip() for file in files)
		return files

	def start(self):
		threadlist = []
		loglist = {}
		files = self.get_files()
		for i in range(NUMBER_OF_THREAD):
			threadlist.append(Scan(self.url, loglist, files))
		for t in threadlist:
			t.start()
		for t in threadlist:
			t.join()

		if CACHE_LOG:
			log = Log(self.url, loglist)
			log.save()
