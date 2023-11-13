# Write your solution here
def factorials(n: int):
    import math
    factorial_dict = {}
    for number in range(1, n+1):

        factorial_dict[number] = math.factorial(number)
        # print(factorial_dict)
    return factorial_dict


if __name__ == "__main__":
    (factorials(5))
    