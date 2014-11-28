#! /usr/bin/env python
# coding:utf-8
from lib.request_util import *
import time

def check_spider_usecase(info,domain,method,i):
	print "----------------"
#	print i,":",info
	res = check_usecase("/search.php",method,None,{"User-Agent":info},domain)
	
	if res == 200:
		print '\033[1;31;40m'
		print i,":",res,"   usecase:",info
		print '\033[0m'
	else:
		print i,":",res,"   usecase:",info	

def SPIDER_TEST(domain,method,usecase):
	spider_file = open(usecase)
	file_content_lines = spider_file.readlines()
	spider_file.close()
	i = 0
	for line in file_content_lines:
		info = line.strip()
		i+=1
		if info != "":
			check_spider_usecase(info,domain,method,i)
			time.sleep(5)
