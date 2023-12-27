# Write your solution here
def lottery_numbers(amount : int, lower : int, upper : int):
    from random import sample
    numbers = list(range(lower, upper))
    return sorted(sample(numbers, amount))
    




if __name__ == "__main__":
    lottery_numbers(5, 2, 100)
