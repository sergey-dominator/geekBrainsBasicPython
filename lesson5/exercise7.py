import json
import os

file_name = "input7.txt"
output_file_name = "output7.txt"

if os.path.exists(file_name):
    companies = dict()
    average_profit = dict()
    profits = []
    result = [companies, average_profit]
    with open(file_name, 'r', encoding='UTF-8') as input_file:
        for line in input_file:
            split_values = line.split(' ')
            company_name = split_values[0]
            company_profit = int(split_values[2])
            company_expenses = int(split_values[3])

            if company_profit > company_expenses:
                profits.append(company_profit - company_expenses)

            companies[company_name] = company_profit - company_expenses

    average_profit["average_profit"] = sum(profits) / len(profits)

    print(result)

    with open(output_file_name, 'w', encoding='UTF-8') as output_file:
        output_file.write(json.dumps(result, indent=2))
else:
    print("File doesn't exist")
