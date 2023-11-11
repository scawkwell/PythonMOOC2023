# Write your solution here
def most_common_character(input):
    character_counter_store = 0
    most_common = ""
    for character in input:
        character_counter = input.count(character)
        if character_counter > character_counter_store:
            character_counter_store = character_counter
            most_common = character
    return most_common



if __name__ == "__main__":
    print(most_common_character("qwwwwwerr"))

