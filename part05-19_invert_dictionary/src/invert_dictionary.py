# Write your solution here
def invert(dictionary: dict):
    temp_dict = {}
    for key, val in dictionary.items():
        temp_dict[val] = key
    dictionary.clear()
    dictionary.update(temp_dict)


# def invert(dictionary: dict):
# 	copy = {}
# 	for key in dictionary:
# 		copy[key] = dictionary[key]
# 		print(copy)
# 	for key in copy:
# 		del dictionary[key]
# 	for key in copy:
# 		dictionary[copy[key]] = key





if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)

