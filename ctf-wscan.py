# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-30 12:37:36
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-30 15:46:45

url = 'http://localhost/'

from config import * 
from lib.scan import scan


s = []
for i in range(NUMBER_OF_THREAD):
	s.append(scan(url))
for i in s:
	i.start()