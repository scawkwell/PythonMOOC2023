# Write your solution here
def length_of_longest(str_list):
    longest = str_list[0]
    for word in str_list:
        if len(word) > len(longest):
            longest = word
    return len(longest)

def all_the_longest(str_list):
    length = length_of_longest(str_list)
    longest_list = []
    for word in str_list:
        if len(word) == length:
            longest_list.append(word)
    return longest_list
        
if __name__ =="__main__":
    print(all_the_longest(('Alan', 'Steve', 'Seymour', 'Kim', 'Susan')))