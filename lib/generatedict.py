# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-30 14:24:51
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-30 15:08:32

from config import *

import re

class GenerateDcit:
	def __init__(self):
		self.exts = self._getexts()
		self.keywords = KEY_WORDS


	def _getexts(self):
		with open('dict/ext.txt', 'r') as f:
			exts = f.readlines()
		return [ext.strip() for ext in exts]

	def generate(self):
		for e in self.exts:
			for kw in self.keywords:
				yield e.replace('$',kw)



