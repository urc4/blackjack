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


def player_bet(player):
   
   bet = 'wrong'
   print(f'{player.name} has ${player.balance}')
   
   while bet.isdigit() == False or int(bet) > player.balance:
      
      bet = input(f'\n{player.name} place your bet for this round: $')

      if bet.isdigit() == False:
         print('Enter a valid amount. Please try again.')
      if int(bet) > player.balance:
         print('Your bet can not top your balance. Please try again.')

   return int(bet)

def player_choice(player):
   choice = 'wrong'
   # hit requests an extra card and stay the opposite
   while choice not in ['h','s']:
      choice = input(f'{player.name} choose to hit(h) or stay(s): ')
      if choice not in ['h','s']:
         print('Pick a valid choice. Please try again.')

   return choice

def valid_hand(hand_value):
   if hand_value > 21:
      print('BUST!')
      return False
   else: 
      return True


# Could make the game automatically take in and understand the player's mind!!!
# instead of asking for him to choose between one or eleven
def hand_value(player):
   hand_value = 0
   for card in player.all_cards:
      if card.rank == 'Ace':
         choice = 'wrong'
         while choice not in [1,11]:
            choice = input(f'Choose ', card, 'to be one(1) or eleven(11): ')
         if choice not in [1,11]:
            print('Pick a valid choice. Please try again.')
         hand_value += choice
      else:
         hand_value += card.value
   return hand_value


def gameon(player):
   choice = 'wrong'
   # hit requests an extra card and stay the opposite
   while choice not in ['y','n']:
      choice = input(f'Does {player.name} want to keep losing money? Yes(y) or No(n): ')
      if choice not in ['y','n']:
         print('Pick a valid choice. Please try again.')

   if choice == 'y':
      return True
   else:
      return False
# Game logic alltogether

player = Player()
dealer = Dealer()

game_on = True
round_count = 0

while game_on:
   round_count += 1
   # Check if players can bet
   # We assume the dealer has an infinite amount of chatter.
   if player.balance < 0:
      print(f'{player.name} has run out of money. Game over, mf.')
      game_on = False
      break

   # Start a new round
   print(f'\nRound {round_count}\n')
   new_deck = Deck()
   new_deck.shuffle()
   player.clear_hand()
   dealer.clear_hand()
   
   # Place bet
   bet_amt = player_bet(player)
   player.place_bet(bet_amt)

   # Give out initial cards
   for num in range(2):
      player.add_cards(new_deck.deal_one())
      dealer.add_cards(new_deck.deal_one())
   
   player.print_cards()
   dealer.show_first_card()

   # Choose to hit or to stay
   player_hand = hand_value(player)
   val_hand = valid_hand(player_hand)
   # Maybe can introduce this to while loop down below
   if val_hand == False:
      game_on = False
      break


   choice = player_choice(player)
   while choice == 'h' and val_hand == True:
      player.add_cards(new_deck.deal_one())
      player.print_cards()
      dealer.show_first_card()
      choice = player_choice(player)
      player_hand = hand_value(player)
      val_hand = valid_hand(player_hand)

   if val_hand == False:
      break


   player.print_cards()
   dealer.print_cards()

   dealer_hand = hand_value(dealer)
   val_hand = valid_hand(dealer_hand)

   if dealer_hand < 17:
      choice = player_choice(dealer)
   while choice == 'h' and val_hand == True:
      dealer.add_cards(new_deck.deal_one())
      player.print_cards()
      dealer.print_cards()
      choice = player_choice(dealer)
      dealer_hand = hand_value(dealer)
      val_hand = valid_hand(dealer_hand)

   if val_hand == False or player_hand > dealer_hand: 
      player.deposit(bet_amt*1.5)
      break
   elif player_hand == dealer_hand:
      player.deposit(bet_amt)
   else:
      pass

game_on = gameon(player)
   