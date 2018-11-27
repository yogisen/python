import os
import json
t = os.path.split("/home/yogi/Documents/test")
print(t) # ('/home/yogi/Documents', 'test')
b = os.path.basename("/home/yogi/Documents") #Documents
print(b)
'''
import glob
import os.path
def listdirectory(path):
    l = glob.glob(path + '\\*')
    for i in l:
        if os.path.isdir(i):
            listdirectory(i)
        else:
            if os.path.splitext(i)[1] == '.txt':
                a = open(i)
                ## traitement
                a.close()
            else:
                print
            "extension non traite"
'''