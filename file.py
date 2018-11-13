# Читаємо інформацію з файла в словник
from pprint import pprint

cities = {}
temp_city = {}

with open('temperature.txt') as temp:
    for city in temp:
        temperatures = temp.readline()
        cities[city.strip()] = temperatures.split()

# pprint(cities)

for city, avg_temp in cities.items():
    avg = 0
    for t in avg_temp:
        avg += int(t)
    avg = avg / len(avg_temp)
    temp_city[city] = ('%.2f' % avg)
    print(city, '%.2f' % avg)


with open('avg_temp_in_city.txt', 'w') as doc:
    for city, average_temp in temp_city.items():
        doc.write(city)
        doc.write('\n')
        doc.write(average_temp)
        doc.write('\n')