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