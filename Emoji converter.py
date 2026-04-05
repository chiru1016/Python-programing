message = input("> ")
word = message.split(' ')
emoji = {
    ":)" : "😊",
    ":(" : "😔",
    ":0" : "😮"
}
output = ""
for i in word:
    output += emoji.get(i, i) + " "
print(output)