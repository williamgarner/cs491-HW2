from Hand import Hand


class Player:
	def __init__(self):
		self.hand = Hand()

	def add_card(self, card):
		self.hand.add_card(card)

	def has_21(self):
		return self.hand.check_for_21()

	def get_hand_value(self):
		return self.hand.get_hand_value()
