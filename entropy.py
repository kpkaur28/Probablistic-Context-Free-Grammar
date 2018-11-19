import sys
import numpy

PROBS = sys.argv[1]
sentence_probs = []

with open(PROBS) as probsFile:
    for line in probsFile:

        lineArray = line.split()
        p_of_s = lineArray[1]
        sentence_probs.append(float(p_of_s))

total = 0
for x in sentence_probs:
    total -= numpy.log2(x)

total = total / len(sentence_probs)

print(total)