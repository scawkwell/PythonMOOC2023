# Write your solution here

def list_sum(list_1, list_2):
    new_list = []
    for n in range(len(list_1)):
        new_list.append(list_1[n] + list_2[n])

    return new_list