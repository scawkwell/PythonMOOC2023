# Write your solution here
def generate_password(length : int):
    from string import ascii_lowercase
    from random import choices
    output = ""
    
    for letter in choices(ascii_lowercase, k = length):
        output += letter
    return output


if __name__ == "__main__":
    print(generate_password(5))