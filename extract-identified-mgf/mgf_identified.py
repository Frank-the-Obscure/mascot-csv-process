# -*- coding: utf-8 -*-
# Author Frank Hu
# select and copy identified peaks to a new mgf file.
# input: directory of mgf files / cleaned query list / output file name
# output: a new mgf file of identified peaks
# 提取 mgf 文件中的特定谱图(通过 csv 文件), 并生成一个新的 mgf 文件.

import os
from sys import argv
import re

script, directory, csv = argv

identified = open(csv).read() # 从整理后的csv生成鉴定到的queries列表

identified_peaks = []
for line in open(csv):
    identified_peaks.append(line[:-1])
print('total identifed peaks: ', len(identified_peaks))

output = open('identfied.mgf','w') # add new name for new mgf file

for mgf in os.listdir(directory):
    if not re.find('mgf', mgf):
        continue

    s = open(mgf).read()

    queries = {}

    match = re.compile('BEGIN IONS.*?END IONS\n', re.DOTALL)

    peak_list = re.findall(match, s) #生成queries的列表

    print('total MS/MS spectra: ', len(peak_list))

    for query in peak_list:
        title = re.search('TITLE=.*? ', query) # 从表中提取title行
        #print(title.group()[6:])
        queries[title.group()[6:-1]] = query


    for peak in identified_peaks:
        if peak in queries:
            output.write(queries[peak]) # 输出鉴定到的mgf文件
            output.write('\n')