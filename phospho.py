# -*- coding: utf-8 -*-
# Author Frank Hu
# mascot csv process phospho
# added phospho-position in mascot peptide level data
# usage: 
# 导出csv时, 加入 start end 两列信息.
# 修改脚本中的 18(line 19), 27(line 22)为 pep_start 和 pep_var_mod_pos 所在列. 注意此处列号从0开始.
# 输出的文件加上 phospho- 前缀

from sys import argv
import csv
import re

script, csv_file = argv

f2 = open('phospho-' + csv_file, 'w', newline='')
with open(csv_file, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        pep_start = row[18] #pep_start
        if pep_start != 'pep_start':
            for i in row:
                if row.index(i) is 27: # pep_var_mod_pos
                    # print(i, row.index(i))
                    mod_position = re.finditer("[23]", i)
                    for j in mod_position:
                        row.append(str(int(pep_start) + j.start() - 2))
                    for i in row:
                        f2.write('"'+ i + '",')
                    f2.write('\n')
        else:
            for i in row:
                f2.write(i + ',')
            f2.write('phos_position\n')

print('phos_position added as %s.'%('phospho-' + csv_file))