# -*- coding: utf-8 -*-
"""ISC4221_lab2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-nA8NIFFZ1ZQgdV7WRRniqAjzq8gyBFe
"""

# ISC4221 - Lab 2
# by: Andres Candido
# Part 1:

import numpy as np

np.random.seed(1)    # set random number generator seed (turn it into comment if not needed)

print('Enter the number of amino acids:') # we assume the input is in the correct data type (only integers)
n = input()


def generate_random_protein(n):
  protein = ''
  total_nucleotides = int(n)              # input() returns a str, we convert it to an int
  counter = 0

  while counter < total_nucleotides:      # loops until our protein has 3n nucleotides
    codon=''

    for i in range(3):
      num = np.random.randint(0,4)        # generate random numbers from 0 to 3 (4 is excluded)

      if num == 0:
        codon += 'A'
      elif num == 1:
        codon += 'G'
      elif num == 2:
        codon += 'C'
      else:
        codon += 'T'

    if codon=='TAA' or codon=='TAG' or codon=='TGA':      # dont add codon if we generated a stop codon
      protein += ''
    else:                                                 # else add codon to protein and increase codon counter by 1
      protein += codon
      counter += 1

  return protein

protein = generate_random_protein(n)

print('Protein string: ', protein)

# Part 2:

print('Name of amino acid you wish to search occurences in protein:')
name = input()
name = name.lower()                                   # make str lowercase

def frequency_amino_acid(protein, amino_acid):

  if amino_acid == 'isoleucine':                      # all amino acids and their codons
    match = ['ATT','ATC','ATA']
  elif amino_acid == 'leucine':
    match = ['CTT','CTC','CTA','CTG','TTA','TTG']
  elif amino_acid == 'valine':
    match = ['GTT','GTC','GTA','GTG',]
  elif amino_acid == 'phenylalanine':
    match = ['TTT','TTC']
  elif amino_acid == 'methionine':
    match = ['ATG']
  elif amino_acid == 'cysteine':
    match = ['TGT','TGC']
  elif amino_acid == 'alanime':
    match = ['GCT','GCC','GCA','GCG']
  elif amino_acid == 'glycine':
    match = ['GGT','GGC','GGA','GGG']
  elif amino_acid == 'proline':
    match = ['CCT','CCC','CCA','CCG']
  elif amino_acid == 'threonine':
    match = ['ACT','ACC','ACA','ACG']
  elif amino_acid == 'serine':
    match = ['TCT','TCC','TCA','TCG','AGT','AGC']
  elif amino_acid == 'tyrosine':
    match = ['TAT','TAC']
  elif amino_acid == 'tryptophan':
    match = ['TGG']
  elif amino_acid == 'glutamine':
    match = ['CAA','CAG']
  elif amino_acid == 'asparagine':
    match = ['AAT','AAC']
  elif amino_acid == 'histidine':
    match = ['CAT','CAC']
  elif amino_acid == 'glutamic acid':
    match = ['GAA','GAG']
  elif amino_acid == 'aspartic acid':
    match = ['GAT','GAC']
  elif amino_acid == 'lysine':
    match = ['AAA','AAG']
  elif amino_acid == 'arginine':
    match = ['CGT','CGC','CGA','CGG','AGA','AGG']
  else:
    print('Not an amino acid')


  num_items = len(match)                                # get number of codons for an amino acids
  current_item = 0
  prot_len = int( len(protein)/3 )                      # number of amino acids in protein (as an int)
  occurences = 0

  while current_item < num_items:                       # repeat while loop until we find occurences of all items in match
    prot_pos = 0                                        # reset to the start position of protein str

    for i in range(prot_len):                           # loop once for each codon in protein str
      current_amino = protein[prot_pos:prot_pos+3]

      if current_amino == match[current_item]:
        occurences += 1

      prot_pos +=3                                      # move to next codon in protein str,

    current_item += 1                                   # move to next item in match

  return occurences

occurences = frequency_amino_acid(protein, name)
print('Occurences of amino acid',name,'in protein: ',occurences)