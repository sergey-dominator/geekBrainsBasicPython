user_data = []
file_name = 'output1.txt'

print('Enter the info to print into file. Leave empty line when you finished entering:')
user_input = input()

while user_input != "":
    user_data.append(user_input + '\n')
    user_input = input()

with open(file_name, 'w') as output:
    output.writelines(user_data)

print('Content of the file is: ')
with open(file_name, 'r') as input_file:
    print(input_file.read())
