# Write your solution here
number = int(input("Please type in a positive integer: "))


# Print from -number to +number, excluding 0.
for i in range(-1 * number, 0): # Print from -number to -1
    print(i)
for i in range(1, number+1):    # Print from 1 to number
    print(i)