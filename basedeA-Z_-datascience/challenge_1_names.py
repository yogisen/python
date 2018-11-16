f = open('unisex-names.csv', 'r')
names = f.read()
names_list = names.split('\n')
print(names_list[0:10]) #['Casey,176544.328149', 'Riley,154860.665173',

# obetnir une liste de liste

names_data = []

for name in names_list:
    temp_list = name.split(',')
    names_data.append(temp_list)
print(names_data[0:3])# [['Casey', '176544.328149'], ['Riley', '154860.665173'],

# convertir les valeurs numeriques

numerical_list = []

for line in names_data:
    name = line[0]
    count = float(line[1])
    new_list = [name, count]
    numerical_list.append(new_list)

print(numerical_list[0:4])# [['Casey', 176544.328149], ['Riley', 154860.665173],

# filtrer la liste

final_list = []

for line in numerical_list:
    name = line[0]
    population = line[1]
    if population >= 160_000:
        final_list.append(name)

print(final_list[0:10]) #['Casey']