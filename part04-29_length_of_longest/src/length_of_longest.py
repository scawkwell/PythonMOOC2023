# Write your solution here
def length_of_longest(str_list):
    longest = str_list[0]
    for word in str_list:
        if len(word) > len(longest):
            longest = word
    return len(longest)


if __name__ == "__main__":
    print(length_of_longest(('Alan', 'Grace', 'Frances', 'Kim', 'S')))