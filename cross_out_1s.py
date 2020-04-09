q1 = 1
q2 = 2
q3 = 3
q4 = 4
q5 = 5
ha = 6


def erase_ones(s):
    l = init_tape(s)
    head = l.index('$') + 2
    cur_state = q1
    finished = False
    while not finished:
        finished = True
        if cur_state == q1:
            if l[head] == '0':
                head = head + 1
                finished = False
                cur_state_tape(cur_state, l, head)
                continue
            elif l[head] == '1':
                head = head + 1
                finished = False
                cur_state = q2
                cur_state_tape(cur_state, l, head)
                continue
            if l[head] == '$':
                cur_state = ha
                finished = False
                cur_state_tape(cur_state, l, head)
                continue
        if cur_state == q2:
            if l[head] == '0':
                l[head] = '1'
                head = head - 1
                cur_state = q3
                finished = False
                cur_state_tape(cur_state, l, head)
                continue
            elif l[head] == '1':
                head = head + 1
                finished = False
                cur_state = q2
                cur_state_tape(cur_state, l, head)
                continue
            if l[head] == '$':
                head = head - 1
                cur_state = q5
                finished = False
                cur_state_tape(cur_state, l, head)
                continue
        if cur_state == q3:
            if l[head] == '0':
                l[head] = '0'
                head = head + 1
                cur_state = q4
                finished = False
                cur_state_tape(cur_state, l, head)
                continue
            elif l[head] == '1':
                head = head - 1
                finished = False
                cur_state_tape(cur_state, l, head)
                continue
            if l[head] == '$':
                head = head + 1
                cur_state = q4
                finished = False
                cur_state_tape(cur_state, l, head)
                continue
        if cur_state == q4:
            if l[head] == '1':
                l[head] = '0'
                head = head + 1
                finished = False
                cur_state = q2
                cur_state_tape(cur_state, l, head)
                continue
        if cur_state == q5:
            if l[head] == '0' or l[head] == '$':
                cur_state = ha
                finished = False
                cur_state_tape(cur_state, l, head)
                continue
            if l[head] == '1':
                l[head] = '$'
                head = head - 1
                finished = False
                cur_state_tape(cur_state, l, head)
                continue
        if cur_state == ha:
            return True
    return False


def cur_state_tape(cur_state, l, head):
    print('Current state: ' + str(cur_state) + " Head: ", str(head))
    print('Tape: ', end='')
    print(l)


def init_tape(s):
    l = []
    l.append('$')
    l.append('$')
    for ch in s:
        l.append(ch)
    l.append('$')
    l.append('$')
    l.append('$')
    return l


erase_ones('0011001')
