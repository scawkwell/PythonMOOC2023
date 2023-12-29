# Write your solution here
def remove_smallest(numbers: list):
    smallest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    
    numbers.remove(smallest)

# Reflection - there is literally just a min() function you dumbass 

if __name__ == "__main__":
    numbers = [9, 7, 5, 3]
    remove_smallest(numbers)
    print(numbers)
