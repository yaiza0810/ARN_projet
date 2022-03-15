
'''chaine aléatoire sans coefficient
import random as rd

file = "randomstring"
OUT = open(file, 'a')

length = int(input("Will you type in the length of a RNA sequence ?\n"))

choice = ['A', 'U', 'C', 'G']

for i in range(length):
    OUT.write(rd.choice(choice))
OUT.write("\n")

'''

''' chaine aléatoire avec coefficient '''

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 08:33:46 2022

@author: utilisateur
"""

import numpy as np
import random


def randomstring (a, u, c, g, longueur):
    
    file = "randomstring"
    OUT = open(file, 'a')
    string = ""
    liste_nucleotide =[]
    for i in range (round(a*longueur)):
        liste_nucleotide.append("A")
    for i in range (round(u*longueur)):
        liste_nucleotide.append("U")
    for i in range (round(c*longueur)):
        liste_nucleotide.append("C")
    for i in range (round(g*longueur)):
        liste_nucleotide.append("G")
    random.shuffle(liste_nucleotide)
            
    string = ''.join(liste_nucleotide)
    
    if len(string) > longueur :
        while len(string) > longueur:
            string = string[:-1]
    elif len(string) < longueur :
        while len(string) < longueur :
            string = string + random.choice(['A','C','U','G'])

    for i in range(len(string)):
        OUT.write(string[i])
    OUT.write("\n")
    return string



randomstring(7/23, 6/23, 5/23, 5/23, 3000)


