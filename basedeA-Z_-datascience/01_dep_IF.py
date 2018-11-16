f = open('departements-fr.csv', 'r', encoding='ISO-8859-1')
data = f.read()
rows = data.split('\n')

departements = []
int_dep_population = []

for row in rows:
    values = row.split(',')
    int_dep_population.append(int(values[1]))
    departements.append(values[0])

found = False

for dep in departements:
    if dep == "Paris":
        found = True

if found:
    print('Paris est present dans la liste')

counter = 0
index = 0

for dep in departements:
    if dep == "Paris":
        index = counter
    counter += 1

print(index) # 75
print(counter) # 100


million_list = []

for pop in int_dep_population:
    if pop > 1_000_000:
        million_list.append(pop)

print(million_list)
