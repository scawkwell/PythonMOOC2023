# Write your solution here
def no_vowels(my_string : str):
    vowelless = ""
    vowels = "aeiou"
    for character in my_string:
        if character not in vowels:
            vowelless += character
    return vowelless

if __name__ == "__main__":
    print(no_vowels("qwerqwer"))