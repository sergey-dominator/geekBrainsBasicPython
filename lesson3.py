# ----------------------------exercise 1-------------------------------
def divide(dividend, divider):
    """Returns dividend divided by divider"""
    try:
        return int(dividend) / int(divider)
    except ZeroDivisionError:
        return "It's not allowed to divide by zero"
    except ValueError:
        return "Please, enter numbers"


print('Enter dividend: ')
dividendUser = input()
print('Enter divider: ')
dividerUser = input()
print(f'{dividendUser} / {dividerUser} = {divide(dividendUser, dividerUser)}')


# ----------------------------exercise 2-------------------------------
def get_info_about_user(first_name, second_name, year_of_birth, city, email, phone):
    return f'We have following info about the user: first name = {first_name}, second name = {second_name}, ' \
           f'year of birth = {year_of_birth}, city = {city}, email = {email}, phone = {phone}'


print('Enter your first name: ')
first_name_from_user = input()
print('Enter your second name: ')
second_name_from_user = input()
print('Enter your year of birth: ')
year_of_birth_from_user = input()
print('Enter your city: ')
city_from_user = input()
print('Enter your email: ')
email_from_user = input()
print('Enter your phone: ')
phone_from_user = input()

print(get_info_about_user(first_name=first_name_from_user, second_name=second_name_from_user,
                          year_of_birth=year_of_birth_from_user, city=city_from_user, email=email_from_user,
                          phone=phone_from_user))


# ----------------------------exercise 3-------------------------------
def sum_of_biggest(first, second, third):
    """returns sum of two biggest numbers"""
    min_value = min(first, second, third)
    if min_value == first:
        return second + third
    elif min_value == second:
        return first + third
    else:
        return first + second


print(f'my_func(1, 2, 3) = {sum_of_biggest(1, 2, 3)}')


# ----------------------------exercise 4-------------------------------
def easy_power(value, power):
    if type(value) != int or type(power) != int:
        return 'easy_power can work only with numbers'

    return value ** power


def power_with_restriction(value, power):
    if type(value) != int or type(power) != int:
        return 'power_with_restriction can work only with numbers'

    if value == 0:
        return 0
    if power == 0:
        return 1

    result_sum = value
    for i in range(abs(power) - 1):
        result_sum = result_sum * value
    return result_sum if power > 0 else 1 / result_sum


print('Enter value: ')
value_from_user = int(input())
print('Enter power: ')
power_from_user = int(input())
print(f'value^power by easy_power = {easy_power(value_from_user, power_from_user)}')
print(f'value^power by easy_power = {power_with_restriction(value_from_user, power_from_user)}')

# ----------------------------exercise 5-------------------------------
end_symbol = '!'
exit_from_program = False


def add(initial_value, new_values):
    """returns sum of initial_value with all numbers from second parameter which stand before end_symbol
    :param initial_value
    number which holds initial value
    :param new_values
    string which contains numbers to add
    """

    global exit_from_program
    split_values = new_values.split(' ')
    parsed_numbers = [initial_value]
    for value_as_str in split_values:
        if value_as_str == end_symbol:
            exit_from_program = True
            break
        try:
            parsed_numbers.append(int(value_as_str))
        except ValueError:
            print(f'Couldn\'t parse {value_as_str}')

    return sum(parsed_numbers)


current_sum = 0
while not exit_from_program:
    print('Enter your numbers: ')
    current_user_input = input()
    current_sum = add(current_sum, current_user_input)
    print(f'Current sum is {current_sum}')


# ----------------------------exercise 6-------------------------------
def capitalize(value):
    if type(value) != str:
        return 'capitalize() can work only with strings'

    return value.capitalize()


def capitalize_every_word(value):
    """Takes one parameter and capitalizes every words of that parameter"""

    if type(value) != str:
        return 'capitalize() can work only with strings'

    words = value.split(' ')
    result = ''
    for word in words:
        result += f'{capitalize(word)} '

    return result


print('Enter your words to capitalize: ')
input_from_user = input()
print(capitalize_every_word(input_from_user))
