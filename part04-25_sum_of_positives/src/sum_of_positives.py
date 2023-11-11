# Write your solution here

def sum_of_positives(list):
    positives = []
    for n in list:
        if n > 0:
            positives.append(n)
    
    return sum(positives)

