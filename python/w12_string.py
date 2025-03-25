def split_name(name):
    new_s = ''
    c = 0
    while c < len(name):
        if name[c] == ' ':
            new_s+= '\n'
        else:
            new_s+= name[c]
        c+= 1
    return new_s

print(split_name("John Shaft"))


def bondify(name):
    new_s = ''
    space = name.find(' ')+1
    while space < len(name):
        new_s+= name[space]
        space+= 1
    new_s+= '... '+name
    return new_s

print(bondify('Mr. DW'))

def find_last(s, key):
    c = len(s) - 1
    while c >= 0:
        if (s[c] == key):
            return c
        c-= 1
    return c

print(find_last('hello', 'l'))
print(find_last('hello', 'h'))
print(find_last('hello', 'z'))

def replace(s, key, r):
    new_s = ''
    c = 0
    spot = s.find(key)
    while c < len(s):
        if c == spot:
            new_s+= r
            c+= len(key)
        else:
            new_s+= s[c]
            c+= 1
    return new_s

print(replace("I abhor cs!", "abhor", "love"))
