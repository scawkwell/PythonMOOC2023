# Write your solution here
# Write your solution here
def column_correct(sudoku: list, column_no: int):
    numbers_so_far = []
    for row in range(len(sudoku)):
        if sudoku[row][column_no] != 0 and sudoku[row][column_no] in numbers_so_far:
            return False
        numbers_so_far.append(sudoku[row][column_no])
    return True

