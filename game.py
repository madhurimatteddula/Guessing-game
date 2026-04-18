import random
name=input("May I ask you for your name? \n")
print(f"{name}, we are going to play a game.")
print("I am thinking of a number between 1 and 100")
print("Go ahead,Guess!")
number =random.randint(1,100)
while True:
    guess=int(input("Guess: "))
    if guess > number:
        print("The guess of the number that you have entered is too high")
        print("Try again!")
    elif guess<number:
        print("The guess of the number that you have entered is too low")
        print("Try again!")
    else :
        print("Congratulations! you guessed the number correctly!")
        break