# Write your solution here

def first_word(string : str):
    return string[0:string.find(" ")]

def second_word(string : str):
    string = string[string.find(" ")+1:]
    if string.find(" ") == -1:
        return string
    return string[0:string.find(" ")]

def last_word(string : str):
    return string[string.rfind(" ")+1:]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))