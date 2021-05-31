number = 7


while True:
    user_input = input("Would you like to play (Y/n)? ")

    if user_input == "n":
        break

    user_number = int(input("Guess a number: "))
    if user_number == number:
        print("You got it!")
    elif abs(number - user_number) == 1:
        print("You were off by 1")
    else:
        print("wrong")
