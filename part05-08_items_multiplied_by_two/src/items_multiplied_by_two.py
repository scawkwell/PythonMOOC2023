# Write your solution here

def double_items(numbers: list):
    new_numbers = list(range(len(numbers)))
    for i in range(len(numbers)):
        new_numbers[i] = numbers[i] * 2

    return new_numbers




if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)