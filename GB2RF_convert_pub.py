#! /usr/bin/env python

"""
Original name: GB2RF_convert4.py
Author: Haw Chuan Lim 
Purpose: Convert names of contigs in a vcf file based on a csv file where each line is:
oldname,newname (no space after comma)
This is useful when contig/scaffold names of a reference genome have been changed (but nothing else is changed)
after submission into RefSeq DB

Example of the csv file
MCBO02000001.1,NW_020340093.1
MCBO02000002.1,NW_020340094.1
MCBO02000003.1,NW_020340095.1
MCBO02000004.1,NW_020340096.1
MCBO02000005.1,NW_020340097.1

Usage: python GB2RF_convert_pub.py -i your_vcf_file; it will output a file called your_vcf_file.replaced
"""

import csv
import os
import sys
import re

flag=0
for arg in sys.argv:
    if flag:
        filename_in = arg
        break
    if arg=="-i":
        flag=1
filename = filename_in.strip('\r')
vcf = open(filename, 'r')


print(vcf.name)
out = open(vcf.name + ".replaced", "w")

csvfile= csv.reader(open("yourfile.csv"))
wordDic = dict(csvfile)

#for key, value in wordDic.items():
#	print(key, value)
	

def multiwordReplace(text, wordDic):
    """
    take a text and replace words that match a key in a dictionary with
    the associated value, return the changed text
    """
    rc = re.compile('|'.join(map(re.escape, wordDic)))
    def translate(match):
        return wordDic[match.group(0)]
    return rc.sub(translate, text)

for line in vcf:
	replace = multiwordReplace(line, wordDic)
	out.write(replace)
	
vcf.close()
out.close()
