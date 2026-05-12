p = '''Movin' to the country
Gonna eat a lot of peaches
I'm movin' to the country
I'm gonna eat me a lot of peaches
Movin' to the country
Gonna eat a lot of peaches
Movin' to the country
I'm gonna eat a lot of peaches

Peaches come from a can
They were put there by a man
In a factory downtown'''

'''
If I had my little way
I'd eat peaches every day
Sun-soakin' bulges in the shade

I'm movin' to the country
I'm gonna eat me a lot of peaches
Movin' to the country
I'm gonna eat me a lot of peaches

Movin' to the country
Gonna eat me a lot of peaches
Movin' to the country
I'm gonna eat me a lot of peaches

I took a little nap where the roots all twist
Squished a rotten peach in my fist
And dreamed about you woman
I poked my finger down inside
Make a little room for an ant to hide
Nature's candy in my hand or can or pie

Millions of peaches peaches for me
Millions of peaches peaches for free
Millions of peaches peaches for me
Millions of peaches peaches for free

Look out

Millions of peaches peaches for me
Millions of peaches peaches for free
Millions of peaches peaches for me
Millions of peaches peaches for free

Look out'''

yankees = {'judge': 0.267,'rosario': 0.265, 'wells': 0.183,'rice': 0.306,'bellinger': 0.292,'stanton': 0.256,'escarra': 0.195,'domínguez': 0.2,'chisholm': 0.207, 'caballero': 0.259, 'goldschmidt': 0.236, 'mcmahon': 0.218,'jones': 0.111, 'grisham': 0.178}

def better_hitters(team, cutoff):
    hitters = []
    for player in team:
        if team[player] > cutoff:
            hitters.append(player)
    return hitters

print(better_hitters(yankees, 0.250))

def lists2dict(g0, g1):
    d = {}
    i = 0
    while i < len(g0):
        d[g0[i]] = g1[i]
        i+= 1
    return d

print(lists2dict(['v', 'vii', 'iv'], ['empire strikes back', 'force awakens', 'new hope']))

def word_counts(s):
    words = s.split()
    counts = {}
    for word in words:
        #word = word.lower()
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_counts(p))