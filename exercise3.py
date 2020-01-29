class Cell:
    def __init__(self, nucleus_count):
        self.__nucleus_count = nucleus_count

    def __add__(self, other):
        if type(self) != type(other):
            raise ValueError('You can add only another Cell instance')

        return Cell(self.__nucleus_count + other.__nucleus_count)

    def __sub__(self, other):
        if type(self) != type(other):
            raise ValueError('You can subtract only another Cell instance')

        if self.__nucleus_count <= other.__nucleus_count:
            print('Passed cell has too many nucleus. Could not subtract it.')
        else:
            return Cell(self.__nucleus_count - other.__nucleus_count)

    def __mul__(self, other):
        if type(self) != type(other):
            raise ValueError('You can multiply with only another Cell instance')

        return Cell(self.__nucleus_count * other.__nucleus_count)

    def __truediv__(self, other):
        if type(self) != type(other):
            raise ValueError('You can divide only by another Cell instance')

        return Cell(self.__nucleus_count // other.__nucleus_count)

    def make_order(self, row_size):
        result = ''
        remaining_nucleus_count = self.__nucleus_count
        while remaining_nucleus_count > 0:
            count_for_current_row = row_size
            if remaining_nucleus_count < row_size:
                count_for_current_row = remaining_nucleus_count

            for _ in range(count_for_current_row):
                result += '*'
            result += '\n'

            remaining_nucleus_count -= count_for_current_row

        return result


first_cell = Cell(5)
second_cell = Cell(4)
third_cell = Cell(6)
fourth_cell = Cell(34)
fifth_cell = Cell(5)

result_cell = (first_cell + second_cell - third_cell) * fourth_cell / first_cell
print(result_cell.make_order(6))
