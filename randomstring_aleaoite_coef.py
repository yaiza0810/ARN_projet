# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 08:33:46 2022

@author: utilisateur
"""

import random
import time

def randomstring (a, u, c, g, longueur):
    
    start = time.time()
    
    file = "randomstring"
    OUT = open(file, 'a')
    
    string = ""
    liste_nucleotide =[]
    condition = True
    long = longueur
    
    while condition :
    
        if len(liste_nucleotide) < long:
            
            for i in range (round(a*long)):
                        liste_nucleotide.append("A")
            for i in range (round(u*long)):
                        liste_nucleotide.append("U")
            for i in range (round(c*long)):
                        liste_nucleotide.append("C")
            for i in range (round(g*long)):
                        liste_nucleotide.append("G")
    
    
        if len(liste_nucleotide) > long :
            #print('la')
            while len(liste_nucleotide) > long:
                liste_nucleotide = liste_nucleotide[:-1]
                
        if len(liste_nucleotide) == longueur:
            #print("terminaer")
            condition = False
        
        #long = abs(len(liste_nucleotide) - long) 
                    
    random.shuffle(liste_nucleotide)
    string = ''.join(liste_nucleotide)
    
    for i in range(len(string)):
        OUT.write(string[i])
    OUT.write("\n")
    
    end = time.time()
    
    #print(string)
    print(len(string))
    print("temps écoulé = ", end-start)
    
    return string



randomstring(7/23, 6/23, 5/23, 5/23, 1000000)