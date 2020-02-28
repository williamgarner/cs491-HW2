class Card(object):
	def __init__(self, value):
		self.value = value
		self.is_ace = value == 'A'
		self.is_ten = self.value == "10" or self.value == "K" or self.value == "Q" or self.value == "J"

	def __repr__(self):
		return self.value

	def get_value(self):
		if self.is_ten:
			return 10
		elif self.is_ace:
			return 1, 11
		else:
			return int(self.value)
