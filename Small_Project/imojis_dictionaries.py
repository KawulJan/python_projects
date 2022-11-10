message = input(">")
words = message.split(' ')
emonjis ={
    ":)":"**",
    ":(": "??"
}
output = ""
for word in words:
    output += emonjis.get(word, word) + " "

print(output)
