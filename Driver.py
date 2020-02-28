from Game import Game

game = Game()

print(f"Welcome to Blackjack you have ${game.account}")
print('The dealer will now shuffle the cards')
game.shuffle_deck()
print("Place your bet: ")
game.bet = int(input())
game.deal_first_cards()
choice = 'h'
while not game.game_over and choice != 's':
	print(f"Here are your cards: {game.get_player_cards()}")
	print("Would you like to hit or stand(h or s)?")
	choice = str(input())
	if choice == 'h' or choice == "H":
		game.deal_player_a_card()

game.dealers_turn()
print("Game over!")
print(f"Your hand {game.get_player_cards()}")
print(f"Dealer's hand: {game.get_dealer_cards()}")
print(game.get_winner())
