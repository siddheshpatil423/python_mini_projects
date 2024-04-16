import random

top_range = input("Type a number: ")

guesses = 0

if top_range.isdigit():
    top_range = int(top_range)

    if top_range < 0:
        print("please type a number greater than 0 next time.")
        quit()
else:
    print("please type a number next time.")
    quit()


ran_num = random.randint(0,top_range)

while True:
    guesses += 1
    user_guess = input("make a guess")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number next time.")
        continue
    
    if user_guess == ran_num:
        print("You gor it in")
        break
    else:
        if user_guess < ran_num:
            print("You were below the number ")
        elif user_guess > ran_num:
            print("you were above the number ")


print("You gor it in",guesses,"guesses")

