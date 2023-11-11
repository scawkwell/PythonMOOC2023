# Write your solution here
def shortest(str_list):
    shortest = str_list[0]
    for word in str_list:
        if len(word) < len(shortest):
            shortest = word
    return shortest


if __name__ == "__main__":
    print(shortest(('Alan', 'Grace', 'Frances', 'Kim', 'S')))