import random

tries = 0

name = input("What is your name? >>> ") #Asking the user for his name
hello = print("hello {0}!".format(name)) #print the player name
next = input("The game is simple. You need to guess the number that the computer have chose. Do you want the [L]ong game or the [F]ast game? >>>") #ask the player for the type of the game

if next == "L":
    rand = random.randint(1,1000)
    while True:
        print("You have 17 tries to guess the number between 1-1000. Good luck {0}>>> ".format(name))
        guess = int(input())
        if guess == rand: #the guess is equal to the number:
            print("you did it in {0} tries".format(tries))
            break
        if guess > rand: #the guess is bigger from the number:
            print("your number is bigger, Try again")
            tries += 1
        if guess < rand: #the guess is lower from the number:
            print("your number is lower, Try again")
            tries += 1
        if tries == 17: #the player reach to the numbers of tries
            print("{0}, You lose , Try again".format(name))
            break
elif next == "S":
    rand = random.randint(1,100)
    while True:
        print("You have 10 tries to guess the number between 1-100. Good luck {0}>>> ".format(name))
        guess = int(input())
        if guess == rand: #the guess is equal to the number:
            print("you did it in {0} tries".format(tries))
            break
        if guess > rand: #the guess is bigger from the number:
            print("your number is bigger, Try again")
            tries += 1
        if guess < rand: #the guess is lower from the number:
            print("your number is lower, Try again")
            tries += 1
        if tries == 10: #the player reach to the numbers of tries
            print("{0}, You lose , Try again".format(name))
            break