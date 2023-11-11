# Write your solution here
def longest_series_of_neighbours(my_list):
    index = 0
    current_length = 1
    longest_index = 0
    longest_length = 0
    while index < len(my_list)-1:
        if my_list[index] + 1 == my_list[index+1] or my_list[index] - 1 == my_list[index+1]:
            current_length += 1
        if current_length > longest_length:
            longest_length = current_length
        else:
            current_length = 1
        index += 1
    return longest_length+1



if __name__ == "__main__":
    print(longest_series_of_neighbours([5, 1, 2, 3, 10, 11, 10, 11, 10]))

