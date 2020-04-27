"""
This is an emulation of PDA 7.15 from Intro to The Theory of Computation by Wayne Goddard.
7.15 is a construct a PDA for the language of Exercise 6.7
6.7 is give a CFG for the complement of {0^n1^n:n>=0}
Author: wadevanorden
"""



def problem(s):
    stack = list() #stack for 
    if(s == ''): #{0^n1^n:n>=0} accepts the empty string so the compliment does not
        return False
    if(int(s[0]) == 1): #If it starts with 1 then it doesnt matter what follows because its a compliment
        return True
    position = 1
    stack.append('delta') # push delta marker
    for letter in s: #Takes the string of numbers 1 at a time
        number = int(letter) #Converts to number
        if(number == 0):
            stack.append('x') #push x onto stack to keep track of 0's
            position=position+1 # keeps track of position in string
        if(number == 1): #if reading 1 pop x
            stack.pop()
            if(stack[-1] == 'delta'): #if delta is the only thing left in stack, visit it
                if(position == len(s)): #if at the end of the string then the string cant be right
                    return False
                if(position<len(s)): #if theres more to the string then anything after will be accepted 
                    return True
            else:
                position=position+1 # no delta is read increase position for reading 1
    return True

print(problem('01'))
print(problem('0011'))
print(problem('001'))
print(problem('0111'))
print(problem('0101'))
print(problem('101'))


        


