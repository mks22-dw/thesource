
def make_csv_string(g):
    new_g = list(map(str, g))
    return ','.join(new_g)
print('\ncsv string test:')
print(make_csv_string([90, 99, 97, 89]))


def make_csv_table(g):
    new_g = list(map(make_csv_string, g))
    return '\n'.join(new_g)

g = [[90, 99, 97, 89], [91, 94, 99, 89], [81, 94, 100, 100], [90, 99, 79, 81], [50, 79, 49, 41], [90, 99, 94, 94]]
print('\ncsv table test')
print(make_csv_table(g))


def get_values(s):
    g = s.split(',')
    g = list(map(int, g))
    return g

def get_averages(g):
    avgs = []
    for sublist in g:
        avg = sum(sublist) / len(sublist)
        avgs.append(avg)
    return avgs

def combine_data(s):
    rows = s.split('\n')
    data = list(map(get_values, rows))
    i = 0
    s = ''
    while i < len(data):
        avg = sum(data[i])/len(data[i])
        data[i] = map(str, data[i])
        s+=','.join(data[i])
        s+= ': ' + str(avg) + '\n'
        i+= 1
    return(s)


s = """90,99,97,89
91,94,99,89
81,94,100,100
90,99,79,81
50,79,49,41
90,99,94,94"""

print('\ncombine data test:')
print(combine_data(s))
