import unittest
from Card import Card


class CardTests(unittest.TestCase):
	def test_value_1(self):
		self.assertEqual(Card("2").get_value(), 2)

	def test_value_ace(self):
		card = Card("A")
		self.assertEqual(card.get_value(), (1, 11))
		self.assertTrue(card.is_ace)

	def test_value_king(self):
		card = Card("K")
		self.assertEqual(card.get_value(), 10)
		self.assertTrue(card.is_ten)

	def test_value_ten(self):
		card = Card("10")
		self.assertEqual(card.get_value(), 10)
		self.assertTrue(card.is_ten)


if __name__ == '__main__':
	unittest.main()
