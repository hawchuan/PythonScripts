#! /usr/bin/env python
#debug with python -m pdb myscript.py
#make consensus sequences (diplotypes) from 2 haplotype sequences per indiv
#bases in cap; input format = fasta format, 2 sequences per indiv
#eg
#sample1a
#ACCTGC
#sample1b
#ATCTAC
#sample2a
#ATCTAN
#sample2b
#GTCTAN

infilename = raw_input("Enter name of fasta alignment to be made into consensus: ")

#open infile
infile = open(infilename, 'r')
#make outfile

outfilename = infilename + "_cs.fa"
outfile = open(outfilename, 'w')


linenum = 0
for line in infile:

	#print linenum

	if linenum%4 == 0: #if modulus of 4, 0%4 == 0, 4%4 == 0
		line = line.strip('\n')
		sample_name = line
		outfile.write(sample_name + "\n")
		print line
		
	if linenum%4 == 1: #first haplotype
		line = line.strip('\n')
		hap1 = list(line) #turn string into list
		
	if linenum%4 == 3: #second haplotype
		line = line.strip('\n')
		hap2 = list(line) #turn string into list
		#print hap1
		#print hap2
		
		consensus = list()
		for i, hap1_base in enumerate(hap1):
			
			if hap1_base == "A" and hap2[i] == "A":
				consensus.append("A")
			if hap1_base == "G" and hap2[i] == "G":
				consensus.append("G")	
			if hap1_base == "C" and hap2[i] == "C":
				consensus.append("C")
			if hap1_base == "T" and hap2[i] == "T":
				consensus.append("T")
			if hap1_base == "?" and hap2[i] == "?":
				consensus.append("?")
			if hap1_base == "N" and hap2[i] == "N":
				consensus.append("N")
			if (hap1_base == "A" and hap2[i] == "C") or (hap1_base == "C" and hap2[i] == "A"):
				consensus.append("M")
			if (hap1_base == "A" and hap2[i] == "G") or (hap1_base == "G" and hap2[i] == "A"):
				consensus.append("R")
			if (hap1_base == "A" and hap2[i] == "T") or (hap1_base == "T" and hap2[i] == "A"):
				consensus.append("W")
			if (hap1_base == "C" and hap2[i] == "G") or (hap1_base == "G" and hap2[i] == "C"):
				consensus.append("S")
			if (hap1_base == "C" and hap2[i] == "T") or (hap1_base == "T" and hap2[i] == "C"):
				consensus.append("Y")
			if (hap1_base == "G" and hap2[i] == "T") or (hap1_base == "T" and hap2[i] == "G"):
				consensus.append("K")

		print ''.join(consensus)
		outfile.write(''.join(consensus) + "\n")
	linenum = linenum + 1

outfile.close()
infile.close()
	

		
	
