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
