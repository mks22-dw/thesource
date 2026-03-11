def split_name(name):
    s = ''
    c = 0
    while c < len(name):
        if name[c] == ' ':
            s+= '\n'
        else:
            s+= name[c]
        c+= 1
    return s

print(split_name('John Shaft'))

def bondify(name):
    last = ''
    c = name.find(' ') + 1
    while c < len(name):
        last+= name[c]
        c+= 1
    return last + '...' + name

print(bondify('Mr DW'))


def find_last(s, key):
    c = len(s) - 1
    while c >= 0:
        if s[c] == key:
            return c
        c-= 1
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
