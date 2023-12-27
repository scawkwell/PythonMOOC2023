# Write your solution here
def row_correct(sudoku: list, row_no: int):
    numbers_so_far = []

    for number in sudoku[row_no]:
        if number != 0 and number in numbers_so_far:
            return False
        numbers_so_far.append(number)

    return True

def column_correct(sudoku: list, column_no: int):
    numbers_so_far = []
    for row in range(len(sudoku)):
        if sudoku[row][column_no] != 0 and sudoku[row][column_no] in numbers_so_far:
            return False
        numbers_so_far.append(sudoku[row][column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers_so_far = []
    for row_check in range(3):
        for column_check in range(3):
            square = sudoku[row_no + row_check][column_no + column_check]
            if square != 0 and square in numbers_so_far:
                return False
            numbers_so_far.append(square)
        return True


def check_all_rows(soduku : list):
    for row in range(len(soduku)):
        result = row_correct(soduku, row)
        if not result:
            return False
    return True

def check_all_columns(soduku : list):
    for column in range(len(soduku)):
        result = column_correct(soduku, column)
        if not result:
            return False
    return True

def check_all_blocks(sudoku : list):
    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
            result = block_correct(sudoku, row, column)
            print(result)
            if not result:
                return False
    
    return True


def sudoku_grid_correct(sudoku: list):
    rows = check_all_rows(sudoku)
    columns = check_all_columns(sudoku)
    blocks = check_all_blocks(sudoku)
    if rows and columns and blocks:
        return True
    return False




sudoku = [
  [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
  [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
  [ 0, 5, 6, 0, 0, 0, 8, 3, 9 ],
  [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
  [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
  [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
  [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
  [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
  [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
]
sudoku_grid_correct(sudoku)

rows = check_all_rows(sudoku)
columns = check_all_columns(sudoku)
blocks = check_all_blocks(sudoku)

# print(rows)
# print(columns)
# print(blocks)