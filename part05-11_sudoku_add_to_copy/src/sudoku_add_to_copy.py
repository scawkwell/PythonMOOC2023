# Write your solution here

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = []
    row_copy = []
    for row in range(len(sudoku)):
        for column in range(len(sudoku[row])):
            row_copy.append(sudoku[row][column])
        
        sudoku_copy.append(row_copy)
        row_copy = []

    sudoku_copy[row_no][column_no] = number
    return sudoku_copy



def print_sudoku(sudoku: list):
    for row_no, row in enumerate(sudoku):
        for col_no, number in enumerate(row):
            if number == 0:
                print("_ ", end="")
            else:
                print(f"{number} ", end="")
            
            if col_no == 2 or col_no == 5:
                print(" ", end="")

        if row_no == 2 or row_no == 5:
            print()
        print()


if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
