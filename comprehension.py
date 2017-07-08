# A number guess game where the player can add their name and have to guess the number from 6 guess 
# to which the program tell the guessed number is too low or high.

import random  # Import the random library

guessesTaken = 0  # Initialize and assign 0 to gessesTaken variable 

print('Hello! What is your name?')  # Print out the message "Hello! What is your name?"
myName = input()  # initialize and assign the user's input to myName variable

number = random.randint(1, 20)  # The program generate a random number between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # Print out a message and insert the myName variable in it

while guessesTaken < 6:  # Loop trough the rest of the program until guessesTaken variable below 6
    print('Take a guess.')  # Print the message "Take a guess"
    guess = input()  # Initalize and assign the user's input to guess variable
    guess = int(guess)  # convert the convert variable into integer

    guessesTaken += 1  # Add 1 to the guessesTaken variable

    if guess < number:  # Until the variable guess value is smaller than the number variable value
        print('Your guess is too low.') # Print out "Your guess is too low"

    if guess > number: # Until the variable guess value is bigger than the number variable value
        print('Your guess is too high.') # Print out "Your guess is too high"

    if guess == number: # If the guess variable value is equal to the number variable value
        break # Break from loop

if guess == number: # If the guess variable value is equal to the number variable value
    guessesTaken = str(guessesTaken) # Convert the variable guessesTaken to a string variable
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') # Print out a sentence with the myName and guessesTaken variable values insert in

if guess != number: # if variable guess not equal to variable number
    number = str(number) # Convert variable number to a string variable
    print('Nope. The number I was thinking of was ' + number) # Print out a sentce with the number variable inserted in
