import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':110, 'Queen':10, 'King':10, 'Ace':11} 
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
   def __init__(self,name = 'Gus'):
      self.name = name
      self.all_cards = []

   def add_cards(self,new_cards):
      if type(new_cards) == type([]):
         self.all_cards.extend(new_cards)
      else:
         self.all_cards.append(new_cards)

   def __str__(self):
      return f'Player {self.name} has {len(self.all_cards)} cards.'

class Dealer:
   def __init__(self):
      self.name = 'Dealer'
      self.all_cards = []

   def add_cards(self,new_cards):
      if type(new_cards) == type([]):
         self.all_cards.extend(new_cards)
      else:
         self.all_cards.append(new_cards)

   def __str__(self):
      return f'Player {self.name} has {len(self.all_cards)} cards.'


