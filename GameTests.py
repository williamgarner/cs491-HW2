import unittest
from Game import Game
from Card import Card


class GameTests(unittest.TestCase):
	def test_shuffle_deck_length(self):
		game = Game()
		game.shuffle_deck()
		self.assertEqual(game.deck.cards.__len__(), 52)

	def test_deal_player(self):
		game = Game()
		game.deal_player_a_card()
		self.assertTrue(game.player.hand.cards)
		self.assertEqual(game.player.hand.cards.__len__(), 1)
		self.assertEqual(game.deck.cards.__len__(), 51)

	def test_deal_dealer(self):
		game = Game()
		game.deal_dealer_a_card()
		self.assertTrue(game.dealer.hand.cards)
		self.assertEqual(game.dealer.hand.cards.__len__(), 1)
		self.assertEqual(game.deck.cards.__len__(), 51)

	def test_get_player_card(self):
		game = Game()
		save_card = game.deck.cards[-1]
		game.deal_player_a_card()
		self.assertEqual(game.get_player_cards(), [save_card])

	def test_get_dealer_cards(self):
		game = Game()
		save_card = game.deck.cards[-1]
		game.deal_dealer_a_card()
		self.assertEqual(game.get_dealer_cards(), [save_card])

	def test_dealer_turn_greater_17(self):
		game = Game()
		game.dealer.add_card(Card('A'))
		game.dealer.add_card(Card('9'))
		game.dealers_turn()
		self.assertEqual(game.dealer.get_hand_value(), 20)

	def test_dealer_turn_less_17(self):
		game = Game()
		game.dealer.add_card(Card('1'))
		game.dealer.add_card(Card('9'))
		game.dealers_turn()
		self.assertNotEqual(game.dealer.get_hand_value(), 10)

	def test_winner_dealer(self):
		game = Game()
		game.player.add_card(Card('K'))
		game.dealer.add_card(Card('K'))
		game.dealer.add_card(Card('2'))
		self.assertEqual(game.get_winner(), "Dealer Wins")

	def test_winner_player(self):
		game = Game()
		game.player.add_card(Card('J'))
		game.dealer.add_card(Card('9'))
		self.assertEqual(game.get_winner(), "You Win")

	def test_winner_no_one(self):
		game = Game()
		game.player.add_card(Card('J'))
		game.dealer.add_card(Card('K'))
		self.assertEqual(game.get_winner(), "No one wins")

	def test_deal_first_cards(self):
		game = Game()
		game.deal_first_cards()
		self.assertEqual(game.player.hand.cards.__len__(), 2)
		self.assertEqual(game.dealer.hand.cards.__len__(), 2)




if __name__ == '__main__':
	unittest.main()
