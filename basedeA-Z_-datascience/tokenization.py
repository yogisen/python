# vocabulary = open("dictionnaire.txt", "r", encoding="utf-8").read()
# tokenized_vocabulary = vocabulary.split(" ")
# print(tokenized_vocabulary)

f = open("texte.txt", "r", encoding="utf-8")
text_string = f.read()
# print (text_string)

#text_string = text_string.replace(",","")
#text_string = text_string.replace("'","")
#text_string = text_string.replace(".","")
# text_string = text_string.replace("\n","")
#print (text_string)

def clean_text(string):
    cleaned_string = string.replace(",","")
    cleaned_string = string.replace(",","")
    cleaned_string = string.replace(",","")
    cleaned_string = string.replace(",","")
    return (cleaned_string)

cleaned_text = clean_text(text_string)
print (cleaned_text)