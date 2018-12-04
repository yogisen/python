import csv

f = open("nfl.csv")
nfl = list(csv.reader(f))
print(nfl)

titans_wins = 0
for row in nfl:
    if row[2] == "Tennessee Titans":
        titans_wins +=1
print(titans_wins)

def nfl_wins(team):
    count = 0
    for row in nfl:
        if row[2] == team:
            count +=1
    return(count)

Pittsburgh_Steelers_wins = nfl_wins("Pittsburgh Steelers")
print (Pittsburgh_Steelers_wins)

def nfl_wins_per_years(team, year):
    count = 0
    for row in nfl:
        if row[2] == team and row [0] == year:
            count +=1
    return(count)

Pittsburgh_Steelers_2009wins = nfl_wins_per_years("Pittsburgh Steelers", "2012")
print(Pittsburgh_Steelers_2009wins)

class Team():

    def __init__(self,name):
        self.name = name

    def print_name(self):
        print(self.name)

    def count_total_wins(self):
        count =0
        for row in nfl:
            if row[2] == self.name:
                count +=1
        return (count)

broncos = Team("Denver Broncos")

broncos_wins = broncos.count_total_wins()

print("broncos" + str(broncos_wins) )