# Write your solution here

def same_chars(string : str, char_1 : int, char_2 : int):
    if char_1 >= len(string) or char_2 >= len(string):
        return False
    
    if string[char_1] == string[char_2]:
        return True

    return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))