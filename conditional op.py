name = input("What is your name? ")
if len(name)<3:
    print("name must be at least 3 characters long")
elif len(name)>10:
    print("name should less 10 characters long")
elif 2<len(name)<15:
    print("looks good!")

temperature = input("Please enter your temperature in celsius:  ")
if temperature > "30":
    print(f"its a hot day bcz your temperature is {temperature} celsius.")
elif temperature < "30":
    print(f"its a cold day bcz your temperature is {temperature} celsius.")
else:
    print(f"its a fine day bcz your temperature is {temperature} celsius.")