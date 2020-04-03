"""
This is an emulation of CFG 6.1 from Intro to The Theory of Computation by Wayne Goddard.
6.1 is a CFG for palindromes that allows odd length palindromes
Author: rcasey
"""

#P → aPa | bPb | a | b | ε

from random import randrange

def m6_1():
    result = "P"             
    while "P" in result:     #while there are still productions to be evaluated in our string
        x = randrange(0, 5)  #a random value is generated, this indicates which production will be chosen
        if x == 0:
            result = result.replace("P", "aPa")  #the production is replaced with a valid set of terminals and another production
            continue
        if x == 1:
            result = result.replace("P", "bPb")
            continue
        if x == 2:
            result = result.replace("P", "a")
            continue
        if x == 3:
            result = result.replace("P", "b")
            continue
        if x == 4:
            result = result.replace("P", "")
            continue

    return result

for i in range(10):
    print(m6_1())