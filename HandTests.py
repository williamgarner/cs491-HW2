import unittest
from Hand import Hand
from Card import Card


class HandTests(unittest.TestCase):
	def test_empty_hand(self):
		hand = Hand()
		self.assertEqual(hand.cards, [])
		self.assertFalse(hand.has_ace)

	def test_add_card_ace(self):
		hand = Hand()
		card = Card('A')
		hand.add_card(card)
		self.assertTrue(hand.has_ace)
		self.assertEqual(hand.cards, [card])

	def test_add_card_9(self):
		hand = Hand()
		card = Card('9')
		hand.add_card(card)
		self.assertFalse(hand.has_ace)
		self.assertEqual(hand.cards, [card])

	def test_has_21(self):
		hand = Hand()
		card1 = Card('K')
		card2 = Card('2')
		card3 = Card('9')
		hand.add_card(card1)
		self.assertFalse(hand.has_ace)
		self.assertEqual(hand.cards, [card1])
		self.assertFalse(hand.check_for_21())
		hand.add_card(card2)
		self.assertFalse(hand.has_ace)
		self.assertEqual(hand.cards, [card1, card2])
		self.assertFalse(hand.check_for_21())
		hand.add_card(card3)
		self.assertFalse(hand.has_ace)
		self.assertEqual(hand.cards, [card1, card2, card3])
		self.assertTrue(hand.check_for_21())

	def test_get_without_ace(self):
		hand = Hand()
		card1 = Card('J')
		card2 = Card('7')
		hand.add_card(card1)
		hand.add_card(card2)
		self.assertEqual(hand.get_without_ace(), 17)

	def test_get_with_ace_11(self):
		hand = Hand()
		card1 = Card('A')
		card2 = Card('4')
		hand.add_card(card1)
		hand.add_card(card2)
		self.assertEqual(hand.get_with_ace(), 15)

	def test_get_with_ace_1(self):
		hand = Hand()
		card1 = Card('A')
		card2 = Card('K')
		card3 = Card('2')
		hand.add_card(card1)
		hand.add_card(card2)
		hand.add_card(card3)
		self.assertEqual(hand.get_with_ace(), 13)

	def test_get_hand_value_no_ace(self):
		hand = Hand()
		card1 = Card('4')
		card2 = Card('2')
		card3 = Card('3')
		hand.add_card(card1)
		hand.add_card(card2)
		hand.add_card(card3)
		self.assertEqual(hand.get_hand_value(), 9)

	def test_get_hand_value_with_ace_11(self):
		hand = Hand()
		card1 = Card('A')
		card2 = Card('2')
		card3 = Card('3')
		hand.add_card(card1)
		hand.add_card(card2)
		hand.add_card(card3)
		self.assertEqual(hand.get_hand_value(), 16)

	def test_get_hand_value_with_ace_1(self):
		hand = Hand()
		card1 = Card('A')
		card2 = Card('K')
		card3 = Card('3')
		hand.add_card(card1)
		hand.add_card(card2)
		hand.add_card(card3)
		self.assertEqual(hand.get_hand_value(), 14)


if __name__ == '__main__':
	unittest.main()
