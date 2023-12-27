# Write your solution here
# Write your solution here
def generate_strong_password(length : int, include_number : bool, include_specials : bool):
    from string import ascii_lowercase, digits
    from random import choice, randint
    specials = "!?=+-()#"
    output = ""

    characters = ascii_lowercase
    if include_number:
        characters += digits
    if include_specials:
        characters += specials

    while len(output) < length:
        if include_number and len(output) < 1:
            output += choice(digits)
        elif include_specials and len(output) < 2:
            output += choice(specials)
        else:
            output += choice(characters)


    return output


if __name__ == "__main__":
    print(generate_strong_password(5, True, False))