# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-30 12:37:36
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-30 13:42:35

url = 'http://blog.kingkk.com/'

from lib.scan import scan

s = []
for i in range(10):
	s.append(scan(url))
for i in s:
	i.start()