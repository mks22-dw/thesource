def upcase(c):
    diff = ord('A') - ord('a')
    if c >= 'a' and c <= 'z':
        new_c = ord(c) + diff
        return chr(new_c)
    else:
        return c
<<<<<<< HEAD
print(f" q: {upcase('q')}")
print(f" C: {upcase('C')}")
print(f" 3: {upcase('3')}")
=======

>>>>>>> 972a386b4087b9eda55f0254e86858921f6d427b


def upstring(s):
    new_s = ''
    c = 0
    while c < len(s):
        new_s+= upcase(s[c])
        c+= 1
    return new_s



