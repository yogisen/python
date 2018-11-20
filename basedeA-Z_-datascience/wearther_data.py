weather_data = []

f = open("madrid-weather-2016.csv", "r")
data = f.read()

rows = data.split('\n')
for row in rows:
    split_row = row.split(',')
    weather_data.append(split_row)

print(weather_data[0:5]) # [['Jour', 'Climat'], ['1', 'Soleil'], ['2', 'Soleil'],

count = 0
for item in weather_data:
    count = count+1

print(count) # 366

new_weather = weather_data[1:366]
print(new_weather)

# verifier la presence d'un element dans une liste

weather = []

for row in new_weather:
    weather.append((row[1]))
print(weather[0:4]) # ['Soleil', 'Soleil', 'Soleil', 'Soleil']

weather_types = ["pluie", "Soleil", "Nuage", "Nuage-Pluie", "Orage", "Climat"]
weather_types_founds = []

for item in weather_types:
    found = item in weather
    weather_types_founds.append(found)

print(weather_types_founds) # [False, True, True, True, True, False]


