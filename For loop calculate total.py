print("1. Shopping cart \n2. Matrix")
choice = int(input("Enter choice: "))
if choice == 1:
    prices = [10,20,30]
    total = 0
    for price in prices:
        total += price
    print(total)
if choice == 2:
    for x in range(4):
        for y in range(3):
            print(f"x is {x} and y is {y}")