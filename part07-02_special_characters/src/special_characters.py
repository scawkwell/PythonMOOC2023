# Write your solution here
def separate_characters(my_string : str):
    import string
    letters = ""
    punct = ""
    others = ""

    for letter in my_string:
        if letter in string.ascii_letters:
            letters += letter
        elif letter in string.punctuation:
            punct += letter
        else:
            others += letter
    
    return (letters, punct, others)





if __name__ == "__main__":
    print(separate_characters("qwer234$sdf£"))