# Write your solution here


def run_add(phone_book):
    name = input("name: ")
    number = input("number: ")
    print("ok!")

    phone_book[name] = number

def run_search(phone_book):
    name = input("name: ")

    if name in phone_book:
        print(f"{phone_book[name]}")
    else:
        print("no number")

def main():
    phone_book = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))

        if command == 1:
            run_search(phone_book)

        if command == 2:
            run_add(phone_book)

        if command == 3:
            break


    print("quitting...")



main()