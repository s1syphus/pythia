
# Set playing v0.1

import random

'''
There might be a more efficient way to do this but I'm not sure what that is
The statements do short-circuit so the check doesn't take that long
'''
def isSet(card1, card2, card3):
	#check color
	if (card1[0] == card2[0]) and (card1[0] == card3[0]):
		return True
	if (card1[0] != card2[0]) and (card1[0] != card3[0]) and (card2[0] != card3[0]):
		return True
	
	#check symbol
	if (card1[1] == card2[1]) and (card1[1] == card3[1]):
		return True
	if (card1[1] != card2[1]) and (card1[1] != card3[1]) and (card2[01] != card3[1]):
		return True
	#check shading
	if (card1[2] == card2[2]) and (card1[2] == card3[2]):
		return True
	if (card1[2] != card2[2]) and (card1[2] != card3[2]) and (card2[2] != card3[2]):
		return True
	#check number 
	if (card1[3] == card2[3]) and (card1[3] == card3[3]):
		return True
	if (card1[3] != card2[3]) and (card1[3] != card3[3]) and (card2[3] != card3[3]):
		return True

'''
beginning of program, this whole thing needs to be refactored hard-core
'''




colors = ['red','green','purple']
symbols = ['squiggles','diamonds', 'ovals']
shading = ['solid', 'striped', 'outlined']
number = ['1','2','3']
deck = []
for i in colors:
	for j in symbols:
		for k in shading:
			for l in number:
				newCard = [i,j,k,l]
				deck.append(newCard)
random.shuffle(deck)
curDeck = deck
'''
this is a super naive search method for finding sets
Might switch to something more efficient if it's too slow
'''
setFound = False
currentCards = []
counter = 0
while setFound == False:
	currentCards.append(curDeck.pop())
	print ""
	for i in currentCards:
		print i
	print ""
'''
	for i in currentCards:
		for j in currentCards:
			for k in currentCards:
				if (i != j and i != k):
'''

	#this part is temporary
	counter += 1
	if counter == 10:
		setFound = True		


print "Set Found!"






















