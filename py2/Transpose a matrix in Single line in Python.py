def transpose_matrix(matrix):
    result = [list(row) for row in zip(*matrix)]
    return result


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposed_matrix = transpose_matrix(matrix)
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed_matrix:
    print(row)
