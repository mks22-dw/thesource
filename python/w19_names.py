import random

teams = '''Los Angeles Angels
Oakland Athletics
Los Angeles Dodgers
San Diego Padres
San Francisco Giants
Tampa Bay Rays
Miami Marlins
Chicago Cubs
Chicago White Sox
Kansas City Royals
St. Louis Cardinals
New York Mets
New York Yankees
Cincinnati Reds
Cleveland Guardians
Philadelphia Phillies
Pittsburgh Pirates
Houston Astros
Texas Rangers
Arizona Diamondbacks
Colorado Rockies
Washington Nationals
Atlanta Braves
Baltimore Orioles
Boston Red Sox
Detroit Tigers
Minnesota Twins
Seattle Mariners'''

teams = teams.split('\n')
print('team list:')
print(teams)

name_length = []
for team in teams:
    name_length.append(len(team))
print('name lengths:')
print(name_length)
avg_length=sum(name_length)/len(name_length)
print('average name length:', avg_length)

short_names = []
long_names = []
for team in teams:
    if len(team) < avg_length:
        short_names.append(team)
    else:
        long_names.append(team)
print('short names:')
print(short_names)
print('long names')
print(long_names)

num_words = []
two_words = []
three_words = []
for team in teams:
    num_words.append(team.count(' ')+1)
    if num_words[-1] == 2:
        two_words.append(team)
    else:
        three_words.append(team)
print('words per name:')
print(num_words)
print('two word teams:', len(two_words))
print(two_words)
print('three word teams:', len(three_words))
print(three_words)

print('5 fake teams:')
i = 0
while i < 5:
    place = two_words[ random.randrange(len(two_words)) ]
    place = place[:place.find(' ')]
    title = two_words[ random.randrange(len(two_words)) ]
    title = title[title.find(' ')+1:]
    print(place + ' ' + title)
    i+= 1
