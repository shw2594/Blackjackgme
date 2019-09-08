import random
#Global Variables
suit=('Hearts','Diamonds','Spades','Clubs')
rank=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
value={'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

class Card():
	def __init__(self,suit,rank):
		self.suit=suit
		self.rank=rank
	def __str__(self):
		return self.rank+ " of "+self.suit
    play=true

class Deck():
	def __init__(self):
		self.deck()=[]
		for suit in suit:
			for rank in rank:
				self.deck.append(Card(suit,rank))
	#def __str__(self):
	#	deck_compo= 
test_deck=Deck()
print(test_deck)
