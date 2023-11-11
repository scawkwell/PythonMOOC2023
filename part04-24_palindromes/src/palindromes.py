# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(string):
    return string == string[::-1]
    
def write_a_palindrome():
    while True:
        string = input("Please type in a paldindrome: ")
        if palindromes(string):
            break
        print("that wasn't a palindrome")

    print(f"{string} is a palindrome!")
            
write_a_palindrome()
