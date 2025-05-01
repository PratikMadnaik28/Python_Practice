try:
    Age = int(input("Please enter you Age: "))
    income = 50000
    risk = income/Age
    print(Age)
    print(risk)
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid Value.")