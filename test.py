import random
import copy
from flask import Flask

class card:
	#class for cards
	def __init__(self, Health, Damage):
		self.Health = Health
		self.Damage = Damage
	
	def battle(self, other):
		self.Health = self.Health - other.Damage
		other.Health = other.Health - self.Damage

class hand:
	def __init__(self):
		self.hand = []
	
	def add_to_hand(self, card: card):
		self.hand.append(card)

	def add_to_field(self, index):
		self.hand.pop(index)


class battlefield:
	def __init__(self):
		self.deck1 = []
		self.deck2 = []

	def battle(self):
		if len(self.deck1) > 0 and len(self.deck2) > 0:
			random_int1 = random.randint(0, len(self.deck1) -1)
			random_int2 = random.randint(0, len(self.deck2) -1)
			self.deck1[random_int1].battle(self.deck2[random_int2])

			if self.deck1[random_int1].Health<= 0:
				self.deck1.pop(random_int1)
			
			print(self.deck2[random_int2].Health)
			if self.deck2[random_int2].Health <= 0:
				self.deck2.pop(random_int2)

	def can_battle(self):
		if len(self.deck1) > 0 and len(self.deck2) > 0:
			return True
		return False

	def add_cards_to_deck1(self, cart: card):
		self.deck1.append(cart)
	
	def add_cards_to_deck2(self, cart: card):
		self.deck2.append(cart)


class battle:
	def __init__(self, battlefield):
		self.battlefield = battlefield

	def battle_start(self):
		#print(self.battlefield.deck1)
		#print(self.battlefield.deck1)
		while self.battlefield.can_battle():
			self.battlefield.battle()
			#print("battle")
	
	def winner(self):
		if len(self.battlefield.deck1) > 0:
			return "1 won"

		if len(self.battlefield.deck2) > 0:
			return "2 won"

		return "tie" 


battlefield1 = battlefield()
battlefield1.deck1 =  [card(2, 2), card(3, 1)]
battlefield1.deck2 =  [card(2, 2), card(3, 1)]

battlefield2 = copy.deepcopy(battlefield1)
battle1 = battle(battlefield1)

print("deck1")
for item in battlefield1.deck1:
	print(f"Health: {item.Health}")
	print(f"Damage: {item.Damage}")


print("deck2")
for item in battlefield1.deck2:
	print(f"Health: {item.Health}")
	print(f"Damage: {item.Damage}")

battle1.battle_start()
print(battle1.winner())

battlefield1 = copy.deepcopy(battlefield2)

battlefield1.add_cards_to_deck1(card(10, 10))

battlefield1.add_cards_to_deck2(card(1, 100))
battle1 = battle(battlefield1)

print("deck1")
for item in battlefield1.deck1:
	print(f"Health: {item.Health}")
	print(f"Damage: {item.Damage}")


print("deck2")
for item in battlefield1.deck2:
	print(f"Health: {item.Health}")
	print(f"Damage: {item.Damage}")


battle1.battle_start()
print(battle1.winner())

app = Flask(__name__)

@app.route('/')
def index():
	return "<p>test<p>"

app.run()
