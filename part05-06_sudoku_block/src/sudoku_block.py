# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers_so_far = []
    for row_check in range(3):
        for column_check in range(3):
            square = sudoku[row_no + row_check][column_no + column_check]
            if square != 0 and square in numbers_so_far:
                return False
            numbers_so_far.append(square)
        return True

