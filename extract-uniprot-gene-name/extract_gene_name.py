# Extract gene name
# Author Frank Hu (Frank-the-Obscure @ GitHub)
# Extract gene name from a uniprot export file (.tab format)
# 从 Uniprot 导出的.tab 文件中提取基因名对照信息
# input: .tab file from Uniprot
# process: extract gene names, sort them, and export them
# output: two .csv files of gene names and protein informations


import re
from sys import argv

script, input_filename = argv

input_file = open(input_filename)

output_csv = open(input_filename + '.csv','w', encoding='utf-8')
output_gene = open(input_filename + 'gene.csv','w', encoding='utf-8')

t = re.compile('\t')
b = re.compile(' ') #gene names are separated by space

# write first line
output_gene.write('Gene, Gene name alias\n')
output_csv.write('Uniprot entry, Entry name, Protein names, Gene, Gene name alias\n')

i = 0
for line in input_file:
    entry = t.split(line)
    gene_name = b.split(entry[4]) #gene names
    alias = []
    gene = 0
    for name in gene_name: #get gene name of SAUSA300_xxxx and alias
        if re.match('SAUSA300', name):
            gene = name
        else:
            alias.append(name)
    if gene: #not first line
        csv = [entry[0], entry[1], entry[3], gene, ' '.join(alias)]
            # entry, entry name, protein names, gene, gene name alias
        gene = gene + ',' + ' '.join(alias) + '\n'
        output_gene.write(gene)
        output_csv.write(','.join(csv) + '\n')
        i += 1

print('Extract finished:', i, 'proteins extrated.')
