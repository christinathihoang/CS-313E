#	File: Bowling.py
#	Description: This program calculates the final scores of each bowling game.
#	Student's Name: Christina Hoang
#	Student's UT EID: ch42297
#	Course Name: CS 313E
#	Unique Number: 86940
#
#	Date Created: 6/5/2017
#	Date Last Modified: 6/9/2017

# strip original string of whitespace
def originalParse(game):
	new_game = []
	for pins in game:
		if (pins == " ") or (pins == "\n"):
			continue
		else:
			new_game.append(pins)
	return (new_game)

# strip original string of whitespace and replace -, /, X with numbers 
def parse(game):
	game = list(game)
	new_game = []
	for pins in game:
		if (pins == " ") or (pins == "\n"):
			continue
		elif (pins == "X"):
			new_game.append(int(10))
		elif (pins == "-"):
			new_game.append(int(0))
		elif (pins == "/"):
			new_game.append(pins)
		else:
			new_game.append(int(pins))
	return (new_game)

def main():
	# open file
	infile = open("scores.txt", "r")

	# go through each line in the file
	for game in infile:
		originalGame = list(originalParse(game))
		game = list(parse(game))
		frame = 1
		runningTotal = 0
		runningScores = []

		# print frame number 
		for j in range(1, 11):
			if (j == 10):
				print (str(j).center(5))
			else:
				print (" " + str(j).center(3), end = " ")
		print ()
		print ("+----+----+----+----+----+----+----+----+----+-----+")
		
		# print number of pins knocked down per frame
		originalFrame = 1
		while (originalFrame <= 10):
			if (originalFrame == 10):
				if (len(originalGame) == 3):
					print ("|" + str(originalGame[0]) + " " + str(originalGame[1]) + " " + str(originalGame[2]) + "|", end = " ")
					originalFrame += 1
				else:
					print ("|" + str(originalGame[0]) + " " + str(originalGame[1]) + "  " + "|", end = " ")
					originalFrame += 1
			elif (originalGame[0] == "X"):
				print ("|" + "  " + str(originalGame[0]), end = " ")
				originalFrame += 1
				originalGame.remove(originalGame[0])
			else:
				print ("|" + str(originalGame[0]) + " " + str(originalGame[1]), end = " ")
				originalFrame += 1
				originalGame.remove(originalGame[0])
				originalGame.remove(originalGame[0])
		print ()
		
		# determine the running total of game
		while (frame <= 10):
			if (frame == 10) and (len(game) == 3):
				frame += 1
				if (game[0] == 10) and (game[1] == 10) and (game[2] == 10):
					runningTotal += 30
					runningScores.append(runningTotal)
				elif (game[0] == 10) and (game[1] < 10) and (game[2] == "/"):
					runningTotal += 20
					runningScores.append(runningTotal)
				elif (game[0] == 10) and (game[1] < 10) and (game[2] < 10):
					runningTotal += (10 + game[1] + game[2])
					runningScores.append(runningTotal)
				elif (game[0] < 10) and (game[1] == "/"):
					runningTotal += (10 + game[2])
					runningScores.append(runningTotal)
				elif (game[0] == 10) and (game[1] == 10) and (game[2] < 10):
					runningTotal += (20 + game[2])
					runningScores.append(runningTotal)

			else:
				if (game[0] == 10):
					if (game[2] == "/"):
						runningTotal += 20
						frame += 1
						runningScores.append(runningTotal)
						game.remove(game[0])
					else:
						runningTotal += (10 + game[1] + game[2])
						frame += 1
						runningScores.append(runningTotal)
						game.remove(game[0])
				elif (game[0] < 10) and (game[1] != "/"):
					runningTotal += (game[0] + game[1])
					frame += 1
					runningScores.append(runningTotal)
					game.remove(game[0])
					game.remove(game[0])
				elif (game[0] < 10) and (game[1] == "/"):
					runningTotal += (10 + game[2])
					frame += 1
					runningScores.append(runningTotal)
					game.remove(game[0])
					game.remove(game[0])

		# print running total 
		frame = 1
		for x in runningScores:
			if (frame == 10):
				print ("|".rjust(1) + str(x).rjust(3) + "|".rjust(3), end = " ")
				frame += 1
			else:
				print ("|".rjust(1) + str(x).rjust(3), end = " ")
				frame += 1
		print ()
		print ("+----+----+----+----+----+----+----+----+----+-----+")
		print ()
		print ()

	# close file
	infile.close()
main()