# Write your solution here
def row_correct(sudoku: list, row_no: int):
    numbers_so_far = []

    for number in sudoku[row_no]:
        if number != 0 and number in numbers_so_far:
            return False
        numbers_so_far.append(number)

    return True

