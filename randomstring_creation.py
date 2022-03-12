import random as rd

file = "randomstring"
OUT = open(file, 'a')

length = int(input("Will you type in the length of a RNA sequence ?\n"))

choice = ['A', 'U', 'C', 'G']

for i in range(length):
    OUT.write(rd.choice(choice))
OUT.write("\n")




