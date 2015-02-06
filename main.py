# github.com/spokenlore
# Version .5
# February 5, 2015

from Shuffle import *

import random, io, os, operator, time

def main():
	start = time.time()
	# Call out to Shuffle.py to start a randomize deck and print to thedeck.txt
	initDeck()
	
	#The following code will be broken down into another function...maybe -Kevin
	deal_card = open('thedeck.txt')	
	deal_card.seek(0)
	print "Hands of dealer"	
	print deal_card.readline(),
	print 'Hidden\n', 
	deal_card.readline()
	
	for x in range(0,5):
		print "Player Hand # ", x+1
		print deal_card.readline(),
		print deal_card.readline(),

#Working on Decision.py ultimately it will return "hit" or "stay" based on probability
 
	print "\nThis program took %s seconds" % (time.time() - start)

if __name__ == '__main__':
	main()