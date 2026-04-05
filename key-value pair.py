print("1. About me  \n2. Print Phone number")
choice = int(input("Enter choice: "))
if choice == 1:
    customer = {
    "name" : "chiru",
    "age" : 21,
    "Married" : True
    }
    customer ["name"] = "Chiru"
    print(customer["name"])
elif choice == 2:
    p_number = input("Enter phone number: ")
    storage = {
        "0" : "zero",
        "1" : "one",
        "2" : "two",
        "3" : "three",
        "4" : "four",
        "5" : "five",
        "6" : "six",
        "7" : "seven",
        "8" : "eight",
        "9" : "nine"
    }
    new = ""
    for i in p_number:
        new +=storage.get(i, "!") + " "
    print(new)