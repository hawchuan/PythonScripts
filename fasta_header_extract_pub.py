#!/usr/bin/env python
"""
Original name: fasta_header_extract.py
Author: Haw Chuan Lim 
Purpose: Extract headers (ie the name after the > symbol) of a multisequence fasta file
"""

fasta1= open('yourfastafile', 'r')

fasta1out = open('fasta1name.out', 'w')

for line in fasta1:
	if line.startswith('>'):
		line = line.strip('\n')
		name = line.split()[0]
		name.replace(">","")

		print name
		fasta1out.write(name + "\n")
		
fasta1out.close()
