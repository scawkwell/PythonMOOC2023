# Write your solution here
def load_dictionary():
    dictionary = []
    with open("dictionary.txt") as file:
        for line in file:
            words = line.strip().split(",")
            dictionary.append((words[0], words[1]))
    return dictionary

def save_dictionary(dictionary : list):
    with open("dictionary.txt", "w") as file:
        for entry in dictionary:
            file.write(f"{entry[0]},{entry[1]}\n")

def newentry(dictionary : list):
    new_finnish = input("The word in Finnish: ")
    new_english = input("The word in English: ")
    dictionary.append((new_finnish,new_english))
    print("Dictionary entry added")

def search(dictionary : list):
    search_term = input("Search term: ")
    for entry in dictionary:
        if search_term in entry[0] or search_term in entry[1]:
            print(f"{entry[0]} - {entry[1]}")


def main():
    dictionary = load_dictionary()

    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        function = int(input("Function: "))

        if function == 3:
            print("Bye!")
            save_dictionary(dictionary)
            break

        if function == 2:
            search(dictionary)
            
        if function == 1:
            newentry(dictionary)
            





main()
