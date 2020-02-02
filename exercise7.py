class ComplexNumber:
    def __init__(self, first_part, second_part):
        self.first_part = first_part
        self.second_part = second_part

    def __add__(self, other):
        return ComplexNumber(self.first_part + other.first_part, self.second_part + other.second_part)

    def __mul__(self, other):
        result_first_part = self.first_part * other.first_part - self.second_part * other.second_part
        result_second_part = self.second_part * other.first_part + self.first_part * other.second_part
        return ComplexNumber(result_first_part, result_second_part)

    def __str__(self):
        if self.second_part < 0:
            return f'{self.first_part} - {abs(self.second_part) if self.second_part != 1 else ""}i'
        else:
            return f'{self.first_part} + {self.second_part if self.second_part != 1 else ""}i'


first_complex = ComplexNumber(2, 3)
second_complex = ComplexNumber(5, -7)

print(first_complex + second_complex)
print(first_complex * second_complex)


