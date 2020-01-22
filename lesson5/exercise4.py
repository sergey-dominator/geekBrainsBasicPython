import os

file_name = "input4.txt"
output_file_name = "output4.txt"
mapping = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

if os.path.exists(file_name):
    with open(file_name, 'r', encoding='UTF-8') as input_file:
        with open(output_file_name, 'w', encoding='UTF-8') as output_file:
            for line in input_file:
                en = line[: line.index(' ')]
                line.replace(en, mapping.get(en))
                output_file.write(line.replace(en, mapping.get(en)))

    with open(output_file_name, 'r', encoding='UTF-8') as result_file:
        print(f'Content of result is:\n{result_file.read()}')
else:
    print("File doesn't exist")


