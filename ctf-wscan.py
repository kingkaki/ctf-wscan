# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-30 12:37:36
# @Last Modified by:   King kaki
# @Last Modified time: 2018-07-30 19:34:14

url = 'http://localhost:80/'

from config import * 
from lib.scan import Scan
from lib.log import Log


def main():
	s = []
	loglist = {}
	for i in range(NUMBER_OF_THREAD):
		s.append(Scan(url, loglist))
	for i in s:
		i.start()
	for i in s:
		i.join()

	# print(loglist)
	if CACHE_LOG:
		log = Log(url, loglist)
		log.save()



if __name__ == '__main__':
	main()

