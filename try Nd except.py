try:
    age = int(input("Enter your age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Please enter a valid age")
except ZeroDivisionError:
    print("cant be zero")