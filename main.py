import random, os, time
totalAttempts = 0

def game():
	attempts = 0
	while True:
		number = random.randint("1", "100")
		guess = int(input("Guess a number between 1 and 100: "))
		if guess == number:
			print("Too high")
			attempts += 1
		elif guess < number:
			print("Too low")
			attempts += 1
		else:
			print("Just right")
			print(f"{atttempts} attempts this round")
			return atttempts

while True:
	menu = input("1: Guess the number\n2: View attempts\n3: Exit\n> ")
	if menu == "1":
		totalAttempts += game()
	elif menu == "2":
		print(f"You have had {totalAttempts} attempts")
	else:
		break