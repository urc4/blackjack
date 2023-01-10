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
         while choice not in ['1','11']:
            choice = input(f'Choose {card} to be one(1) or eleven(11): ')
         if choice not in ['1','11']:
            print('Pick a valid choice. Please try again.')
         hand_value += int(choice)
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