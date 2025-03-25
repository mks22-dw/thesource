def make_list_to_n(n):
    i = 1
    g = []
    while i <= n:
        g.append(i)
        i+=1
    return g
print(make_list_to_n(0))
print(make_list_to_n(1))
print(make_list_to_n(3))

def power_list(b, n):
    e = 1
    g = []
    while e <= n:
        g.append(b**e)
        e+= 1
    return g
print(power_list(2, 5))

def make_sentence(g):
    i = 0
    s = ''
    while i < len(g):
        s+= g[i]
        if i != len(g) - 1:
            s+= ' '
        i+= 1
    return s
print(make_sentence([]))
print(make_sentence(['bob']))
print(make_sentence(['hot', 'dog']))

def join_list(g, s):
    i = 0
    new_s = ''
    while i < len(g):
        new_s+= str(g[i])
        if i != len(g) - 1:
            new_s+= s
        i+= 1
    return new_s
print(join_list([4, 18, 2], '-'))
print(join_list([1, 2, 3, 4], ' potato '))
