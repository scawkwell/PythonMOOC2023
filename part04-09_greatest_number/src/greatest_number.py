# Write your solution here

def greatest_number(num_1, num_2, num_3):
    number_list = [num_1, num_2, num_3]
    number_list.sort()
    greatest = number_list[2]
    return greatest


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)