# Write your solution here
def read_input(input_string, lower, upper):
    while True:
        try:
            number = int(input(input_string))
        except:
            number = upper + 1
        
        if number > lower and number < upper:
            return number
        else:
            print(f"You must type in an integer between {lower} and {upper}")



# number = read_input("Please type in a number: ", 5, 10)
# print("You typed in:", number)