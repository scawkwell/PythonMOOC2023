# Write your solution here
def longest(strings: list):
    longest = 0
    for stringg in strings:
        if len(stringg) > longest:
            longest_string = stringg

        longest = max(len(stringg), longest)

    return longest_string




if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))


    