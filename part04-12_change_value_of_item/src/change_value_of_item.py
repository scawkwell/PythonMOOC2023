# Write your solution here
listt = list(range(1,6))


while True:

    index = int(input("Index: "))

    if index == -1:
        break
    new_value = int(input("New value: "))

    listt[index] = new_value

    print(listt)