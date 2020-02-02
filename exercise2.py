class CustomArithmeticError(Exception):
    def __init__(self, message):
        self.message = message


print("Enter dividend: ")
dividend = input()

print("Enter divider: ")
divider = input()

try:
    dividend = int(dividend)
    divider = int(divider)

    if divider == 0:
        raise CustomArithmeticError("What are you doing? You can't divide by zero")

    print(f'{dividend} / {divider} = {dividend / divider}')

except ValueError:
    print("Only numbers are supported")
except CustomArithmeticError as arithmeticError:
    print(arithmeticError.message)
