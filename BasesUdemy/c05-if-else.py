count = 5

if count < 10:
    print("count is less than 10: {}".format(count))
elif count == 10:
    print("count is 10")
else:
    print("count is greater than 10: {}".format(count))

# equivalent to ternary operator
notify_user = True if count > 10 else False

name = "Alice"
name = ""  # empty value

if name != "John":
    print("Hello stranger")
elif not name:
    print("Empty name :(")

languages = ["Kotlin", "Python", "Java"]
# if "Python" not in languages:
if "Python" in languages:
    print("Python is present")
