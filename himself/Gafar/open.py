f = open("/home/yogi/Bureau/liste_fichiers_dns.json", "r", encoding="utf-8")

liste_fichiers_dns = f.read()
print(liste_fichiers_dns)

'''
"/home/yogi/Documents/test/Document 1 sans titre",
    "/home/yogi/Documents/test/Document 1 sans titre (3e copie)",
    "/home/yogi/Documents/test/Document 1 sans titre (5e copie)",
    "/home/yogi/Documents/test/Document 1 sans titre (6e copie)",
    "/home/yogi/Documents/test/Document 1 sans titre (copie)",
    "/home/yogi/Documents/test/Document 1 sans titre (autre copie)",
    "/home/yogi/Documents/test/Document 1 sans titre (4e copie)"
'''

#f = open("/home/yogi/Bureau/liste_fichiers_dns.json", "w", encoding="utf-8")
#print(f.name) # /home/yogi/Bureau/liste_fichiers_dns.json

'''
>>> f = open('test.txt', 'w')
>>> print f.name
test.txt
>>> f = open('D:\\test\\test.txt', 'w')
>>> f.name
'D:\\test\\test.txt'
>>> os.path.basename(f.name)
'test.txt'
'''