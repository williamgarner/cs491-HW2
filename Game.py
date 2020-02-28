from Player import Player
from Deck import Deck


class Game:
	def __init__(self):
		self.player = Player()
		self.dealer = Player()
		self.look_at_dealer_card = False
		self.deck = Deck()
		self.account = 100
		self.bet = 0
		self.winnings = 0
		self.game_over = False

	def deal_first_cards(self):
		self.deal_player_a_card()
		self.deal_dealer_a_card()
		self.deal_player_a_card()
		self.deal_dealer_a_card()

	def shuffle_deck(self):
		self.deck.shuffle()

	def check_for_value_over(self):
		return self.player.get_hand_value() > 21

	def deal_player_a_card(self):
		self.player.add_card(self.deck.get_top_card())
		self.game_over = self.check_for_value_over()

	def get_player_cards(self):
		return self.player.hand.cards

	def get_dealer_cards(self):
		return self.dealer.hand.cards

	def deal_dealer_a_card(self):
		card = self.deck.get_top_card()
		self.dealer.add_card(card)

	def dealers_turn(self):
		while self.dealer.get_hand_value() < 17:
			self.dealer.add_card(self.deck.get_top_card())

	def get_winner(self):
		if self.player.get_hand_value() > 21 >= self.dealer.get_hand_value():
			return 'Dealer Wins'
		elif self.dealer.get_hand_value() > 21 >= self.player.get_hand_value():
			return "You Win"
		elif self.dealer.get_hand_value() <= 21 and self.player.get_hand_value() <= 21:
			if self.dealer.get_hand_value() > self.player.get_hand_value():
				return 'Dealer Wins'
			elif self.dealer.get_hand_value() < self.player.get_hand_value():
				return "You Win"
			else:
				return "No one wins"
		else:
			return "No one wins"

