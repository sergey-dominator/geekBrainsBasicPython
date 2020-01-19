from functools import reduce


def multiply(first_operand, second_operand):
    return first_operand * second_operand


print(reduce(multiply, [i for i in range(100, 1001) if i % 2 == 0]))
