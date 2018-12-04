import csv

class Team():
    def __init__(self, name):
        self.name = name
        f = open("nfl.csv")
        csvreader = csv.reader(f)
        self.nfl = list(csvreader)

    def count_total_wins(self):
        count = 0
        for row in self.nfl:
            if row[2] == self.name:
                count +=1
        return (count)

    def count_wins_per_year(self, year):
        count = 0
        for row in self.nfl:
            if row[2] == self.name and row[0] == year:
                count +=1
        return (count)

sf = Team("San Francisco 49ers")
sf_wins = sf.count_total_wins()
sf_wins2012= sf.count_wins_per_year("2012")
print(sf_wins)
print(sf_wins2012)

