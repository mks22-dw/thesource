from random import random

f = open('data/2024_nyc_temps.csv')
text = f.read().strip()
f.close()

def make_temp_list(text):
    #remove the first row
    data = text.split('\n')[1:]
    print(data)
    temps = []
    for row in data:
        row = row.split(',')
        temp = row[1].split('.')
        temp = int(temp[0])
        temps.append(temp)
    return temps

temp_list = make_temp_list(text)
print(temp_list)

def make_temp_counts(temps):
    counts = {}
    t = 0
    while t < len(temps) - 1:
        key = temps[t]
        next = temps[t+1]
        if key in counts:
            if next in counts[key]:
                counts[key][next]+= 1
            else:
                counts[key][next] = 1
        else:
            counts[key] = {next: 1}
        t+= 1
    return counts

temp_counts = make_temp_counts(temp_list)
print(temp_counts)

def make_temp_markov(counts):
    for temp in counts:
        total_options = sum(counts[temp].values())
        for next in counts[temp]:
            counts[temp][next] = counts[temp][next]/total_options

make_temp_markov(temp_counts)
print(temp_counts)

def get_next_day(model, today):
    odds = model[today]
    r = random()
    total = 0
    for state in odds:
        total+= odds[state]
        if r < total:
            return state

def get_forecast(model, days, start):
    forecast = []
    i = 0
    while (i < days):
        forecast.append(start)
        start = get_next_day(model, start)
        i+= 1
    return forecast

#print(get_forecast(weather, 10, 'sunny'))
