import os

file_name = "input2.txt"

if os.path.exists(file_name):
    with open(file_name, 'r') as input_file:
        lines_count = 0
        for line in input_file:
            lines_count += 1
            print(f'Line {lines_count} contains {len(line.split(" "))} words')

        print(f'The whole file contains {lines_count} lines')
else:
    print("File doesn't exist")
