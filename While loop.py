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
    started = False
    while True:
        option = input("> ").lower()
        if option == "help":
            print("Start \nStop \nQuit")
        elif option == "start":
            if started == True:
                print("Hey car is already started!!")
            else:
                started = True
                print("Car is starting... ready to go!")
        elif option == "stop":
            if not started == True:
                print("Hey car is already stopped!!")
            else:
                started = False
                print("Car is stopping...")
        elif option == "quit":
            print("goodbye")
            break
        else:
            print("Invalid option")