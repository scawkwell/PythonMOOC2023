# Write your solution here
def everything_reversed(input_list):
    output_list = []
    for item in input_list:
        output_list.insert(0, item[::-1])
    return output_list


if __name__ == "__main__":#
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
