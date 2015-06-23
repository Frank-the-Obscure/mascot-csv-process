# -*- coding: utf-8 -*-
# Author Frank Hu


import re

combine = [] #combined protein list

while True:
    filename = input('Please input file name (without ".csv"), input s to finish: ')
    print(filename)
    if filename == "s":
        # end and output
        try:
            output = open('combined.csv', 'w')
        except PermissionError:
            print('permission denied, please close the file to write.')
        else:
            for i in combine:
                output.write(i)
            break            
    else:
        # read file infomation
        try:
            csv = open(filename + '.csv')

        except FileNotFoundError:
            print ('File not found!')
        else:
            print ('enter name ok')
            data = csv.read()
            protein_list = re.findall('\d+,.*?\n', data)

            samplename = re.findall('(?<=Peak list data path,).*',data)[0] # get raw file name in csv line 9
            print(samplename) #test
            for i in protein_list:
                if re.findall('OS=', i): 
                    combine.append(samplename + ',' + i)
            print(len(combine))

