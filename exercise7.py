from itertools import count


def factorial(n):
    result = 1
    for el in range(1, n + 1):
        result *= el
    return result


def factorial_generator():
    for el in count(1):
        yield factorial(el)


print('Test generator of factorials: ')
my_factorial_generator = factorial_generator()
for i in range(1, 16):
    print(f'factorial of {i} is {next(my_factorial_generator)}')
