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
    while option.lower() != "quit":
        option = str(input("> "))
        if option.lower() == "help":
            print("Start \nStop \nQuit")
        elif option.lower() == "start":
            print("Car is starting... ready to go!")
        elif option.lower() == "stop":
            print("Car is stopping...")
        elif option.lower() == "quit":
            print("goodbye")
            break
        else:
            print("Invalid option")
