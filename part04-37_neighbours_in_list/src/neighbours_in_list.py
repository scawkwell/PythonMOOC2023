# Write your solution here
def is_next_to(index, my_list):
    if index +1 == len(my_list):
        return
    if my_list[index] == my_list[index+1] + 1 or my_list[index] == my_list[index+1] - 1:
        return True
    else:
        return False
    

def longest_series_of_neighbours(my_list):
    index = 0
    current_length = 1
    longest_length = 0

    while index < len(my_list):
        if current_length > longest_length:
            longest_length = current_length
        
        if is_next_to(index, my_list):
            current_length += 1
        else:
            current_length = 1
        
        index += 1

    return longest_length




if __name__ == "__main__":
    print(longest_series_of_neighbours([5, 1, 2, 3, 10, 11, 10, 11, 10]))

