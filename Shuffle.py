import random

#Shuffle Deck and print to file 

def initDeck():
	deck = []
	suits = ["d", "c", "h", "s"]
	cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
	for x in suits:
		for y in cards:
			deck.append(x+str(y))
	newdeck = []
	with open('thedeck.txt', "w") as outputfile:
		for y in xrange(0,52):
			drop = int(random.random()*len(deck))
			newdeck.append(deck[drop])
 			
			outputfile.write("%r \n" % deck.pop(drop))

		          
	return newdeck

def generateSamples(filename):
	for x in xrange(0,numSamples):
		deck = initDeck()
		openingHand = deck[0] + " " + deck[1] + "\n"
		print openingHand

def readHand(hand):
	playerhand = Hand(hand)
	# playerhand.display()
	return playerhand