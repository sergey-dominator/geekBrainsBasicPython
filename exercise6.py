from itertools import count, cycle


def generate_digits(start):
    for el in count(start):
        yield el


def cycling_generator(initial_list):
    for el in cycle(initial_list):
        yield el


print('Test generator of digits:')
digits_generator = generate_digits(7)
# print first 100 digits from generator
for i in range(100):
    print(next(digits_generator))

print('Test cycling generator:')
my_cycling_generator = cycling_generator(['hello', 'my', 'dear', 'friend'])
for i in range(10):
    print(next(my_cycling_generator))
