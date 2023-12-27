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

def nth_word(string : str, n : int):
    space_index = 0
    while True:
        if string.find(" ") == -1:
            print("if", string)
            return string
        
        space_index = string.find(" ")
        print(space_index)
        string = string[space_index+1:]
        print(string)



# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
    print()
    print(nth_word(sentence, 2))