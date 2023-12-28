# write your solution here
with open("wordlist.txt") as file:
    word_hash = {row.strip() : None for row in file}

sentence = input("Write text: ")

output = ""

for word in sentence.split(" "):
    
    if word.lower() in word_hash:
        output += word + " "
    
    if word.lower() not in word_hash:
        output += "*" + word + "* "

print(output)
