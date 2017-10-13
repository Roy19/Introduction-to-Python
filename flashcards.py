import sys			#Module that helps us use command line arguments in Python
import random


if len(sys.argv)<2:		#Check whether the flashcard name has been supplied to the program in the command line
	print("Must specify a flashcard name. Try again!")
	exit(1)
	
f = open(sys.argv[1],"r")

questions_dict={}

for line in f:
	line = line.strip().split(",")
	question = line[0]
	answer = line[1]
	questions_dict[question]=answer
	
f.close()			#Close the file after using it.

print("Welcome to the flashcard quizzer.")
print("At any time, type 'quit' to quit.")
print("")
	
questions = list(questions_dict.keys())
while True:
	question = random.choice(questions)
	
	print("Question:"+question)
	answer = input("Your guess:")
	
	if answer == 'quit':
		print("Thanks for playing. Goodbye!")
		break
	elif answer==questions_dict[question]:
		print("You're correct!")
	else:
		print("Wrong answer. The correct answer is "+questions_dict[question])

		
	
