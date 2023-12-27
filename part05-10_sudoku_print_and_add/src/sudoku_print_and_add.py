# Write your solution here
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number


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
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]  

    print_sudoku(sudoku)