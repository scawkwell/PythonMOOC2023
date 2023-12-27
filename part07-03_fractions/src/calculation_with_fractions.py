# Write your solution here
def fractionate(amount : int):
    from fractions import Fraction
    output  = []
    while len(output) < amount:
        output.append(Fraction(1, amount))
    return output


if __name__ == "__main__":
    for p in fractionate(5):
        print(p)