def sum(*args):
    total = 0
    for number in args:
        total += number
    print(total)


def sum(*args):
    """Pass args to other function"""

    def real_sum(*nums):
        total = 0
        for number in nums:
            total += number
        return total

    print(real_sum(*args))


sum(2, 3)
sum(2, 3, 8)

numbers = (10, 5, 22)  # define args as a tuple
sum(*numbers)
