from cat import game

deck = game.Deck('abcdefg', 'hijklmnop')

print(deck)

for card in deck:
	print(card, deck.current)
