import os

file_name = "input3.txt"
threshold = 20000

if os.path.exists(file_name):
    with open(file_name, 'r') as input_file:
        salaries = []
        for line in input_file:
            split_values = line.split(" ")
            if len(split_values) < 2:
                print(f'There are some problems with line {line}. Each line should have second name and salary')
            else:
                current_salary = float(split_values[1])
                if current_salary < threshold:
                    print(f'{split_values[0]} has salary lower than {threshold}')
                salaries.append(current_salary)

        print(f'Average salary is {sum(salaries) / len(salaries)}')
else:
    print("File doesn't exist")
