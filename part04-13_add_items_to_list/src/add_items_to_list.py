# Write your solution here
new_item_count = int(input("How many new items: "))
loop_count = 0
list = []

while loop_count < new_item_count:
    list.append(int(input(f"Item {loop_count+1}: ")))
    loop_count += 1

print(list)