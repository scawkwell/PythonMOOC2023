# Write your solution here

def transpose(matrix: list):
    x = len(matrix)
    y = len(matrix[0])
    new_matrix = list(range(y))
    for item in new_matrix:
        new_matrix[item] = list(range(x))

    for row_index, row in enumerate(matrix):
        for index, val in enumerate(row):
            new_matrix[index][row_index] = val
    
    matrix[:] = new_matrix


if __name__ == "__main__":
    
    matrix = [ [1, 2, 3], 
            [4, 5, 6] ]
    
    print(matrix)
    transpose(matrix)
    print(matrix)