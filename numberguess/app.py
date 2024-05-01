import random
random_number = random.randint(1,10)

guess = int(input("Guess the number: "))
chances =5 

while guess != random_number:

    if guess>random_number:
        chances=chances-1
        if chances==0:
            print("You run out of chances")
            exit()
        print("Guess is high!")
        print("You have",chances,"Chances")
        guess=int(input("Guess the Number : "))
    elif guess<random_number:
        chances=chances-1
        if chances==0:
            print("You loss the game")
            exit()
        print("Guess is Low")
        print("You have",chances,"Chances")
        guess=int(input("Guess the number : "))

print("Congratulations: You have won")