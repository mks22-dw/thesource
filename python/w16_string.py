def upcase(c):
    diff = ord('A') - ord('a')
    if c >= 'a' and c <= 'z':
        new_c = ord(c) + diff
        return chr(new_c)
    else:
        return c



def upstring(s):
    new_s = ''
    c = 0
    while c < len(s):
        new_s+= upcase(s[c])
        c+= 1
    return new_s



