"""
This is an emulation of TM 11.14 from Intro to The Theory of Computation by Wayne Goddard.
11.14 is consider the following TM with input alphabet {0,1}
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
    previous = False
    while(True): # infinite loop 
        if(node == 1): #If in the first state
            if(tape[index]==1):
                index = index-1 #move left
                node = 2 #Switch to state 2
                previous = True # Used to catch the infinite loop at start
            elif(tape[index]==0):
                previous = False
                tape[index]='$' #set value to $
                index = index+1 #move right
                node = 3 #go to state 3
            elif(tape[index]=='x'):
                print(tape, 'pointer: ' + str(index))
                return True # At accept state
        elif(node == 2): #state 2
            if(tape[index]==1 or tape[index]==0): # if 0 or 1 pointer dies
                print(tape, 'pointer: ' + str(index))
                return False
            elif(tape[index]=='$'): #if $ swap with 0 and move left
                previous = False
                tape[index]=0
                index = index-1
            elif(tape[index]=='x'):#if delta move to the right and to state 1
                if(previous == True):
                    print(tape, 'pointer: ' + str(index))
                    return False
                index = index+1
                node = 1
        elif(node == 3): # state 3
            if(tape[index]==1): #if 1 move right and go to state 4
                previous = False
                index = index+1
                node = 4
            elif(tape[index]==0): #if 0 move right and stay there
                previous = False
                index = index+1
            else: #otherwise delta or $ die
                print(tape, 'pointer: ' + str(index))
                return False
        elif(node == 4): # state 4
            if(tape[index]==1): #if 1 then stay and move right
                previous = False
                index = index+1
            elif(tape[index]=='x'): #if delta than move left and go to state 5
                index = index-1
                node = 5
            else: #otherwise if 0 or $ die
                print(tape, 'pointer: ' + str(index))
                return False
        elif(node == 5): #state 5
            if(tape[index]==1): #if 1 move left and switch to delta also move to state 6
                previous = False
                tape[index] = 'x'
                index = index-1
                node = 6
            else: #all other options die
                print(tape, 'pointer: ' + str(index))
                return False
        elif(node == 6): #state 6
            if(tape[index] == 1): # if 1 stay and move left
                previous = False
                index = index-1
            elif(tape[index] == 0):#if 0 stay and move left
                previous = False
                index = index-1
            elif(tape[index] == '$'): # if $ move left and go to state 1
                previous = False
                index = index+1
                node = 1
            else: #if delta then die
                print(tape, 'pointer: ' + str(index))
                return False

print('What happens to the TM if the first symbol of the input is a 1?')
print(problem('1'))
print('What is the final string if the unput is 0011')
print(problem('0011'))

print('----------------------------------------------------------------')
print('Which 4 symbol strings does the TM accept?')
print('Running tests on all 4 symbol strings')

trueStatements = list()
if(problem('0000') == True):
    trueStatements.append('0000')
if(problem('0001') == True):
    trueStatements.append('0001')
if(problem('0010') == True):
    trueStatements.append('0010')
if(problem('0011') == True):
    trueStatements.append('0011')
if(problem('0100') == True):
    trueStatements.append('0100')
if(problem('0101') == True):
    trueStatements.append('0101')
if(problem('0110') == True):
    trueStatements.append('0110')
if(problem('0111') == True):
    trueStatements.append('0111')
if(problem('1000') == True):
    trueStatements.append('1000')
if(problem('1001') == True):
    trueStatements.append('1001')
if(problem('1010') == True):
    trueStatements.append('1010')
if(problem('1011') == True):
    trueStatements.append('1011')
if(problem('1100') == True):
    trueStatements.append('1100')
if(problem('1101') == True):
    trueStatements.append('1101')
if(problem('1110') == True):
    trueStatements.append('1110')
if(problem('1111') == True):
    trueStatements.append('1111')

print('----------------------------------------------------------------')
print('The 4 symbol strings it accepts are')
print(trueStatements)