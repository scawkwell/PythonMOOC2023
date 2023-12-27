# Write your solution here
def line(n, string):
    if string == "":
        print("*" * n)
        return
    print(string[0] * n)



# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")