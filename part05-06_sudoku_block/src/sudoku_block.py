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



if __name__ == "__main__":
        
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





    print(block_correct(sudoku, 0, 0))
