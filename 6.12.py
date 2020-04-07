"""This program emulates the Context Free Grammar from example 6.10 from the book Intro to Theory of Computation
by Wayne Goddard.  Here a list is used to append the variables transition. The GCF in this case is
S -> BB
B -> SS | c
Instead of trying to max out memory with recursive calls, a bounds k is given for max number of iterations with the base
case being in our list only contains c's.  Assuming in most cases the function terminates by i > k, the print c function
prints the max possible values of c left over by remaining S and B's
author: Timothy Capille"""

# starting list
l = ['S']

# function representation of CFG
def CFG6_10(k):
    i = 0
    while l.count('c') != len(l) and i < k:
        if l.__contains__('S'):
            S(l)
        if l.__contains__('B'):
            B(l)
        i = i + 1
    print_C(l.count('c'))

# S Variable
def S(l):
    l.remove('S')
    l.append('B')
    l.append('B')

# B Variable
def B(l):
    import random
    r = random.uniform(0, 1)
    if r <= 0.5:
        l.append('S')
        l.append('S')
        l.remove('B')
    else:
        z = l.index('B')
        l[z] = 'c'

# prints possible number of c's
def print_C(n):
    c = 'c' * (n + l.count('B') + 2*l.count('S'))
    print(c,len(c))


for i in range(10):
    CFG6_10(i)
