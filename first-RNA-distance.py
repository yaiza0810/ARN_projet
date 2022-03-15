# first-RNA.py  # for python 2.7
#
# Python program to generate the inequalities for the ILP 
# formulation for the simple RNA folding problem,
# discussed in Chapter 6, Section 6.1.1.
#

#
import time

start = time.time()
file = "test.lp"
OUT = open(file, 'w')

# Collect information from the user
print("Will you type in the RNA sequence, or read it from file `randomstring'?")

inchoice = input("Type 't' for typed input, 'f' for file. ")
if (inchoice == 't'):
    RNA = input("Write an RNA sequence (using A,U,C,G), and hit return \n")
else:
    IN = open("randomstring", 'r')
    RNA = IN.readline().strip()

print("You input the sequence: %s" % RNA)

length = len(RNA)
minDist = 4

# Generate the objective function

OUT.write("Maximize \n")
for i in range(1, length):
    for j in range(i + 1, length + 1):
        OUT.write("+ P(%d,%d) \n" % (i, j))
OUT.write("such that \n")

# The following segment generates the ILP inequalities to ensure
# that only complementary nucleotides pair.
'''
for i in range(1, length):
    for j in range(i + 1, length + 1):

        if (RNA[i - 1] == 'A') and (RNA[j - 1] != 'U'):
            OUT.write("P(%d,%d) = 0 \n" % (i, j))

        if (RNA[i - 1] == 'U') and (RNA[j - 1] != 'A'):
            OUT.write("P(%d,%d) = 0 \n" % (i, j))

        if (RNA[i - 1] == 'C') and (RNA[j - 1] != 'G'):
            OUT.write("P(%d,%d) = 0 \n" % (i, j))

        if (RNA[i - 1] == 'G') and (RNA[j - 1] != 'C'):
            OUT.write("P(%d,%d) =  0 \n" % (i, j))
'''            
# The following segment generates the ILP equalities to ensure that two positions 
# can not be paired if the distance between them is greater than 4

for i in range(1, length):
    for j in range(i+1, length+1):
        if((j-i) <= minDist):
            OUT.write("P(%d,%d) = 0 \n" % (i,j))

# The following segment generates the ILP inequalities to ensure
# that each position is paired to at most one other position 

for i in range(1, length + 1):
    inequality = ""

    for j in range(1, i):
        inequality = inequality + " + P(%d,%d)" % (j, i)

    for j in range(i + 1, length + 1):
        inequality = inequality + " + P(%d,%d)" % (i, j)

    inequality = inequality + ' <= 1'
    OUT.write(inequality)
    OUT.write("\n")

# The following segment generates the ILP inequalities to ensure
# that no pairs cross.

for h in range(1, length - 2):
    for i in range(h + 1, length - 1):
        for j in range(i + 1, length):
            for k in range(j + 1, length + 1):
                OUT.write("P(%d,%d) + P(%d,%d) <= 1 \n" % (h, j, i, k))
                

# Write out the list of binary variables 
OUT.write("Binary \n")
for i in range(1, length):
    for j in range(i + 1, length + 1):
        OUT.write("P(%d,%d) \n" % (i, j))


OUT.write("end \n")
print("The ILP file is ", file)
print(time.time()-start)
