def split_name(name):
    space = name.find(' ')
    s = name[:space]
    s+= '\n'
    s+= name[space+1:]
    return s

print(split_name('John Shaft'))

def bondify(name):
    space = name.find(' ')
    last = name[space+1:]
    return last + '...' + name

print(bondify('Mr DW'))


def find_last(s, key):
    rev = s[::-1]
    spot = rev.find(key)
    if spot == -1:
        return -1
    return len(s) - spot - 1

print(find_last( 'hello', 'l'))
print(find_last('hello', 'h'))
print(find_last('hello', 'z'))


def replace(s, key, replacement):
    spot = s.find(key)
    if spot == -1:
        return s
    start = s[:spot]
    end = s[spot+len(key):]
    return start + replacement + end

print(replace("I hate cs!", "hate", "love"))
