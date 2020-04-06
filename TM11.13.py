"""This is an emulation of Turing Machine 3.13 from Wayne Goddard: Intro to Theory of Computation.  This program
uses a list and an index to act as the head and the tape of a TM.  This function allows for a parameter string, and
tests whether it is accepted by the TM. The use of the symbol $ is used instead of delta.  Every time an action
occurs within the machine the head (index) and tape is printed allowing the user to follow along with the steps
that the TM makes
author : Timothy Capille"""

# Number of states in the machine.  H_a is the accept state
q_1 = 1
q_2 = 2
q_3 = 3
q_4 = 4
q_5 = 5
q_6 = 6
h_a = 'h_a'


#  Tm 3.13 as a function

def TM_3_13(s):
    # l = tape of TM
    l = init_TM(s)
    # current state
    state = q_1
    head = l.index('$') + 2
    finished = False
    while not finished:
        finished = True
        if state == q_1:
            if l[head] == '0' or l[head] == '1':
                state = q_2
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
            elif l[head] == '#':
                head = head + 1
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
            else:
                state = h_a
                finished = False
                continue
        if state == q_2:
            if l[head] == '0':
                l[head] = '#'
                head = head + 1
                state = q_3
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
            elif l[head] == '1':
                l[head] = '#'
                head = head + 1
                state = q_5
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
            elif l[head] == '#':
                head = head + 1
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
            else:
                state = q_6
                head = head - 1
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
        if state == q_3:
            if l[head] == '0':
                head = head + 1
                state = q_2
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
            elif l[head] == '1':
                l[head] = '#'
                head = head + 1
                state = q_4
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
            elif l[head] == '#':
                head = head + 1
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
        if state == q_4:
            if l[head] == '0':
                head = head + 1
                state = q_5
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
            elif l[head] == '1':
                head = head + 1
                state = q_3
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
            elif l[head] == '#':
                head = head + 1
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
            else:
                head = head - 1
                state = q_6
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
        if state == q_5:
            if l[head] == '0':
                l[head] = '#'
                head = head + 1
                state = q_4
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
            elif l[head] == '1':
                head = head + 1
                state = q_2
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
            elif l[head] == '#':
                head = head + 1
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
        if state == q_6:
            if l[head] == '0':
                head = head - 1
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
            elif l[head] == '1':
                head = head - 1
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
            elif l[head] == '#':
                head = head - 1
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
            else:
                state = q_1
                head = head + 1
                finished = False
                print('Head: ' + str(head) + ' State: ' + str(state))
                print(l)
                continue
        if state == h_a:
            print('Head: ' + str(head) + ' State: ' + str(state))
            print(l)
            return True
    return False


# initial configuration of the tape
def init_TM(s):
    l = []
    l.append('$')
    l.append('$')
    for ch in s:
        l.append(ch)
    l.append('$')
    l.append('$')
    l.append('$')
    return l


# tests a list of strings that should pass and a list of strings that should fail
def test():
    t = ['10', '01', '1001', '0110', '0101', '1010']  ## all true
    f = ['0', '1', '11', '00', '1111', '101', '010']  ## all false
    print('--------------------------------------True -------------------------------------------')
    for x in t:
        print(TM_3_13(x))
    print('--------------------------------------False ------------------------------------------')
    for y in f:
        print(TM_3_13(y))

test()
