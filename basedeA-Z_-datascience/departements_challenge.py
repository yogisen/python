f = open('departements-fr.csv', 'r', encoding='ISO-8859-1')
data = f.read()
rows = data.split('\n')

int_dep_population = []

for row in rows:
    values = row.split(',')
    int_population = int(values[1])
    int_dep_population.append(int_population)

print(type(int_dep_population[2]))
#<class 'int'>

