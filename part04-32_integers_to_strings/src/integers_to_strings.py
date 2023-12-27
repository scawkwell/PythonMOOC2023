# Write your solution here
def formatted(float_list : list):
    formatted = []
    for item in float_list:
        formatted.append(f"{item:.2f}")
    return formatted


if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)

