"""
This is an emulation of PDA 7.2 from Intro to The Theory of Computation by Wayne Goddard.
This PDA accepts the language {0^n 1^2n}.
Author: rcasey
"""

from collections import deque

state_1 = 1
state_2 = 2
state_3 = 3
state_4 = 4
state_5 = 5

def m7_2(input):
    L = list(input)   #The input string as a list of characters
    pos = 0           #The pos in the string that is being evaluated, does not increase if an Epsilon statement is read
    s = state_1       #The current state
    stack = deque()   #The PDA's stack
    result = False    #The result indicates whether or not out input is accepted by the machine

    #Some code here will appear redundant because of the way the machine is being emulated
    #s will always equal state_1 at this point because the machine always begins in the same start state
    #the length of L is checked, if it is greater than zero the machine advances, if not it stays in state_1, this is how I chose to emulate state_1 being an accept state
    if s == state_1 and len(L) > 0:
        s = state_2
        stack.append('delta')
    
    while pos < len(L):
        if s == state_2:
            if L[pos] == '0':       #if the pointer is in state_2 and the next char to be read is zero
                s = state_3         #the pointer advances to state 3
                stack.append('x')   #a marker is pushed onto the stack
                pos += 1            #position increases so the next char in L is read
                continue
            elif L[pos] == '1' and stack[-1] == 'x':    #stack[-1] is the equivalent of stack.peek()
                s = state_4
                stack.pop()
                pos += 1
                continue
            else:
                break
            continue
        if s == state_3:   #this state does not increment pos because an epsilon function is used here
            s = state_2
            stack.append('x')
            continue
        if s == state_4:
            if L[pos] == '1' and stack[-1] == 'x':
                stack.pop()
                pos += 1
            else:
                break
            continue

    if s == state_4 and stack[-1] == 'delta' and pos == len(L): #if s is in state_4, the top of the stack is 'delta', 
        s = state_5                                             #and every position in our string has been evaluated the pointer advances to state_5
    if s == state_5 or s == state_1:    #states 1&5 are accept states, the pointer can only remain in state_1 if the input string is empty, and can only advance to state_5 if the above criteria is met
        result = True
    return result
            
        
print(m7_2('011'))     #true
print(m7_2('0011'))    #false
print(m7_2('001111'))  #true
print(m7_2('0111'))    #false
