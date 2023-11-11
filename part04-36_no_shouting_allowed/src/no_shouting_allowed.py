# Write your solution here
def no_shouting(list_of_strings):
    result = []
    for string in list_of_strings:
        if not string.isupper():
            result.append(string)
    return result

