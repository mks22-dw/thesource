def get_values(s):
    g = s.split()
    i = 0
    while i < len(g):
        g[i] = int(g[i])
        i+= 1
    return g
print(get_values('90 99 97 89'))

def get_vals_list(s):
    g = s.split('\n')
    i = 0
    while i < len(g):
        g[i] = get_values(g[i])
        i+= 1
    return g

s = """90 99 97 89
91 94 99 89
81 94 100 100
90 99 79 81
50 79 49 41
90 99 94 94"""
print(get_vals_list(s))

def get_averages(g):
    avgs = []
    for sublist in g:
        avg = sum(sublist) / len(sublist)
        avgs.append(avg)
    return avgs
print(get_averages(get_vals_list(s)))
