import glob
import os

for file in os.listdir("/home/yogi/Documents/test"):
    if file.endswith('.txt'):
        print(file)
'''
Document 1 sans titre (13e copie).txt
Document 1 sans titre (8e copie).txt
Document 1 sans titre (10e copie).txt
Document 1 sans titre (7e copie).txt
Document 1 sans titre (11e copie).txt
Document 1 sans titre (15e copie).txt
Document 1 sans titre (9e copie).txt
'''
list_files = glob.glob('*.txt')
print(list_files) # []
# marche pas !!!!
'''
with open("/home/yogi/Documents/test/*.txt", 'r') as f:
    if "DNS 1 = 4.4.4.4" in f.readlines():
        print("bravo")
    else:
        print("tantpis")
'''