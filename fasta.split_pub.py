#! /usr/bin/env python
#debug with python -m pdb myscript.py

"""
Original name: fasta.split3.py
Author: Haw Chuan Lim 
Purpose: Split a concatenated fasta file in component loci based on file stating the following in 3 columns: 
locus name, 
starting position of locus in fasta file (1 = position num in fasta file),
ending position of locus in fasta file

Script will output the same num of fasta file as the number of loci in the split file
Example of split file format

uce1	1	500
uce2	501	600
uce3	600	1466
"""
import re

#set infile name
infilename = raw_input("Enter name of fasta to be split: ")
splitfilename = raw_input("Enter name of file containing locus names and start/end, no header line: ")

#open splitfile
#split file has no headerline
splitfile = open(splitfilename, 'r')

#for each line in the splitfile, cut out the correct part in the fasta file and 
#give the output file name from the 1st column of the splitfile


for line in splitfile:
	line = line.strip('\n')
	ucelist = line.split('\t') #first is uce name, 2nd is start of the uce, 3rd is end of uce. To extract the right starting point, use number in 2nd column minus 1
	ucename = ucelist[0]
	start = int(ucelist[1])-1 #convert to integer, minus one
	end = int(ucelist[2])
		
	#make outfile based on each uce name
	outfilename = ucename + ".fa"
	outfile = open(outfilename, 'w')
	
	#within each line of split file, do the following:
	print ucename, start, end
	
	#do different processing for odd and even lines
	
	infile = open(infilename, 'r')
	linenum = 0
	for line2 in infile:
		print linenum
		
		if linenum%2 == 0: #1st line is line 0, and 0%2 == 0
			line2 = line2.strip('\n')
			sample_name = line2
			#print "The sample name is:", sample_name
			outfile.write(sample_name + "\n")
		else:
			line2 = line2.strip('\n')
			seq = list(line2) #turn string into list
			#print ''.join(seq[start:end]) #this joins the list into string without delimiter in between
			#seq_truncated = seq[start:end]
			seq_truncated = ''.join(seq[start:end])
			outfile.write(seq_truncated + "\n")
						
		linenum = linenum + 1
		
	outfile.close()
	infile.close()
			
splitfile.close()

	

