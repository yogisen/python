import csv
f = open("legislators.csv")
legislators = list(csv.reader(f))

gender = []
for item in legislators:
    gender.append(item[3])

print(set(gender)) # {'', 'M', 'gender', 'F'}

party = []
for item in legislators:
    party.append(item[6])
print(set(party)) # {'', 'Liberty', 'Unconditional Unionist', 'Liberal Republican', 'Anti-Jacksonian',

# EMPTY VALUES

for row in legislators:
    if row[6] == "":
        row[6] = "no party"

party = []
for item in legislators:
    party.append(item[6])
print(set(party))

# si gender est vide remplacer par M

for row in legislators:
    if row[3] == "":
        row[3] = "M"

gender = []
for item in legislators:
    gender.append(item[3])
print(set(gender)) # {'F', 'M', 'gender'}


birth_years = []

for row in legislators:
    birthday = row[2]
    parts = birthday.split('-')
    birth_years.append(parts[0])

print(birth_years[0:10]) # ['birthday', '1745', '1742', '1743', '1730'