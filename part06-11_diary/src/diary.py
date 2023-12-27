# Write your solution here
def read_diary():
    with open("diary.txt") as new_file:
        for entry in new_file:
            print(entry)

def write_diary():
    user_input = input("Diary entry: ")
    with open("diary.txt", "a") as new_file:
        new_file.write(user_input)
        new_file.write("\n")
    print("Diary saved")


while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))

    if function == 1:
        write_diary()

    if function == 2:
        read_diary()

    if function == 0:
        print("Bye now!")
        break