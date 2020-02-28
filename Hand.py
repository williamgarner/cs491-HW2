class Hand:
	def __init__(self):
		self.cards = []
		self.has_ace = False

	def __repr__(self):
		return self.cards

	def add_card(self, card):
		if card.is_ace:
			self.has_ace = True
		self.cards.append(card)

	def check_for_21(self):
		return self.get_hand_value() == 21

	def get_without_ace(self):
		total = 0
		for card in self.cards:
			total += card.get_value()
		return total

	def get_with_ace(self):
		total = 0
		total_with_ace = 0
		for card in self.cards:
			if card.is_ace:
				total += 1
				total_with_ace += 11
			else:
				total += card.get_value()
				total_with_ace += card.get_value()
		if total <= 21 < total_with_ace:
			return total
		elif total_with_ace <= 21 < total:
			return total_with_ace
		elif total_with_ace <= 21 and total <= 21:
			return max(total, total_with_ace)
		else:
			return 22

	def get_hand_value(self):
		if self.has_ace:
			return self.get_with_ace()
		else:
			return self.get_without_ace()
