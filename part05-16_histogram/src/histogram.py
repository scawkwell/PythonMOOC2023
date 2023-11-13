# Write your solution here
def histogram(input_string):
    letters = {}
    
    for letter in input_string:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1

    for key, value in letters.items():
        print(f"{key} {"*" * value}")

