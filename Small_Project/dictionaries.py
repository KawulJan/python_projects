customer = {"name": "Muhammad Uyghur", "age": 32, "is_verified": True}
print(customer.get("age"))
print(customer["name"])

phone = input("Phone: ")
digit_mapping = {
    "2": "two",
    "1": "one",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
output = ""
for ch in phone:
    output += digit_mapping.get(ch, "!") + " "
print(output)
