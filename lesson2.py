# ----------------------------exercise 1-------------------------------
flexible_list = [1, 2.0, 11 + 2j, 'fourth', False, ('cortege',), ['inner list'], {'set'}, {'dict': True}, range(1, 10)]

for index, element in enumerate(flexible_list):
    print(f'The type of {index}th element is {type(element)}')

# ----------------------------exercise 2-------------------------------
input_list_2 = []
while True:
    print(f'Current values of the list are: {input_list_2}')
    print('Do you want to add additional element? (Y/N) ')
    user_decision = input()
    if user_decision.lower() == 'y' or user_decision.lower() == 'yes':
        print('Please, enter your next element: ')
        input_list_2.append(input())
    elif user_decision.lower() == 'n' or user_decision.lower() == 'no':
        print('You have finished filling the list')
        break

current_index = 0
# we don't need to do anything with the last element, so we can iterate until the penultimate element
while current_index < len(input_list_2) - 1:
    temp_element = input_list_2[current_index]
    input_list_2[current_index] = input_list_2[current_index + 1]
    input_list_2[current_index + 1] = temp_element
    current_index += 2

print(f'Result list is: {input_list_2}')

# ----------------------------exercise 3-------------------------------
print('Enter the number of a month: ')
parsed_month = int(input())

seasons_of_year = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}
found_in_dict = False
for key, value in seasons_of_year.items():
    if value.count(parsed_month) > 0:
        print(f'According to the dict this month belongs to {key}')
        break
else:
    print("Couldn't determine season for this month by dict :(")

seasons_of_year_list = ['winter', 'winter',
                        'spring', 'spring', 'spring',
                        'summer', 'summer', 'summer',
                        'autumn', 'autumn', 'autumn',
                        'winter'
                        ]
# we have to check the parsed_month against zero, because negative numbers refers to elements of list from the end
if 0 < parsed_month < len(seasons_of_year_list):
    # list is 0-indexed structure, so we have to decrease the index by one
    print(f'According to the list this month belongs to {seasons_of_year_list[parsed_month - 1]}')
else:
    print("Couldn't determine season for this month by list :(")

# ----------------------------exercise 4-------------------------------
print('Enter your sentence: ')
got_sentence = input()

split_words = got_sentence.split(' ')
print('You have entered following elements: ')
for index, word in enumerate(split_words):
    print(f'{index + 1}: {word[:10]}')

# ----------------------------exercise 5-------------------------------
rating = []

while True:
    print(f'Current values of the rating are: {rating}')
    print('Do you want to add additional element? (Y/N) ')
    user_decision = input()
    if user_decision.lower() == 'y' or user_decision.lower() == 'yes':
        print('Please, enter your next element: ')
        # looking for suitable place for the new element
        new_element = int(input())

        inserted = False
        for current_index in range(len(rating)):
            if rating[current_index] < new_element:
                rating.insert(current_index, new_element)
                inserted = True
                print(f'New element was inserted at position {current_index}')
                break
        # if all elements in rating are bigger than new one, than just add the new element to the end
        if not inserted:
            rating.append(new_element)
    elif user_decision.lower() == 'n' or user_decision.lower() == 'no':
        print('You have finished filling the rating')
        break

# ----------------------------exercise 6-------------------------------
features = ('название', 'цена', 'количество', 'ед. изм.')
products = []

current_number_of_element = 1
while True:
    print(f'Current values of the products are: {products}')
    print('Do you want to add an additional product? (Y/N) ')
    user_decision = input()
    if user_decision.lower() == 'y' or user_decision.lower() == 'yes':
        features_values = {}
        for feature in features:
            print(f'Please, enter value for following feature: {feature}')
            feature_value = input()
            features_values[feature] = feature_value
        new_product = [current_number_of_element, features_values]
        products.append(new_product)
        current_number_of_element += 1
    elif user_decision.lower() == 'n' or user_decision.lower() == 'no':
        print('You have finished filling the list')
        break

analytics = dict()
print('Calculating analytics about the products. Please wait...')
for feature in features:
    feature_values = []
    for product in products:
        feature_values.append(product[1][feature])
    analytics[feature] = feature_values

print('Analytics has been gathered:')
print(analytics)
