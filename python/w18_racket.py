import random

def check_parens(code):
    p_count = 0
    c = 0
    while c < len(code):
        if code[c] == '(':
            p_count+= 1
        elif code[c] == ')':
            p_count-= 1
        c+= 1
    return p_count == 0

c0 = '(+ 4 5)'
c1 = '(+ 4 5'
c2 = '(+ 4 (* (- 2 1) (/ 3 6)))'
c2 = '(+ 4 (* (- 2 1) (/ 3 6)))'
c3 = '(+ 4 (* (- 2 1) / 3 6)))'

print(f'check {c0}: {check_parens(c0)}')
print(f'check {c1}: {check_parens(c1)}')
print(f'check {c2}: {check_parens(c2)}')
print(f'check {c3}: {check_parens(c3)}')


def to_int(s):
    c = len(s) - 1
    n = 0
    pow = 0
    while c >= 0:
        n+= (ord(s[c]) - ord('0')) * 10**pow
        pow+= 1
        c-= 1
    return n

s = '876321'
si = to_int(s)
print(f's: {s}, {si}, {type(si)}')


def eval_arithmetic(code):
    operation = code[1]
    values = code[3:-1]
    space = values.find(' ')
    v0 = to_int(values[:space])
    v1 = to_int(values[space+1:])
    if operation == '+':
        return v0 + v1
    elif operation == '-':
        return v0 - v1
    elif operation == '*':
        return v0 * v1
    elif operation == '/':
        return v0 / v1

s = '(+ 87 321)'
print(f'{s} = {eval_arithmetic(s)}')


e0 = '(- 954 824)(- 340 271)(/ 659 653)(/ 296 689)'
e1 = '(* 97 557)(- 246 924)(- 692 642)(/ 194 737)(* 359 640)'
e2 = '(- 373 127)(/ 981 184)'

def eval_expressions(e):
    s  = ''
    end_paren = e.find(')')
    while end_paren != -1:
        exp = e[:end_paren+1]

        result = eval_arithmetic(exp)
        s+= f'{exp} = {result}\n'
        print(f'\t{exp}')
        e = e[end_paren + 1:]
        end_paren = e.find(')')
    return s

print(eval_expressions(e1))


# Challenge Problems
def check_parens2(code):
    open_count = 0
    close_count = 0
    c = 0
    while c < len(code):
        if code[c] == '(':
            open_count+= 1
        elif code[c] == ')':
            close_count+= 1
        if open_count - close_count < 0:
            return False
        c+= 1
    return (open_count - close_count) == 0

c0 = '(+ 4 5)'
c1 = '(+ 4 5'
c2 = '(+ 4 (* (- 2 1)(/ 3 6)))'
c2 = '(+ 4 (* (- 2 1)(/ 3 6)))'
c3 = '(+ 4 (* (- 2 1) / 3 6)))'
c4 = '(+ 4 (* ))))'

print(f'check {c0}: {check_parens2(c0)}')
print(f'check {c1}: {check_parens2(c1)}')
print(f'check {c2}: {check_parens2(c2)}')
print(f'check {c3}: {check_parens2(c3)}')
print(f'check {c4}: {check_parens2(c4)}')
