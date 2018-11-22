vocabulary = open("dictionnaire.txt", "r", encoding="utf-8").read()

tokenized_vocabulary = vocabulary.split(" ")

print(tokenized_vocabulary)