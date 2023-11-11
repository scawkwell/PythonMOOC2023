# Write your solution here
def times_ten(start_index: int, end_index: int):
    my_dict = {}
    for number in range(start_index, end_index+1):
        my_dict[number] = number * 10

    return my_dict





if __name__ == "__main__":
    d = times_ten(3, 4)
    print(d)
