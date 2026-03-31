def make_list_to_n(n):
    g = []
    x = 1
    while x <= n:
        g.append(x)
        x+= 1
    return g

print(make_list_to_n(0))
print(make_list_to_n(1))
print(make_list_to_n(3))

def count_evens(g):
    evens = 0
    for i in g:
        if i % 2 == 0:
            evens+= 1
    return evens

print(count_evens([5, 86, -988, 17, -988]))


def make_sentence(g):
    s = ''
    for word in g:
        s+= word + ' '
    return s

print(make_sentence([]))
print(make_sentence(['bob']))
print(make_sentence(['hot', 'dog']))

def join_list(g, s):
    new_s = ''
    c = 0
    while c < len(g) - 1:
        new_s+= f'{g[c]}{s}'
        c+= 1
    if c != 0:
        new_s+= f'{g[c]}'
    return new_s

print(join_list([4, 18, 2], '-'))
print(join_list([1, 2, 3, 4], ' potato '))
