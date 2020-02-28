import unittest
from Deck import Deck


class DeckTests(unittest.TestCase):
	def test_deck_length(self):
		self.assertEqual(Deck().cards.__len__(), 52)

	def test_deck_shuffle_legth(self):
		deck = Deck()
		deck.shuffle()
		self.assertEqual(deck.cards.__len__(), 52)

	def test_get_top_card(self):
		deck = Deck()
		top_card = deck.cards[-1]
		self.assertEqual(deck.get_top_card(), top_card)

	def test_get_top_card_shuffle(self):
		deck = Deck()
		deck.shuffle()
		top_card = deck.cards[-1]
		self.assertEqual(deck.get_top_card(), top_card)


if __name__ == '__main__':
	unittest.main()
