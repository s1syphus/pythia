
# Set playing v0.1

import random

'''
There might be a more efficient way to do this but I'm not sure what that is
The statements do short-circuit so the check doesn't take that long
'''

class Card:
	def __init__(self, color, symbol, shading, number):
		self.color = color
		self.symbol = symbol
		self.shading = shading
		self.number = number
	def __str__(self):
		return self.color + " " + self.symbol + " " + self.shading + " " + self.number
	def returnColor(self):
		return self.color	
	def returnSymbol(self):
		return self.symbol	
	def returnShading(self):
		return self.shading	
	def returnNumber(self):
		return self.number	
	def __eq__(self, other):
		if isinstance(other, Card):
			return self.color == other.color and self.symbol == other.symbol and self.shading == other.shading and self.number == other.number

def isSet(card1, card2, card3):
	#check color
	if (card1.returnColor() == card2.returnColor()) and (card1.returnColor() == card3.returnColor()):
		return True
	if (card1.returnColor() != card2.returnColor()) and (card1.returnColor() != card3.returnColor()) and (card2.returnColor() != card3.returnColor()):
		return True
	#check symbol
	if (card1.returnSymbol() == card2.returnSymbol()) and (card1.returnSymbol() == card3.returnSymbol()):
		return True
	if (card1.returnSymbol() != card2.returnSymbol()) and (card1.returnSymbol() != card3.returnSymbol()) and (card2.returnSymbol() != card3.returnSymbol()):
		return True
	#check shading
	if (card1.returnShading() == card2.returnShading()) and (card1.returnShading() == card3.returnShading()):
		return True
	if (card1.returnShading() != card2.returnShading()) and (card1.returnShading() != card3.returnShading()) and (card2.returnShading() != card3.returnShading()):
		return True
	#check number 
	if (card1.returnNumber() == card2.returnNumber()) and (card1.returnNumber() == card3.returnNumber()):
		return True
	if (card1.returnNumber() != card2.returnNumber()) and (card1.returnNumber() != card3.returnNumber()) and (card2.returnNumber() != card3.returnNumber()):
		return True

colors = ['red','green','purple']
symbols = ['squiggles','diamonds', 'ovals']
shading = ['solid', 'striped', 'outlined']
number = ['1','2','3']
deck = []

for i in colors:
	for j in symbols:
		for k in shading:
			for l in number:
				newCard = Card(i,j,k,l)
				deck.append(newCard)
random.shuffle(deck)
curDeck = deck
'''
this is a super naive search method for finding sets
Might switch to something more efficient if it's too slow
'''
setFound = False
currentCards = []
foundSet = []

while len(deck) != 0:
#	while setFound == False:
	currentCards.append(curDeck.pop())
	foundSet = []
	for i in currentCards:
		for j in currentCards:
			for k in currentCards:
				if (i != j and i != k and j != k):
					setFound = isSet(i,j,k)
					print "Set Found!"
					print i
					print j
					print k
					currentCards.remove(i)
					currentCards.remove(j)
					currentCards.remove(k)
					continue	

					





















