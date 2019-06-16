#! /usr/bin/env python
#debug with python -m pdb myscript.py

"""
Original name: prune_Q.py
Author: Haw Chuan Lim
Trim your fasta alignments based on the proporiton of unknownn (?) per column
"""

from Bio import AlignIO
import glob
import os

#find all files ending with fasta, the input filename is name
for name in glob.glob('*fasta'):
		
	#output filename. splitext split at ".". Pick first part and add .80.fasta (signifying that you have trimmed away region with 20% or more missing data
	#print name
	outfilename = os.path.splitext(name)[0] + ".80.fasta"
	outfile = open(outfilename, "w")
	

	align = AlignIO.read(open(name),"fasta")

	keep_cols = []
	for i in range(align.get_alignment_length()-1):
		c = align[:,i]
		if c.count('?')<(0.20*len(align)): #keep columns that have less than 20% unknowns
			#print i
			keep_cols.append(i)
	#print keep_cols

	for record in align:
		outfile.write(">%s\n" % record.id)
		outfile.write('%s\n' % ''.join([record.seq[i] for i in keep_cols]))

	outfile.close()