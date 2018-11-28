f = open("/home/yogi/Bureau/liste_fichiers_dns.json", "r", encoding="utf-8")

liste_fichiers_dns = f.read()
print(liste_fichiers_dns) # ex :"/home/yogi/Documents/test/Document 1 sans titre (3e copie)",

liste_fichiers_dns.split("\n")

for line in liste_fichiers_dns.split():
    print(line)
'''
    with open("/home/yogi/Documents/test/Document 1 sans titre (10e copie).txt", "r")as f:
        for line in f:
            print(line)
'''