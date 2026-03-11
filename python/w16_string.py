def upcase(c):
    diff = ord('A') - ord('a')
    if c >= 'a' and c <= 'z':
        new_c = ord(c) + diff
        return chr(new_c)
    else:
        return c
print(f' q: {upcase('q')}')
print(f' C: {upcase('C')}')
print(f' 3: {upcase('3')}')


def upstring(s):
    new_s = ''
    c = 0
    while c < len(s):
        if s[c] >= 'a' and s[c] <= 'z':
            new_s+= upcase(s[c])
        else:
            new_s+= s[c]
        c+= 1
    return new_s

print(f' hello: {upstring('hello')}')
print(f" What's up: {upstring("What's up?")}")
