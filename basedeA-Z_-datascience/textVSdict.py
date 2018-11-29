f = open("texte.txt", "r", encoding="utf-8")
texte = f.read()
g = open("dictionnaire.txt", "r", encoding="utf-8")
vocabulary = g.read()

tokenized_vocabulary = vocabulary.split(" ")

def clean_text(text_string, special_caracters, replacement_string):
    cleaned_string = text_string

    for string in special_caracters:
        cleaned_string = cleaned_string.replace(string, replacement_string)
    cleaned_string = cleaned_string.lower()
    cleaned_string = cleaned_string.split(" ")
    return (cleaned_string)

clean_characters = [".", "'", ",", "\n"]
replacement = ""
cleaned_text = clean_text(texte, clean_characters, replacement)

print(cleaned_text)
print(tokenized_vocabulary)

misspelled_words = []

for missed in cleaned_text:
    if missed not in tokenized_vocabulary:
        misspelled_words.append(missed)

print(misspelled_words)
