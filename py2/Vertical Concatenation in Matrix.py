def vertical_concatenation(matrix1, matrix2):
    # Check if the matrices have the same number of columns
    if len(matrix1[0]) != len(matrix2[0]):
        return "Matrices cannot be vertically concatenated. Number of columns must be the same."
    result_matrix = matrix1 + matrix2

    return result_matrix

# Input matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8, 9],
    [10, 11, 12]
]

concatenated_matrix = vertical_concatenation(matrix1, matrix2)

# Display the result
print("Matrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nVertical Concatenation:")
for row in concatenated_matrix:
    print(row)
