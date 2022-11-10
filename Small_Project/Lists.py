names = ["alim", 'muhammad', 'Gulnur', 'samat', "halid"]
names[0] = "UyghurJan"
print(names)

numbers = [1, 2, 3, 4, 5, 10, 19, 99]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

matrix = [
    [1, 2, 5],
    [3, 4, 6],
    [5, 6, 9]
]

for row in matrix:
    for item in row:
        print(item)
matrix[0][1] = 20
print(matrix[0][1])
