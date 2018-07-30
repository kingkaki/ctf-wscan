# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-30 16:06:30
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-30 21:19:08

from datetime import datetime
import re
from config import *
class Log:
	def __init__(self, url, log):
		self.url = url
		self.filename = self._getname(self.url)
		self.log = log


	def save(self):
		print('output at {}'.format(self.filename))
		with open('output/{}'.format(self.filename), 'w+') as f:
			f.write('{}{}{}\n'.format('*'*10, datetime.now(), '*'*10) )
			f.write('{}TARGET : {}{}\n'.format('*'*10, self.url, '*'*10))
			f.write('\n')
			f.write('{}SETTING{}\n'.format('*'*10, '*'*10))
			f.write('NUMBER_OF_THRED => {}\n'.format(NUMBER_OF_THREAD))
			f.write('KEY_WORDS => {}\n'.format(KEY_WORDS))
			f.write('\n')
			f.write('{}RESULT{}\n'.format('*'*10, '*'*10))

			for file, status_code in self.log.items():
				
				f.write('[{}] => {}\n'.format(status_code, file))

	def _getname(self, url):
		r =  re.match(r'http[s]?://([\\\.\w\d:/]+)/', url).group(1)
		r = r.replace(':','-')
		r = r.replace('/','-')
		r = r.replace('\\','-')
		return r+'.txt'











