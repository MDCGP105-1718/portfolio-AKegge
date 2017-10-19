from random import randint
guesses = 0
userguess = 0
correctGuess = False
low = 1
high = 100
number = randint(low, high)
print (f"Guess a number between {low} and {high}. It will be a whole number.")
while correctGuess!=True:
    guesses += 1
    userguess = int(input(f"Guess {guesses}: "))
    if(userguess == number):
        correctGuess = True
        print(f"You guessed it in {guesses} guesses!")
    elif(userguess < number):
        print(f"{userguess} is too low.")
    elif(userguess > number):
        print(f"{userguess} is too high.")
