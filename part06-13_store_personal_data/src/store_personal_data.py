# Write your solution here
def store_personal_data(person : tuple):
    with open("people.csv", "a") as file:
        line = f"{person[0]};{person[1]};{person[2]}"
        file.write(line)
