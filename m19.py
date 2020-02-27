"""This is an emulation of the DFA 1.19 from the text Intro to The Theory of Computation by Wayne Goddard
 This was created to illustrate not only the output of the DFA, but the filters applied to help understand
 what this language of this DFA recognizes
 Author: Timothy Capille"""

# Individual states of the DFA.  Each are given an integer value for easy equality checks.
# In this machine state 1 is the only accept state
state_1 = 1
state_2 = 2
state_3 = 3
state_4 = 4

"""Replicates the effects of DFA 1.19. Randrange returns a value of either 0 or 1.  String represents an empty string that we intend
 to build using this DFA. State is the current state of the machine. In each iteration of the loop, a symbol is appended to string and the state changes according to it's transition function.
 Any string that results in the DFA to transition to state1 is appended to the list of results."""

def m1_19():
    import random
    s = state_1
    result = []
    string = ""
    result.append(string)
    for _ in range(50):
        # generate next symbol and add that to our string
        rand = random.randrange(0, 2)
        w = rand
        string = string + str(w)
        # make decisions in accordance with transition function
        if s == state_1:
            if w == 0:
                s = state_2
            else:
                s = state_3
            continue

        if s == state_2:
            if w == 0:
                s = state_1
                result.append(string)
            else:
                s = state_4
            continue

        if s == state_3:
            if w == 0:
                s = state_4
            else:
                s = state_1
                result.append(string)
            continue

        if s == state_4:
            if w == 0:
                s = state_3
            else:
                s = state_2
            continue
    return result

"""This DFA was one of the first machines that I couldn't deduct right off the bat.  To filter possible languages, I created checks to see if certain aspects of the language held true.
 My first thought for this language was all even length strings, but then realized that I could have 0111 and that would not be in the language.  The next check is for an even amount of 0's and 1's, and too held true.
 This is the solution to the exercise."""
def all_even_length(l):
    for x in l:
        if len(x) % 2 != 0:
            return False
    return True
def check1and0(l):
    for x in l:
        if x.count("1") % 2 != 0 and  x.count("0") % 2 != 0:
            return False
    return True

print(m1_19())
print(all_even_length(m1_19()))
print(check1and0(m1_19()))

