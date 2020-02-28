from Card import Card
import random


class Deck:
	def __init__(self):
		self.cards = [Card(v) for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]*4]

	def shuffle(self):
		if len(self.cards) > 1:
			random.shuffle(self.cards)

	def get_top_card(self):
		return self.cards.pop()
