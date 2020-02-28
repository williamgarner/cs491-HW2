import unittest
from Player import Player
from Card import Card


class PlayerTests(unittest.TestCase):
	def test_empty_player(self):
		player = Player()
		self.assertEqual(player.hand.cards, [])
		self.assertFalse(player.hand.has_ace)

	def test_add_card(self):
		card = Card('A')
		player = Player()
		player.add_card(card)
		self.assertEqual(player.hand.cards, [card])

	def test_has_21_true(self):
		card1 = Card('A')
		card2 = Card('K')
		player = Player()
		player.add_card(card1)
		player.add_card(card2)
		self.assertEqual(player.hand.cards, [card1, card2])
		self.assertTrue(player.has_21())

	def test_has_21_false(self):
		card1 = Card('A')
		card2 = Card('3')
		player = Player()
		player.add_card(card1)
		player.add_card(card2)
		self.assertEqual(player.hand.cards, [card1, card2])
		self.assertFalse(player.has_21())

	def test_get_hand_value_ace_11(self):
		card1 = Card('A')
		card2 = Card('K')
		player = Player()
		player.add_card(card1)
		player.add_card(card2)
		self.assertEqual(player.hand.cards, [card1, card2])
		self.assertEqual(player.get_hand_value(), 21)

	def test_get_hand_value_ace_1(self):
		card1 = Card('A')
		card2 = Card('K')
		card3 = Card('3')
		player = Player()
		player.add_card(card1)
		player.add_card(card2)
		player.add_card(card3)
		self.assertEqual(player.hand.cards, [card1, card2, card3])
		self.assertEqual(player.get_hand_value(), 14)

	def test_get_hand_value_no_ace(self):
		card1 = Card('K')
		card2 = Card('3')
		player = Player()
		player.add_card(card1)
		player.add_card(card2)
		self.assertEqual(player.hand.cards, [card1, card2])
		self.assertEqual(player.get_hand_value(), 13)



if __name__ == '__main__':
	unittest.main()
