input_list = [300, 5, 19, 2, 25, 55, 33, 66]

print([input_list[i] for i in range(1, len(input_list)) if input_list[i] > input_list[i - 1]])
