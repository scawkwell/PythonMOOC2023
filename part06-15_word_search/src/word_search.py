# Write your solution here

def dot_search(search_term : str, word_list : list):
    output = []
    for word in word_list:
        if len(word) != len(search_term):
                continue
        for index, letter in enumerate(search_term):
            if letter != "." and letter != word[index]:
                break
        else:
                output.append(word)
    return output


def find_words(search_term: str):
    with open("words.txt") as file:
        word_list = [row.strip() for row in file]

    search_term = search_term.lower()

    if "." in search_term:
        return dot_search(search_term, word_list)

    if search_term.startswith("*"):
        output = [word for word in word_list if word.endswith(search_term[1:])]
        return output

    if search_term.endswith("*"):
        output = [word for word in word_list if word.startswith(search_term[:-1])]
        return output

    if search_term in word_list:
        return [search_term]

    return []


if __name__ == "__main__":

        print(find_words(".an.l"))
