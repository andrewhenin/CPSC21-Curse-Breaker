"""
This program is a curse breaker. The object of the game for 
the player is to guess the rune sequence. For the game,
4 runes in the sequence will be used, and each rune
can only show up once (i.e., there are no duplicates in the
sequence). Each turn, the player enters a guess, and the
program then reports how many of the player’s guesses are
correct (using exact matches, meaning the right rune in
the right place).

Name: Andrew Henin
Date: March 2022
"""

from random import choice

def main():
	rounds = printWelcome()
	print()
	rune_list = ["ansuz", "isaz", "sowilo", "hagalaz", "algiz", "ehwaz", "naudiz"]
	code = [ "", "", "", ""]
	code = generate_code(rune_list, code)
	correct_runes = 0
	for i in range(rounds):
		if correct_runes != 4:
			guess = oneTurn(rune_list, i)
			correct_runes = check_guess(code, guess)
			print("%d / 4 correct" % (correct_runes))
	if correct_runes == 4:
		print("\nCongratulations, you win! The curse is broken!")
	elif correct_runes != 4:
		print("\nSorry, you lose; good thing there's a big stack of cursed artifacts!")
		
	
	
def printWelcome():
	"""
	This function prints the welcome message along with the
        rules of the game. It also asks the user how many rounds.
	parameters: none
	return: rounds
	side effects: none
	"""
    
	print("Welcome to Curse Breaker!\n")
	print("The object of the game for the player is to guess the \n\
rune sequence, e.g. sowilo isaz hagalaz ansuz. For our game, \n\
we’ll use 4 runes in the sequence, and we’ll say each rune \n\
can only show up once (i.e., there are no duplicates in the \n\
sequence). Each turn, the player enters a guess, and the \n\
program then reports how many of the player’s guesses are \n\
correct (using exact matches, meaning the right rune in \n\
the right place).\n")

	rounds = int(input("Enter the number of turns the game should take: "))
	print("The player has %d rounds to guess the secret code.\n\
If they do, they win! Otherwise, the artifact explodes\n\
and the evil wizard wins!\n" % (rounds))

	return rounds



def print_runes(rune_list):
	"""
	This function prints the rune_list with vertical bars between
	every element in the list.
	parameters: rune_list
	return: none
	"""
				
	runes_str = "| "			#this is an accumulator string
	for i in range(len(rune_list)):
		runes_str = runes_str + rune_list[i] + " | "
	print(runes_str)




def get_rune(runes, number):
	
	"""
	This function asks the user to choose a rune for the numbered position.
	Parameters: runes, number
	returns: rune_input
	side effects: none
	"""
	
	rune_input = input("Enter rune %d: " % (number))
	while rune_input not in runes:
		print("%s is not a valid rune; please choose from the \
following runes:" % (rune_input))
		print_runes(runes)
		rune_input = input("Enter rune %d: " % (number))
	return rune_input





def get_guess(runes, guess):
	
	"""
	This function takes one list of the possible runes and
	a second list to store the user's guesses. 
	It gets 4 valid inputs from the user and append them to 
	a list.
	parameters: runes, gusss
	return: guess
	side effects: none
	"""
	
	for i in range(4):
		rune = get_rune(runes, i+1)
		guess.append(rune)
	return guess



def oneTurn(runes, number):
	
	"""
	This function prints each turn depending on the user's input.
	Parameters: rounds, number
	returns: guess
	side effects: none
	"""
	
	print("============")
	print("Turn %d" % (number+1))
	print("Please enter four legal runes. Your choices are:")
	print_runes(runes)
	guess = []
	guess = get_guess(runes, guess)
		
	guessedRunesStr = "| "			#this is an accumulator string
		
	for i in range(len(guess)):
		guessedRunesStr = guessedRunesStr + guess[i] + " | "
	print()	
	print("You guessed:")
	print(guessedRunesStr)
		
	return guess
		



def generate_code(runes, code):
	
	"""
	This function generates four random runes without repition.
	These generated random runes will be the ones that the user will
	trey to guess.
	Parameters: runes, code
	Return: code
	side effects: none
	"""
	
	code[0] = choice(runes)
	for i in range(1, len(code)):     
		code[i] = choice(runes)
		while code[i] in code[:i]:
			code[i] = choice(runes)
	return code
	
	


def check_guess(code, guess):
	
	"""
	This function will check the guess of the user against the generated
	code.
	Parameters: code, guess
	returns: correct
	side effects: none
	"""
	
	correct = 0
	
	for i in range(len(guess)):
		if guess[i] == code[i]:
			correct = correct + 1
	return correct

main()












































