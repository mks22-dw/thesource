s = """90 99 97 89
91 94 99 89
81 94 100 100
90 99 79 81
50 79 49 41
90 99 94 94"""

def get_values(source):
    vals = []
    space = source.find(' ')
    while space != -1:
        val = source[:space]
        vals.append(int(val))
        source = source[space+1:]
        space = source.find(' ')
    if source != '':
        vals.append(int(source))
    return vals

print('get_values test:')
flat_list = get_values('90 99 97 89')
print(flat_list)

####################################

def get_vals_list(source):
    rows = source.split('\n')
    vals = []
    for row in rows:
        vals.append(get_values(row))
    return vals
            
print('\nget_vals_list test:')
all_vals = get_vals_list(s)
print(all_vals)

####################################

def get_averages(g):
    avgs = []
    for inner_list in g:
        avg = sum(inner_list) / len(inner_list)
        avgs.append(avg)
    return avgs

print('\nget_averages test:')
print(get_averages(all_vals))

####################################

def numlist_to_string(g):
    s = ''
    for value in g:
        s+= f'{value},'
    return s[:-1]

print('\nnumlist_to_string test:')
print(numlist_to_string(flat_list))

####################################

def combine_data(data):
    values =  get_vals_list(data)
    averages = get_averages(values)
    s = ''
    i = 0
    for row in values:
        csv = numlist_to_string(row)
        s+= f'{csv}: {averages[i]}\n'
        i+= 1        
    return s

print('\ncombine_data test:')
print(combine_data(s))
        
