name = input("Type your Name: ")
print("Welcome!", name, "to this adventure!")

answer = input("You are on a dirt road and it has come to an end. You can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or you can swim across. Type walk to walk around or swim to swin across: ").lower()
    if answer == "swim":
        print('You swam across and were eaten by an alligator.')
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
    else:
        print("Not a valid answer. You lose.")

elif answer == "right":
    answer = input("You come to bridge it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()

    if answer == "back":
        print('You go back and you lose.')
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (Yes/No)").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not a valid answer. You lose.")
    else:
        print("Not a valid answer. You lose.")

else:
    print("Not a valid answer. You lose.")


print("Thank You for your time.")