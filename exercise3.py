class WrongType(Exception):
    def __init__(self, message):
        self.message = message


list_of_numbers = []

while True:
    print("Add new number to the list: ")
    new_value = input()

    try:
        if not new_value.isnumeric():
            raise WrongType("You can add only numbers")

        list_of_numbers.append(new_value)
    except WrongType as error:
        print(error.message)

    print(f'current list of numbers: {list_of_numbers}')

    print('Do you want to add a new element?')
    decision = input()

    if decision.lower() != 'yes':
        break
