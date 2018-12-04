class team ():
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

madrid = team("real madrid")
print(madrid)               #<__main__.team object at 0x7f50801567b8>
print(madrid.name)          #real madrid
madrid.print_name()         #real madrid
