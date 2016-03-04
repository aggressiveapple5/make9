#Author: Matt Keller
#Date: February 10 2016
import random

ready = raw_input("Type ready when you want the game to begin: ")
ready = ready.lower()
score = 0

if ready == "ready":
	print("Instructions: try to get as close to 9 points as possible without going over. \
You will start with 0 points and be asked if you would like more points. Type 'y' to receive more points or 'n' to stop receiving them.")
	decide = "y"
	
	
	while score < 9.0 and decide == "y": #This means it will quit if either score is over nine or decide is n
		decide = raw_input("Your score is {}. Do you want more points? ".format(score))
		decide = decide.lower()
		if decide == "y":
			score += random.uniform(0.0, 3.0)
		elif decide == "n":
			print("Your final score is {}. Not bad.".format(score))


if score > 9.0:
	print("You lose")
	print("You score was {}.".format(score))

if ready != "ready":
		print("I'm sorry that you don't want to play.")
		
		