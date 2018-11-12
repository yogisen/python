# str string
# import string
# help(string)

#__all__ = ['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'cap...
# ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# digits = '0123456789'
#hexdigits = '0123456789abcdefABCDEF'
#octdigits = '01234567'
#printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
#punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#whitespace = ' \t\n\r\x0b\x0c'

print('\tBonjour le monde') # # \t tabulation
print('Ceci \n permet de sauter une ligne')
print('\n') # \n saut de ligne
print('Vous voyez ce que je veux dire ?')

s = "bonjour voici un texte avec des lettres"
print(s)
print (len(s)) # 39 caracteres

print (s[10:25]) # ici un texte av
print (s[-2: ]) # es
print (s[:5]) # bonjou
print (s[:-10]) # bonjour voici un texte avec d
print (s[::1]) # bonjour voici un texte avec des lettres
print (s[::-1]) # serttel sed ceva etxet nu iciov ruojnob
print (s[::2]) # bnorviiu et vcdsltrs

s = s + ' ajoute un texte à ma chaine de caractere' #
print(s) # bonjour voici un texte avec des lettres ajoute un texte à ma chaine de caractere

s = s * 3
print(s)
# bonjour voici un texte avec des lettres ajoute un texte à ma chaine de caracterebonjour voici un texte avec des lettres ajoute un texte à ma chaine de caracterebonjour voici un texte avec des lettres ajoute un texte à ma chaine de caractere
print (len(s)) # 240

# help(str) s. affiche toutes les fonctions disponibles

print (s[0:6].capitalize()) # Bonjou
print (s[0:40].split()) # ['bonjour', 'voici', 'un', 'texte', 'avec', 'des', 'lettres']
print (s[0:40].upper()) # BONJOUR VOICI UN TEXTE AVEC DES LETTRES

print (s[0:40].split('i')+ s[0:40].split('e'))
# ['bonjour vo', 'c', ' un texte avec des lettres ', 'bonjour voici un t', 'xt', ' av', 'c d', 's l', 'ttr', 's ']

print((' '.join(s.split('i'))).split('e'))
# ['bonjour vo c  un t', 'xt', ' av', 'c d', 's l', 'ttr', 's ajout', ' un t', '

# format

print("le message de ma variable que je cite ici : {}.format")