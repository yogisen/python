import os

for file in os.listdir("/home/yogi/Documents/test"):
    if file.endswith('.txt'):
        print(file)
        with open("/home/yogi/Documents/test/" + file, 'r') as f:
            for line in f:
                # print(line)
                # print(line.split())
                dns = "coucou"
                if dns in line:
                    #if dns in line.split():
                    print(file)






'''

with open("/home/yogi/Documents/test/Document 1 sans titre (10e copie).txt", "r")as f:
    for line in f:
        print (line)
f = open("/home/yogi/Documents/test/Document 1 sans titre (10e copie).txt", "r")
text_string = f.read()

with open("/home/yogi/Documents/testDocument 1 sans titre (10e copie).txt", "r")as f:
    data = f.readlines()
    for line in data:
        words = line.split()
    print(words)
'''