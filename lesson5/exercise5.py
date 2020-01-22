from functools import reduce

file_name = "output5.txt"

digits = [4, 6, 7]


def sum_str(first, second):
    try:
        first_number = int(first)
        second_number = int(second)
        return first_number + second_number
    except ValueError:
        return 0


with open(file_name, 'w+') as output_file:
    # writing down the digits
    for digit in digits:
        output_file.write(str(digit) + ' ')

    # set the stream position at the beginning of the file
    output_file.seek(0)
    content = output_file.read().strip()
    split = content.split(' ')
    print(f'Sum of all digits is {reduce(sum_str, split)}')
