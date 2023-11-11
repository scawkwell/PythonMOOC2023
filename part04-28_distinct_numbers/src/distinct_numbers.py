# Write your solution here

def distinct_numbers(int_list):
    int_list.sort()
    distinct_list = []
    for n in int_list:
        if n in distinct_list:
            continue
        distinct_list.append(n)
    return distinct_list


if __name__ == "__main__":
    print(distinct_numbers([1, 1, 2, 3, 4, 3]))
    print("poo")
