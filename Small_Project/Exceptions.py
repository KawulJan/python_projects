try:
    age = int(input("age: "))
    income = 30000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("inter invalid value / age can not be 0.")
except ValueError:
    print("Invalid value")

