"""
This is an emulation of CFG 6.2 from Intro to The Theory of Computation by Wayne Goddard.
6.2 is a CFG for the language of binary strings in the form 0^n 1^2n
Author: rcasey
"""

#S → 0S11 | ε

from random import randrange

def m6_2():
    result = "S"
    while "S" in result:
        x = randrange(0, 2)
        if x == 0:
            result = result.replace("S", "0S11")
            continue
        if x == 1:
            result = result.replace("S", "")
            continue

    return result

for i in range(10):
    print(m6_2())