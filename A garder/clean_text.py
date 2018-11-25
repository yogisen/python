f = open("texte.txt", "r", encoding="utf-8")
texte = f.read()

def clean_text(text_string, special_caracters, replacement_string):
    cleaned_string = text_string

    for string in special_caracters:
        cleaned_string = cleaned_string.replace(string, replacement_string)
    cleaned_string = cleaned_string.lower()
    return (cleaned_string)

clean_characters = [".", "'", ",", "\n","e"]
replacement = ""
clean_text = clean_text(texte, clean_characters, replacement)

print(clean_text)


ou -------------------------------------------------
```
def clean_text(string):
    cleaned_string = string.replace(",","")
    cleaned_string = cleaned_string.replace("'","")
    cleaned_string = cleaned_string.replace(".","")
    cleaned_string = cleaned_string.replace("\n","")
    cleaned_string = cleaned_string.replace("é","e")
    cleaned_string = cleaned_string.lower()
    return (cleaned_string)
```
