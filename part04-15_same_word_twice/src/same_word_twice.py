# Write your solution here
story = []

while True:
    new_word = input("Word: ")
    if new_word in story:
        break
    story.append(new_word)

print(f"You typed in {len(story)} different words")
