class Matrix:
    def __init__(self, values):
        self.__values = values

    def __str__(self):
        result = ''
        for row in self.__values:
            for el in row:
                result += f"{el} "
            result += "\n"
        return result

    def __add__(self, other):
        if type(other) != type(self):
            raise ValueError('You can add matrix with only another matrix')
        if len(self.__values) != len(other.__values):
            raise ValueError('You can add only matrix with the same dimension')
        for index, row in enumerate(self.__values):
            if len(row) != len(other.__values[index]):
                raise ValueError('You can add only matrix with the same dimension')

        result = []
        for row_index, row in enumerate(self.__values):
            current_new_row = []
            for column_index, element in enumerate(row):
                current_new_row.append(element + other.__values[row_index][column_index])
            result.append(current_new_row)

        return Matrix(result)


first_matrix = Matrix([
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6]
])

second_matrix = Matrix([
    [9, 8, 7, 6],
    [8, 7, 6, 5],
    [7, 6, 5, 4]
])

print('First matrix:')
print(first_matrix, end='')
print('Second matrix:')
print(second_matrix)
print('Resulting matrix:')
print(first_matrix + second_matrix)
