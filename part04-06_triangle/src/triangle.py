# Copy here code of line function from previous exercise
def line(n, string):
    if string == "":
        print("*" * n)
        return
    print(string[0] * n)


def triangle(size):
    # You should call function line here with proper parameters
    for row in range(size):
        line(row+1, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
