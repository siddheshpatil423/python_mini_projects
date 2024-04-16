print("welcome to my Computer Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print(playing.lower())

correct = 0

def correctANS():
    print("Correct!")

def wrongANS():
    print("Oops! Wrong Answer.")

print("Okay! Let's play :) ")

correct = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    correctANS()
    correct+=1
else:
    wrongANS()

answer = input("What does ROM stand for? ")

if answer.lower() == "read only memory":
    correctANS()
    correct+=1
else:
    wrongANS()

answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    correctANS()
    correct+=1
else:
    wrongANS()

answer = input("what does PSU stand for? ")

if answer.lower() == "power supply unit":
    correctANS()
    correct+=1
else:
    wrongANS()

answer = input("What does GPU stand for?")

if answer.lower() == "graphics processing unit":
    correctANS()
    correct+=1
else:
    wrongANS()

def finalResult(n):
    a = (n/5)*100

    print("You answered "+str(n)+" questions correct!")

    if (a >= 80):
        print("You Won! You answers were "+str(a)+" % correct!")
    else:        
        print("You lost! You answers were "+str(a)+" % correct!")



finalResult(correct)
