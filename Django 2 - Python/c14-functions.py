# positional parameter
def say_hello(names):
    # names[0] = 'Bobette'  # parameter passed by reference, modify content
    # names = ['Bobette']  # parameter
    total = 0
    for name in names:
        print("Hello " + name)
        total += 1

    return total


# keyword argument with default value
def say_greeting(names, greeting='Hi'):
    for name in names:
        print(greeting + ' ' + name)


names = ['Bob', 'Alice', 'John']
count = say_hello(names)
print("Said hello " + str(count) + " times")

say_greeting(names, greeting='Hey there')


def sum(a, b):
    return a + b


result = sum(34, 8)  # result=42
