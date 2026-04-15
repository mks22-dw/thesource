def split_name(name):
    s = ''
    for c in name:
        if c == ' ':
            s+= '\n'
        else:
            s+= c
    return s

print(split_name('John Shaft'))

def bondify(name):
    last = ''
    space = name.find(' ') + 1
    for c in name[space:]
        last+= c
    return last + '...' + name

print(bondify('Mr DW'))


def find_last(s, key):
    spot = -1
    for c in s[::-1]
        if c == key:
            return spot
        spot-= 1
    return c

print(find_last( 'hello', 'l'))
print(find_last('hello', 'h'))
print(find_last('hello', 'z'))


def replace(s, key, replacement):
    spot = s.find(key)
    if spot == -1:
        return s
    new_s = ''
    c = 0
    while c < len(s):
        if c == spot:
            new_s+= replacement
            c+= len(key)
        else:
            new_s+= s[c]
            c+= 1
    return new_s

print(replace("I hate cs!", "hate", "love"))
