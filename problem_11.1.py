"""
This is an emulation of TM 11.1 from Intro to The Theory of Computation by Wayne Goddard.
11.1 is consider the following TM. For each of these strings, show the final tape and say whether the TM accepts it or not
a) 0011
b) 101010
c) 110
d) 00100
Author: wadevanorden
"""

def problem(s):
    tape = list() #Create Tape
    tape.append('x') #Set X's as deltas on tape
    for letter in s:
        tape.append(int(letter)) # Create tape with string and x's
    tape.append('x')

    index = 1 #Start tape on the first number of string
    node = 1 #Have nodes set as states where we start at 1
    while(True): # infinite loop 
        if(node == 1): #If in the first state
            if(tape[index]==1): #If 1, replace with 1 and move to the right and stay in the same state
                index = index+1 #We dont have to replace so we just move to right
            elif(tape[index]==0): #If 0 replace with delta and move to the right
                tape[index] = "x"
                index = index+1
                node = 2
            elif(tape[index]=='x'): #Not stated in graph, but in order for it to be deterministic all states must be covered
                print(tape, 'pointer: ' + str(index))
                return False
        elif(node == 2): # state 2
            if(tape[index]==1): #if 1, replace 1 and move right and stay in the same state
                index = index+1
            elif(tape[index]==0): #if 0 replace with delta and move left and go to state 3
                tape[index] = "x"
                index = index-1
                node = 3
            elif(tape[index]=='x'): #If delta than accept
                print(tape, 'pointer: ' + str(index))
                return True
        elif(node == 3): #state 3
            if(tape[index]==1 or tape[index]==0): #If 0 or 1, move left and replace with the same number
                index = index-1
            elif(tape[index]=='x'): #If delta, move to right and go to state 1
                index = index+1
                node = 1

print('Problem A 0011 = ')
print(problem('0011'))
print('Problem B 101010 = ')
print(problem('101010'))
print('Problem C 110 = ')
print(problem('110'))
print('Problem D 00100 = ')
print(problem('00100'))