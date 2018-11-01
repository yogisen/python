# iterate over list
languages = ["Kotlin", "Python", "Ruby", "Java"]

for language in languages:
    if language == "Kotlin":
        continue
    elif language == "Ruby":
        break
    print(language)

# iterate over dictionnary
words = {
    "Hello": "You say yes",
    "Goodbye": "I say no",
}

for word in words:
    print(word)

# iterate over range
total = 0
for i in range(1, 10):
    total += i
print(total)

# inverse steps
total = 0
for i in range(20, 0, -10):
    total += i
print(total)

# iterate over list
items = [1, 2, 3]

for i in items:
    print(i)  # 1, 2, 3
