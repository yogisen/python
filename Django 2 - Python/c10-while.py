password = ''
cancelled = False

while password != 'MontyPython':
    print("Secret password?")
    password = input()

    if password == 'exit':
        cancelled = True
        break

if cancelled:
    print("Don't give up...")
else:
    print("You found the secret password!")

