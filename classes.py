import random

# Goal is to beat the dealer and get closer to 21 without going over it
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': None} 
# Ace can be 1 or 11
# Create a class for a card
class Card:

   def __init__(self,suit,rank):
      self.suit = suit
      self.rank = rank 
      self.value = values[rank]

   def __str__(self):
      return f'{self.rank} of {self.suit}' 

# Create a deck class
class Deck:
   
   def __init__(self):
      self.all_cards = []
      for suit in suits:
         for rank in ranks:
            self.all_cards.append(Card(suit,rank))
   
   def shuffle(self):
      random.shuffle(self.all_cards)              

   def deal_one(self):
      return self.all_cards.pop()
      
# Create a player class
class Player:

   def __init__(self,name = 'Player', balance = 100):
      self.name = name
      self.all_cards = []
      self.balance = balance

   def add_cards(self,new_cards):
      if type(new_cards) == type([]):
         self.all_cards.extend(new_cards)
      else:
         self.all_cards.append(new_cards)

   # Can i change this for __str__ function but vas to return string type
   def print_cards(self):
      print(f'\n{self.name} has\n')
      for card in self.all_cards:
         print('\t', card)
      print('\n')

   def clear_hand(self):
      self.all_cards.clear()


   def deposit(self, dep_amt):
      self.balance += dep_amt

   def place_bet(self, bet_amt):
      if bet_amt <= self.balance:
         self.balance -= bet_amt
      else:
         print('Your bet can not top your balance.')


''' 
player = Player()
c1 = Card(suits[0],ranks[1])
c2 = Card(suits[2],ranks[7])
player.add_cards([c1,c2])
player.print_cards()
'''


# Dealer has to hit until they have at least 17
# Could add inhertiance to player and dealer so as to have same fucntions
class Dealer:

   def __init__(self, name = 'Dealer'):
      self.all_cards = []
      self.name = name

   def show_first_card(self):
      print(f'\n{self.name} has\n')
      print('\t', self.all_cards[0])
      print('\t   ?')

   def print_cards(self):
      print(f'\n{self.name} has\n')
      for card in self.all_cards:
         print('\t', card)
      print('\n')

   def add_cards(self,new_cards):
      if type(new_cards) == type([]):
         self.all_cards.extend(new_cards)
      else:
         self.all_cards.append(new_cards)

   def clear_hand(self):
      self.all_cards.clear()
