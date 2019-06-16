#! /usr/bin/env python

"""
Original name: length_of_uce.py
Author: Haw Chuan Lim 
Purpose: Find number of variants a locus/contig has within the body of a VCF file (ie below the #CHROM line)
Print a file with locus/contig names and the number of variants found in each
"""

import collections

infilename = raw_input("Enter file name of vcf body: ") #no header line whatsoever

vcf_body = open(infilename, 'r')

locus_list = []

for line in vcf_body:
	line = line.strip('\n')
	locus_name = line.split('\t')[0] #take the first itme (locus name) from str.split
	locus_list.append(locus_name) 


#make list of unique locus names
unique_locus = collections.OrderedDict.fromkeys(locus_list) #make the locus names unique, keep order
unique_locus_list = list(unique_locus) #turn the dictionary into list

#print unique_locus_list

#count how many times elements in locus_list matches unique_locus
outfile = open('num_variants_per_locus.txt', 'w')
ele_num = 0
for unique in unique_locus:
	count = locus_list.count(unique) #count num of times elements in unique_locus match the overall locus_list
	#outstring = unique_locus_list[ele_num], count
	outstring = "%s\t%s" % (unique_locus_list[ele_num], count) #put tab in between the 2 things to be output
	print outstring
	outfile.write(outstring + "\n")
	ele_num = ele_num + 1
	
outfile.close()