"""
This is an emulation of PDA 7.3 from Intro to The Theory of Computation by Wayne Goddard.
This PDA accepts the language {0^n 1 0^n}.
Author: rcasey
"""

from collections import deque

state_1 = 1
state_2 = 2
state_3 = 3
state_4 = 4

def m7_3(input):
    L = list(input)    #The input string as a list of characters
    pos = 0            #The pos in the string that is being evaluated
    s = state_1        #The current state
    stack = deque()    #The PDA's stack
    result = False     #The result indicates whether or not out input is accepted by the machine

    if s == state_1:
        s = state_2
        stack.append('delta')

    while pos < len(L):
        if s == state_2:
            if L[pos] == '0':      #if the pointer is in state_2 and the next symbol read is a zero
                                   #the pointer remains in state_2
                stack.append('x')  #a marker is pushed onto the stack
                pos += 1           #position increases so the next symbol is read
                continue
            elif L[pos] == '1':
                s = state_3
                pos += 1
                continue
        if s == state_3:
            if L[pos] == '0' and stack[-1] == 'x':  #stack[-1] is equivalent to stack.peek()
                #pointer remains in state_3
                stack.pop()
                pos += 1
                continue
            else: 
                break
    if s == state_3 and stack[-1] == 'delta' and pos == len(L):  #if s is in state_3, the top of the stack is 'delta',
        s = state_4                                              #and every position in our string has been evaluated the pointer advances to state_4
    if s == state_4:   #state_4 is the accept state
        result = True
    return result

print(m7_3('010'))   #true
print(m7_3('1'))     #true
print(m7_3('00100')) #true
print(m7_3(''))      #false
print(m7_3('00'))    #false
print(m7_3('0100'))  #false
print(m7_3('0010'))  #false
