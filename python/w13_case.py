def upcase(c):
    cdiff = ord('a') - ord('A')
    if c >= 'a' and c <= 'z':
        return chr(ord(c) - cdiff)
    return c

print(upcase('a'))
print(upcase('z'))
print(upcase('m'))

def upstring(s):
    new_s = ''
    c = 0
    while c < len(s):
        new_s+= upcase(s[c])
        c+= 1
    return new_s

print(upstring('hello'))
print(upstring("What's up?"))
