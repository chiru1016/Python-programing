print("1. Guess \n2. Car")
choice = int(input("Enter choice: "))
if choice == 1:
    secret = 9
    count = 0
    while count<=3:
        guess = int(input("guess: "))
        count +=1
        if guess == secret:
            print("you won!!")
            break
    else:
        print("Limit over")
elif choice == 2:
    option = ""
    while option != "quit":
        option = input("> ").lower()
        if option == "help":
            print("Start \nStop \nQuit")
        elif option == "start":
            print("Car is starting... ready to go!")
        elif option == "stop":
            print("Car is stopping...")
        elif option == "quit":
            print("goodbye")
            break
        else:
            print("Invalid option")
