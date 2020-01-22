import os

file_name = 'input6.txt'

if os.path.exists(file_name):
    result = dict()
    with open(file_name, 'r', encoding='UTF-8') as input_file:
        for line in input_file:
            subject_index = line.index(':')
            hours = line[subject_index + 1:].strip().split(' ')

            sum_hours = 0
            for hour in hours:
                try:
                    type_index = hour.index('(')
                    current_hour = hour[:type_index]
                    sum_hours += int(current_hour)
                except ValueError:
                    pass

            subject_name = line[:subject_index]
            result[subject_name] = sum_hours

    print(f'Result dictionary is: {result}')
else:
    print("File doesn't exist")