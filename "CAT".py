import random #it might be imported already from sakubot i guess 
# WARNING ERRORS EVERYWHERE literally first time on python and doing this after around 24h of not sleeping
# Everything would be better if the list of players could be turned into a class, like, much better
# But I don't know how to do that
# Needs try: except: blocks everywhere
# .choose and .join must be commands that give b

def cat(self, channel, nick, text)
	#need the output dunno what you will make it so i'll just call it this for now
	message = "A game of CAT will start shortly! You have 10 seconds to join!"
	out(channel, message)
	time = time.time()
	Players = []
	Playerlist = []
	player0, player1, player2, player3, player4, player5, player6, player7, player8, player9 = []#dunno if correct syntax
	while (time+10) != time.time():
		#i have no idea if this would work but the join func should only be called while while is alive?
		join(channel, nick, text)
	
	if len(Players) > 2 && len(Players) < 10:
		message = "OK! A CAT game is going to start!"
		out(channel, message)
		game = False
	
		for i in range(5):
			player0.append(random.choice(Deck.white)) #there should be a way to shorten this code
			player1.append(random.choice(Deck.white)) #also to not use lists when no player
			player2.append(random.choice(Deck.white)) #which should be almost the same code
			player3.append(random.choice(Deck.white)) #and there must be because otherwise it won't even look like it'll run
			player4.append(random.choice(Deck.white))
			player5.append(random.choice(Deck.white))
			player6.append(random.choice(Deck.white))
			player7.append(random.choice(Deck.white))
			player8.append(random.choice(Deck.white))
			player9.append(random.choice(Deck.white))	
		for n in len(Players):
			Players[n] = [player{n}] #need the same thing that up there ^	
		for not game:
			if highwin != 5
				judge = random.choice(Players)
				Players.remove(judge)
				message = random.choice(Deck.black)
				out(channel, message)
				outputWhite()
				time = time.time()
				while (time+10) != time.time()
					#call choose like when .join
				outputBlack(listblack)
				time = time.time()
				while (time+10) != time.time()
					#same but with .judge
				checkwin()
				Players.append(judge)
				drawWhite()
			else:
				game = True
		
	elif len(Players) >= 10:
		message = "Sorry, we're full!"
		privmsg(channel, nick, message) #then again no idea how you're going to deal with this
	else: 
		message = "Not enough players, I'm sorry."
		out(channel, message)
		break

def join(self, channel, nick, text):
	if nick not in Players:
		Players.append(nick)
	else:
		message = "Stop being such a faggot, {0}".format(nick)
		out(channel, message)

def drawWhite(self, player):
	player{self.player}.append(random.choice(Deck.white)) #need the thing from above

def outputWhite(self):
	for player in Players:
		message = "Choose from here!"
		privmsg(channel, player, message)
		for cards in player{n}:
			message = "(" + cards + ")" + player{n}[cards]
			privmsg(channel, player, message)
			
def outputBlack(self, listblack):
	message = "Judge from these:"
	privmsg(channel, judge, message)
	for i in listblack:
		message = "(" + cards + ")" + i
		privmsg(channel, judge, message)		
		
class Deck:
	def __init__(self, white, black, uwhite, ublack):
		with open(black.txt) as bl:
			self.black = bl.readlines()
		with open(white.txt) as cis:
			self.white = cis.readlines()
			
def choose(self, channel, nick, text, which):
	listblack.append(player{Players.index(nick)}[which])

def judge(self, channel, nick, text, which):
	winner = #there should be some link between "which" and player, but yeah, everything would be easier with classes
	
def checkwin(self, ):
	#returns highwin value
	# dunno what do anymore, just kill me, i'm done
	
	
