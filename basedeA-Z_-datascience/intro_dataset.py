f = open("US-births-2000-2014.csv", "r")
us_births = f.read()
births_split = us_births.split("\n")
print(births_split[0:10])

# convertir en liste de liste

def read_csv(file):
    f = open(file, "r")
    string_list = f.read()
    string_list = string_list.split('\n')
    string_list = string_list[1:]

    final_list = []

    for row in string_list:
        int_fields = []
        string_fields = row.split(',')
        for row in string_fields:
            int_fields.append(int(row))
        final_list.append((int_fields))
    return(final_list)

us_births_list = read_csv("US-births-2000-2014.csv")
print(us_births_list[0:10])

# calculer le nbre de naisssance par mois

def month_births(list):
    births_per_months = {}

    for li in list:
        month = li[1]
        births = li[4]

        if month in births_per_months:
            births_per_months[month] += births
        else:
            births_per_months[month] = births
    return(births_per_months)

us_months_births = month_births(us_births_list)
print(us_months_births)

