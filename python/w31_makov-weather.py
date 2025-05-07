from random import random

weather = {
    'sunny': {'sunny':0.7, 'rainy':0.1, 'cloudy':0.2},
    'rainy': {'sunny':0.1, 'rainy':0.6, 'cloudy':0.3},
    'cloudy': {'sunny':0.2, 'rainy':0.5, 'cloudy':0.3}
    }

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

print(get_forecast(weather, 10, 'sunny'))
        