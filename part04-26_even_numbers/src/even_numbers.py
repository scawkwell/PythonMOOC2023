# Write your solution here

def even_numbers(list):
    evens = []
    for n in list:
        if n % 2 == 0:
            evens.append(n)
    
    return evens