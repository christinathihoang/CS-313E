#   File: War.py
#   Description: This program depicts the outcome of a game of War.
#   Student's Name: Christina Hoang
#   Student's UT EID: ch42297
#   Course Name: CS 313E
#   Unique Number: 86940
#
#   Date Created: 6/23/2017
#   Date Last Modified: 6/26/2017

import random

def getValue(card):

	if len(card) == 3:
		card = Card(card[0:2], card[2])
	else:
		card = Card(card[0], card[1])
	return(card)

def playGame(player, opponent):

	try:
		counter = 0
		while len(player.hand) >= 1 and len(opponent.hand) >= 1:
	
			# counter keeps track of the round number
			counter += 1
			print()
			print("ROUND",counter,":")

			# each player puts topmost card from deck face up
			playerDraw = player.hand.pop(0)
			opponentDraw = opponent.hand.pop(0)
			print("Player 1 plays:", playerDraw)
			print("Player 2 plays:", opponentDraw)
			print(" ")
		
			# retrieve and compare the rank values of each card
			playerCard = getValue(playerDraw)
			opponentCard = getValue(opponentDraw)

			# if player 1 wins the round, both cards are added to player 2's hand
			if playerCard > opponentCard:
				print("Player 1 wins round",counter,":",playerDraw,">",opponentDraw)
				player.hand.append(playerDraw)
				player.hand.append(opponentDraw)

			# if player 2 wins the round, both cards are added to player 1's hand
			elif playerCard < opponentCard:
				print("Player 2 wins round",counter,":",opponentDraw,">",playerDraw)
				opponent.hand.append(playerDraw)
				opponent.hand.append(opponentDraw)

			# if there is a tie, the players go to war
			elif playerCard == opponentCard:

				print("War starts: ",playerDraw,"=",opponentDraw)
				# the first two initially played cards are added to the card pile
				playerCardPile = []
				opponentCardPile = []
				flag = True
				playerCardPile.append(playerDraw)
				opponentCardPile.append(opponentDraw)

				# this loops continues to run as long as the compared cards are tied
				while flag == True:

					# place three cards faced down
					for i in range(0,3):
						print("Player 1 puts",player.hand[0],"face down")
						print("Player 2 puts",opponent.hand[0],"face down")
						playerCardPile.append(player.hand.pop(0))
						opponentCardPile.append(opponent.hand.pop(0))

					# each player draws a fourth card
					playerWarDraw = player.hand.pop(0)
					opponentWarDraw = opponent.hand.pop(0)
					print("Player 1 puts",playerWarDraw,"face up")
					print("Player 2 puts",opponentWarDraw,"face up")

					# retrieve value and compare cards
					playerWarCard = getValue(playerWarDraw)
					opponentWarCard = getValue(opponentWarDraw)

					# if player 1 wins the round, all 10 cards are added to player 2's hand
					if playerWarCard > opponentWarCard:
						print("Player 1 wins round",counter,":",playerWarDraw,">",opponentWarDraw)
						playerCardPile.append(playerWarDraw)
						opponentCardPile.append(opponentWarDraw) 
						player.hand += playerCardPile
						player.hand += opponentCardPile
						playerCardPile = []
						opponentCardPile = []
						flag = False

					# if player 2 wins the round, all 10 cards are added to player 1's hand
					elif playerWarCard < opponentWarCard:
						print("Player 2 wins round",counter,":",opponentWarDraw,">",playerWarDraw)
						playerCardPile.append(playerWarDraw)
						opponentCardPile.append(opponentWarDraw) 
						opponent.hand += playerCardPile
						opponent.hand += opponentCardPile
						playerCardPile = []
						opponentCardPile = []
						flag = False

					# if the compared cards are the same, draw three more hards faced down and one card faced up 
					elif playerWarCard == opponentWarCard:
						playerCardPile.append(playerWarDraw)
						opponentCardPile.append(opponentWarDraw)

			print(" ")
			print("Player 1 now has",len(player.hand),"card(s) in hand:")
			print(player)
			print("Player 2 now has",len(opponent.hand),"card(s) in hand:")
			print(opponent)
			print("\n")

	# create exception in the case that the players run out of cards to continue playing 
	except IndexError:

		# give the rest of the cards to winning player
		#if len(player.hand) < len(opponent.hand):
		#	opponent.hand += cardPile
		#	opponent.hand += player.hand
		#	player.hand = []
		#elif len(opponent.hand) < len(player.hand):
		#	player.hand += opponent.hand
		#	player.hand += cardPile
			

		# print hand
		print("Player 1 now has",len(player.hand),"card(s) in hand:")
		print(player)		
		print("Player 2 now has",len(opponent.hand),"card(s) in hand:")
		print(opponent)


class Card():

	# initialize card and its attributes
	def __init__(self, rank, suit):
		self.suit = suit
		self.rank = rank

		if self.rank == "J":
			self.value = 11
		elif self.rank == "Q":
			self.value = 12
		elif self.rank == "K":
			self.value = 13
		elif self.rank == "A":
			self.value = 14
		else:
			self.value = self.rank

	# string method
	def __str__(self):
		return(str(self.value))

	# equal to method
	def __eq__(self, other):
		return(int(self.value) == int(other.value))

	# less than method
	def __lt__(self, other):
		return(int(self.value) < int(other.value))

	#greater than method
	def __gt__(self, other):
		return(int(self.value) > int(other.value))


class Deck():

	# initialize deck
	def __init__(self):
		self.cardList = ["2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC", \
						"2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD", \
						"2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH", \
						"2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS"]

	# string method
	def __str__(self):
		deck = ""
		for i in range(13):
			deck += self.cardList[i].rjust(4)
		deck += "\n"
		for j in range(13, 26):
			deck += self.cardList[j].rjust(4)
		deck += "\n"
		for k in range(26, 39):
			deck += self.cardList[k].rjust(4)
		deck += "\n"
		for l in range(39, len(self.cardList)):
			deck += self.cardList[l].rjust(4)
		return(deck)

	# metheod to shuffle deck
	def shuffle(self):
		return(random.shuffle(self.cardList))

	# metheod to deal cards to each player, one at a time
	def dealOne(self, player):
		draw = self.cardList.pop(0)
		if len(draw) == 3:
			c = Card(draw[0:2], draw[2])
		else:
			c = Card(draw[0], draw[1])
		player.hand.append(draw)

class Player():

	# initialize the hand of each player
	def __init__(self):
		self.hand = []

	# string method
	def __str__(self):
		if len(self.hand) == 0:
			return(" ")
		elif len(self.hand) <= 13:
			hand = ""
			for i in range(len(self.hand)):
				hand += self.hand[i].rjust(4)
			return(hand)
		elif len(self.hand) <= 26:
			hand = ""
			for i in range(13):
				hand += self.hand[i].rjust(4)
			hand += "\n"
			for j in range(13, len(self.hand)):
				hand += self.hand[j].rjust(4)
			return(hand)
		elif len(self.hand) <= 39:
			hand = ""
			for i in range(13):
				hand += self.hand[i].rjust(4)
			hand += "\n"
			for j in range(13, 26):
				hand += self.hand[j].rjust(4)
			hand += "\n"
			for k in range(26, len(self.hand)):
				hand += self.hand[k].rjust(4)
			return(hand)
		else:
			hand = ""
			for i in range(13):
				hand += self.hand[i].rjust(4)
			hand += "\n"
			for j in range(13, 26):
				hand += self.hand[j].rjust(4)
			hand += "\n"
			for k in range(26, 39):
				hand += self.hand[k].rjust(4)
			hand += "\n"
			for l in range(39, len(self.hand)):
				hand += self.hand[l].rjust(4)
			return(hand)

	# check to see whose hand is empty and return the winner
	def handNotEmpty(self):
		return(len(self.hand) != 0)


def main():
	cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
	print("Initial deck:")
	print(cardDeck)                 # print the deck so we can see that you built it correctly
	print(" ")
	random.seed(15)                 # leave this in for grading purposes
	cardDeck.shuffle()              # shuffle the deck
	print("Shuffled deck:")
	print(cardDeck)                 # print the deck so we can see that your shuffle worked
	print("\n\n\n")

	player1 = Player()              # create a player
	player2 = Player()              # create another player

	for i in range(26):             # deal 26 cards to each player, one at 
	   cardDeck.dealOne(player1)    #   a time, alternating between players
	   cardDeck.dealOne(player2)
	
	print("Initial hands:")
	print("Player 1:")
	print(player1)
	print(" ")
	print("Player 2:")
	print(player2)

	playGame(player1, player2)

	if player1.handNotEmpty():
		print("\n\nGame over.  Player 1 wins!")
	else:
		print("\n\nGame over.  Player 2 wins!")

	print ("\n\nFinal hands:")    
	print ("Player 1:   ")
	print (player1)                 # printing a player object should print that player's hand
	print ("\nPlayer 2:")
	print (player2)                 # one of these players will have all of the cards, the other none
	
main()