#    function1

# def greet_user(name, last_name):
#   print(f"hi {name} {last_name}!")
#  print("welcome to our hotel")

# print("start")
# greet_user(name="samat", last_name="alim")  #key argument and possion arguments
# print("finish")

# return arguments

#    function2

# def square(numbar):
#   return numbar * numbar


# result = square(3)
# print(result)  # print(square(3))


#     function3

def emoji_converter(message):
    words = message.split(" ")
    emoji = {
        ":)": "**",
        ":(": "$$"
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))
