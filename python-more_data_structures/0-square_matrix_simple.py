def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for numbers in row:
            new_row.append(numbers ** 2)
        new_matrix.append(new_row)
    return new_matrix
