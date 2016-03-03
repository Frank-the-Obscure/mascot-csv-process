# -*- coding: utf-8 -*-
# Author Frank Hu
# mascot csv process v1.1

import os
import re

combine = [] #combined protein list
dir_test = os.getcwd()

print('input dir is: ', dir_test) # may change to input dir in later versions.

number_of_csv = 0 # to get how many files are read by us
for filename in os.listdir(dir_test): # add list
    # print(filename)
    if re.match('F\d+?\.csv', filename): # re to find target mascot files
        number_of_csv += 1
        #print(filename, 'match') # test re
        csv = open(filename)
        data = csv.read()
        protein_list = re.findall('\d+,.*?\n', data)

        samplename = re.findall('(?<=Peak list data path,).*',data)[0] # get raw file name in csv line 9
        #print(samplename) #test of read file name
        for i in protein_list:
            if re.findall('OS=', i): # note that it's only in uniprot format data (with 'OS=' string)
                combine.append(samplename + ',' + i)
        #print(len(combine)) #test of how many lines are appended.

# output to flie
output = open('combined.csv', 'w')
for i in combine: 
    output.write(i)
print('\noutput to "combined.csv".\nread %d files, output %d lines'%(number_of_csv, len(combine)))

'''
while True:
    filename = input('Please input file name (without ".csv"), input s to finish: ')
    print(filename) # log to check input
    if filename == "s":
        # end input and output
        try:
            output = open('combined.csv', 'w')
        except PermissionError:
            print('permission denied, please close the file to write.')
        else:
            for i in combine:
                output.write(i)
            print('output finished. output %d lines'%(len(combine)))
            break            
    else:
        # read file infomation
        try:
            csv = open(filename + '.csv')
            # note: for convience, add .csv for users.
        except FileNotFoundError:
            print ('File not found!')
        else:
            print ('enter name ok')
            data = csv.read()
            protein_list = re.findall('\d+,.*?\n', data)

            samplename = re.findall('(?<=Peak list data path,).*',data)[0] # get raw file name in csv line 9
            print(samplename) #test
            for i in protein_list:
                if re.findall('OS=', i): # note that it's only in uniprot format data (with 'OS=' string)
                    combine.append(samplename + ',' + i)
            print(len(combine))
'''
