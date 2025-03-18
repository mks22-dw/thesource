def split_name(name):
    space = name.find(' ')
    first = name[:space]
    last = name[space+1:]
    return first + '\n' + last

print(split_name("John Shaft"))


def bondify(name):
    space = name.find(' ')
    last = name[space+1:]
    s = last + '... ' + name
    return s

print(bondify('Mr. DW'))

def find_last(s, key):
    reverse = s[::-1]
    spot = reverse.find(key)
    if (spot == -1):
        return spot
    else:
        return (len(s)-1) - spot

print(find_last('hello', 'l'))
print(find_last('hello', 'h'))
print(find_last('hello', 'z'))

def replace(s, key, r):
    spot = s.find(key)
    if (spot != -1):
        new_s = s[:spot]
        new_s+= r
        new_s+= s[spot+len(key):]
        return new_s
    return s

print(replace("I abhor cs!", "abhor", "love"))
