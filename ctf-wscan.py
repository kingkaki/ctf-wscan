# -*- coding: utf-8 -*-
# @Author: King kaki
# @Date:   2018-07-30 12:37:36
# @Last Modified by:   kingkk
# @Last Modified time: 2018-08-12 09:58:53

# url = 'http://localhost:80/'
# url = 'http://ctf5.shiyanbar.com/web/'
import sys

from lib.init import Init

def main():
	scan = Init(sys.argv)
	scan.start()

if __name__ == '__main__':
	main()

