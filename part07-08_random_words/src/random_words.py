# Write your solution here
def words(n : int, beginning : str):

    from random import sample

    with open("words.txt") as file:
        word_list = [row.strip() for row in file]

    valid_words = [word for word in word_list if word.startswith(beginning)]

    return sample(valid_words, k = n)
    



if __name__ == "__main__":
    print(words(3, "ca"))