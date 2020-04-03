"""
This is an emulation of PDA 7.4 from Intro to The Theory of Computation by Wayne Goddard.
This PDA accepts the language {w # reverse(w)}, strings that are palindromes with # as the middle symbol.
Author: rcasey
"""

from collections import deque

state_1 = 1
state_2 = 2
state_3 = 3
state_4 = 4

def m7_4(input):
    L = list(input)   #The input string as a list of characters
    pos = 0           #The pos in the string that is being evaluated, does not increase if an Epsilon statement is read
    s = state_1       #The current state
    stack = deque()   #The PDA's stack
    result = False    #The result indicates whether or not out input is accepted by the machine

    if s == state_1:
        s = state_2
        stack.append('delta')

    while pos < len(L):
        if s == state_2:
            if L[pos] == '0':       #if the pointer in in state_2 and the next symbol read is a zero
                stack.append('0')   #the pointer remains in state_2 and a 0 marker is pushed onto the stack
                pos += 1            #position increases so the next symbol is read
                continue
            elif L[pos] == '1':    #if the machine read a one a 1 marker is pushed onto the stack
                stack.append('1')
                pos += 1
                continue
            elif L[pos] == '#':
                s = state_3
                pos += 1
                continue
        if s == state_3:
            if L[pos] == '0' and stack[-1] == '0':   #stack[-1] is equivalent to stack.peek()
                stack.pop()                          #if a 0 is read a 0 marker is removed from the stack
                pos += 1
                continue
            elif L[pos] == '1' and stack[-1] == '1':
                stack.pop()                          #if a 1 is read a 1 marker is removed from the stack
                pos += 1
                continue
            else:
                break
    if s == state_3 and stack[-1] == 'delta' and pos == len(L):  #if s is in state_3, the top of the stack is 'delta
        s = state_4                                              #and every position in our string has been evaluated the pointer advances to state_4
    if s == state_4:       #state_4 is the accept state
        result = True
    return result

print(m7_4('01#10'))     #true
print(m7_4('101#101'))   #true
print(m7_4('0110#0110')) #true
print(m7_4('#'))         #true
print(m7_4('0110'))      #false
print(m7_4('01#110'))    #false
print(m7_4('001#10'))    #false
print(m7_4('011#101'))   #false

            