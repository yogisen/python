import os

directory = '/home/yogi/Documents/test'

def checkDirectory(path, lookFor):
    content = os.listdir(path)
    for file in content:
        if file.endswith('.txt'):
            with open(path + '/' + file, 'r',encoding="utf8", errors='ignore') as f:
                for idx, line in enumerate(f.readlines()):
                    line = line.rstrip()

                    #if line == lookFor:
                    if lookFor in line:
                        yield idx, file
                        break

for idx, file in checkDirectory(directory, "valuelokkfor"):
    print (idx, file[0:-4])
    #print(file[0:-4])
'''
for idx, file in checkDirectory(directory, "value", ""):
    #print (idx, file)
    print(file[0:-4])
'''