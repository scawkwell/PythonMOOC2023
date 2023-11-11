# Write your solution here
list = []

print(f"The list is now {list}")

while True:
    operation = input("a(d)d, (r)emove, or e(x)it: ")

    if operation == "x":
        break
    
    if operation == "d":
        if len(list) == 0:
            list.append(1)
        else:
            list.append(list[-1]+1)

    if operation == "r":
        list.pop(-1)

    print(f"The list is now {list}")


print("Bye!")