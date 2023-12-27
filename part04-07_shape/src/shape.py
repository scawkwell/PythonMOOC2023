# Copy here code of line function from previous exercise and use it in your solution
def line(n, string):
    if string == "":
        print("*" * n)
        return
    print(string[0] * n)


def triangle(size, character):
    # You should call function line here with proper parameters
    for row in range(size):
        line(row+1, character)


def shape(tri_size, tri_char, height, rec_char):
    triangle(tri_size, tri_char)
    for row in range(height):
        line(tri_size, rec_char)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")