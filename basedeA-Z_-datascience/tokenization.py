# ouvre un fichier modifie les caracteres

f = open("texte.txt", "r", encoding="utf-8")
text_string = f.read()

def clean_text(string):
    cleaned_string = string.replace(",","")
    cleaned_string = cleaned_string.replace("'","")
    cleaned_string = cleaned_string.replace(".","")
    cleaned_string = cleaned_string.replace("\n","")
    cleaned_string = cleaned_string.lower()
    return (cleaned_string)

cleaned_text = clean_text(text_string)
print (cleaned_text)