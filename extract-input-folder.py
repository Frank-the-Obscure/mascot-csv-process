# -*- coding: utf-8 -*-
# Author Frank Hu
# mascot csv process v1.5
# import all csv files in a folder

import os
import re

combine = [] #combined protein list

dir_input = input('Please input folder path(e.g. D:\Study\Inbox): ')
print('input directory is: ', dir_input) 

number_of_csv = 0 # to get how many files are read by us
for filename in os.listdir(dir_input): # add list
    # print(filename)
    if re.match('F\d+?\.csv', filename): # re to find target mascot files
        number_of_csv += 1
        #print(filename, 'match') # test re
        csv = open(dir_input + '\\' + filename)
        data = csv.read()
        protein_list = re.findall('\d+,.*?\n', data)

        samplename = re.findall('(?<=Peak list data path,).*',data)[0] # get raw file name in csv line 9
        #print(samplename) #test of read file name
        for i in protein_list:
            if re.findall('OS=', i): # note that it's only in uniprot format data (with 'OS=' string)
                combine.append(samplename + ',' + i)
        #print(len(combine)) #test of how many lines are appended.

# output to flie
output = open(dir_input + '\\combined.csv', 'w') # output to dir_input with "combined.csv"
for i in combine: 
    output.write(i)
print('\noutput to "combined.csv".\nread %d files, output %d lines'%(number_of_csv, len(combine)))

