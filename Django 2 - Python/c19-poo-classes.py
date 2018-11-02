class User:

    company = 'Django'  # class variable, shared by all instances
    __secret_salary = 10000  # simulation of private variable

    def __init__(self, name):  # constructor of an instance
        self.name = name  # instance variable, unique to each instance

    def display_info(self):
        print("{} works for {}".format(self.name, User.company))

    def set_email(self, email):
        self.email = email  # instance variable can be assigned anytime


# class variable is always accessible, not bound to an instance
print(User.company)

# error: User.name does not exist until an instance has been created
# print(User.name)

user = User('Bob')
user.display_info()
user.set_email('bob@python.org')

print(user.email)

# access to private variable has to be *very* explicit
print(User._User__secret_salary)
