# Write your solution here

def create_tuple(x: int, y: int, z: int):
    smallest = min(x, y, z)
    largest = max(x, y, z)
    summed = x + y + z

    return (smallest, largest, summed)



if __name__ == "__main__":
    print(create_tuple(1, 2, -3))