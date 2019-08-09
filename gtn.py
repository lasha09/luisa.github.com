#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

guess = input("Guess a number between 1 and 20 (inclusive): ")
if not guess.isnumeric(): # checks if a string is only digits 0 to 9
	print("That's not a positive whole number, try again!")
else:
	guess = int(guess) # converts a string to an integer

# check if correct
	if guess == aRandomNumber:
		print("you guessed correct!")
	

#check if out of tries
	if numTries >= 3: #numTries >= 2
		print("sorry! you failed!")
	
	

# give hints 
if(guess > aRandomNumber):
	print("try a smaller number next time.")
elif(guess < aRandomNumber):
	print("try a bigger number next time.")