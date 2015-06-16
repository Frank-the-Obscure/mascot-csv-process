# -*- coding: utf-8 -*-
# Author Frank Hu


import re
from sys import argv

# read one hand infomation
script, filename = argv
txt = open(filename)
data = txt.read()

test_info = re.findall('\d+,.*?\n', data)

samplename = re.findall('(?<=Peak list data path,).*',data)[0] # get raw file name in csv
print samplename #test

output = open('%s_extracted.csv'%(filename), 'w')
#print test_info
for i in test_info:
	if re.findall('OS=', i): # use of uniprot-formated file
		output.write(samplename + ',')
		output.write(i)
