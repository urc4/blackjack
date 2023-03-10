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
      
# Create a jock class that preceeds both player and dealer classes

class Jock : # should I make acces to all_cards private?
   
   def __init__(self):
      self.all_cards = []
   
   def add_cards(self, new_cards):
      if type(new_cards) == type([]):
         self.all_cards.extend(new_cards)
      else:
         self.all_cards.append(new_cards)
         # maybe add type check with an elif or else dont take none

   def clear_hand(self):
      self.all_cards.clear()
      #maybe add a remove card on top but that doesnt make any sense
   # Can i change this for __str__ function but vas to return string type
   def print_cards(self, number_cards = 10):
      if number_cards == 1:
         print(f'\n{self.name} has\n\t{self.all_cards[0]}\n\t      ?')
      else:
         print(f'\n{self.name} has\n')
         for card in self.all_cards:
            print('\t', card)
         print('\n')

# watch out for naming differetn obejct types and functions with the same names
# Could make the game automatically take in and understand the player's mind!!!
# instead of asking for him to choose between one or eleven

#player hand value function has to be different from dealers, maybe 
#could turn this into a method for the classes previously determined
class Player(Jock):
  
   def __init__(self, name = 'Player', balance = 100):
      Jock.__init__(self)
      self.name = name
      self.balance = balance

   def deposit(self, dep_amt):
      self.balance += dep_amt

   def place_bet(self, bet_amt):
      #usually bet ranges from $2 to $500
      if bet_amt <= self.balance:
         self.balance -= bet_amt
      else:
         print(f'Your bet of ${bet_amt} can not top your balance of ${self.balance}')

   def hand_value(self):
      hand_value = 0
      ace_count = 0
   
      for card in self.all_cards:
         if card.rank == 'Ace':
            ace_count += 1
         else:
            hand_value += card.value
   
      if ace_count == 0:
         return hand_value
     
      else:
         possible_hand_values = [hand_value]*(ace_count+1)
         for index in range(ace_count+1):
            possible_hand_values[index] += (ace_count-index)*1 + index*11
         best_hand = min(possible_hand_values)
         for index in range(1,ace_count+1):
            if possible_hand_values[index] <= 21:
               best_hand = possible_hand_values[index]

         return best_hand
# Dealer has to hit until they have at least 17
# Could add inhertiance to player and dealer so as to have same fucntions
class Dealer(Jock):
   # add something like congrats you broke the game now get your ass outtahere
   def __init__(self, balance = 10000):
      Jock.__init__(self)
      self.name = 'Dealer'
      self.balance = balance
   
   def hand_value(self):
      hand_value = 0
      ace_count = 0
   
      for card in self.all_cards:
         if card.rank == 'Ace':
            ace_count += 1
         else:
            hand_value += card.value
   
      if ace_count == 0:
         return hand_value
     
      else:
         possible_hand_values = [hand_value]*(ace_count+1)
         for index in range(ace_count+1):
            possible_hand_values[index] += (ace_count-index)*1 + index*11
         best_hand = min(possible_hand_values)
         for index in range(1,ace_count+1):
            if 17 <= possible_hand_values[index] <= 21:
               best_hand = possible_hand_values[index]
               
         return best_hand



