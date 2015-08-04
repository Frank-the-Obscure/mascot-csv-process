# -*- coding: utf-8 -*-
# Author Frank Hu
# mascot csv process phospho
# added phospho-position in mascot peptide level data
# usage: 
# 导出csv时, 加入 start end 两列信息. 其余各行默认参数不变(否则需修改各个参数的列号)
# 修改脚本中的 18(line 19), 27(line 22)为 pep_start 和 pep_var_mod_pos 所在列. 注意此处列号从0开始.
# 输出的文件将加上 phospho- 前缀

from sys import argv
import csv
import re

script, csv_file = argv

with open(csv_file, newline='') as f:
    reader = csv.reader(f)
    f2 = open('phospho-' + csv_file, 'w', newline='')

    lines = 0 # 处理的行数记录
    site_list = [] # 位点信息列表, 用于输出最后的位点总数

    for row in reader: #对于每一行
        lines += 1 #记录处理的行数, 用于输出
        pep_start = row[18] #row[18]-第19列, pep_start 即肽段的第一个氨基酸所在位置, 用于计算磷酸化位点的位置
        if pep_start != 'pep_start': # 第一行
            i = 0
            while i < len(row):           
                if i is 27: # pep_var_mod_pos
                    mod_position = re.finditer("[23]", row[i]) #1. 寻找磷酸化位点(2,3)
                    for j in mod_position: #2. 把位点加入row list
                        site = row[1] + '-' + str(int(pep_start) + j.start() - 2) # row[1] (第二列, accession) + 修饰位点
                        if site not in site_list:
                            site_list.append(site)
                        row.append(site) 
                    for k in row: #3. 写入csv信息
                        f2.write('"'+ k + '",')
                    f2.write('\n')
                i += 1
        else:
            for i in row:
                f2.write(i + ',')
            f2.write('phos_position\n')

print('phos_position added as %s., %d lines in total, %d sites in total'
    %('phospho-' + csv_file, lines, len(site_list)))