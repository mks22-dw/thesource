from pprint import pprint

def lists2dict(keys, values):
    d = {}
    i = 0
    while i < len(keys):
        d[keys[i]] = values[i]
        i+= 1
    return d

print(lists2dict(['v', 'vii', 'iv'], ['empire strikes back', 'force awakens', 'new hope']))

yankees = {'volpe': .250,
           'soto': .329,
           'judge': .222,
           'tores': .216,
           'rizzo': .265,
           'stanton': .227,
           'verdugo': .275,
           'trevino': .281,
            'cabrera': .250}


def better_hitters(team, cutoff):
    good = []
    for hitter in team:
        if team[hitter] >= cutoff:
            good+= [hitter]
    return good

print(better_hitters(yankees, .275))

def word_counts(s):
    counts = {}
    s = s.split()
    for word in s:
        if word in counts:
            counts[word]+= 1
        else:
            counts[word]= 1
    return counts


f = open("data/alice.txt")
text = f.read()
f.close()

counts = word_counts(text)
pprint(counts)
print(counts)
